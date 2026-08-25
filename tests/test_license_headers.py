import hashlib
import os
import stat
import tempfile
from pathlib import Path

import pytest

from tools import license_headers as subject


def write_policy(
    root: Path,
    *,
    old_ids: tuple[str, ...] = (),
    license_id: str = "LicenseRef-FastLED-Reciprocal-1.0-rc1",
) -> subject.Policy:
    policy_path = root / "header-policy.toml"
    policy_path.write_text(
        "\n".join(
            [
                "schema_version = 1",
                f"old_license_ids = [{', '.join(repr(value) for value in old_ids)}]",
                "[license]",
                f'id = "{license_id}"',
                "header_version = 1",
                'ai_document = "LICENSE-AI-AGENT-INSTRUCTIONS.md"',
                "[profiles.release]",
                'roots = ["src"]',
                'extensions = ["h", "hpp", "cpp", "py"]',
                "[comments]",
                'h = "//"',
                'hpp = "//"',
                'cpp = "//"',
                'py = "#"',
                "[[exclusions]]",
                'pattern = "src/vendor/**"',
                'reason = "fixture vendor"',
                'provenance = "fixture LICENSE"',
                "",
            ]
        ),
        encoding="utf-8",
    )
    (root / "src").mkdir()
    return subject.load_policy(policy_path, "release")


def test_missing_header_updates_and_is_idempotent(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "demo.cpp.hpp"
    source.write_bytes(b"#pragma once\r\nint demo();")

    finding = subject.classify(source, policy)
    assert finding.state is subject.State.MISSING
    assert subject.update_file(finding, policy)
    assert subject.classify(source, policy).state is subject.State.CURRENT
    assert b"\r\n" in source.read_bytes()
    assert not source.read_bytes().endswith(b"\n")
    assert not subject.update_file(subject.classify(source, policy), policy)


def test_bom_shebang_encoding_and_mode_are_preserved(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "script.py"
    source.write_bytes(subject.UTF8_BOM + b"#!/usr/bin/env python3\n# coding: utf-8\nprint('ok')\n")
    source.chmod(0o744)

    assert subject.update_file(subject.classify(source, policy), policy)
    updated = source.read_bytes()
    assert updated.startswith(subject.UTF8_BOM + b"#!/usr/bin/env python3\n# coding: utf-8\n")
    assert b"# SPDX-License-Identifier: LicenseRef-FastLED-Reciprocal-1.0-rc1" in updated
    if os.name != "nt":
        assert stat.S_IMODE(source.stat().st_mode) == 0o744


def test_known_old_header_is_upgraded_without_touching_body(tmp_path: Path) -> None:
    old_id = "LicenseRef-FastLED-Reciprocal-0.9"
    policy = write_policy(tmp_path, old_ids=(old_id,))
    source = tmp_path / "src" / "old.h"
    source.write_text(
        f"// SPDX-License-Identifier: {old_id}\n"
        "// AI LICENSE: OLD-AI.md\n"
        "// AI agents must read that file before substantial FastLED changes.\n"
        "// Substantial AI changes must be reported upstream with a reproducible patch.\n"
        "\n#pragma once\n",
        encoding="utf-8",
    )

    finding = subject.classify(source, policy)
    assert finding.state is subject.State.OUTDATED
    assert subject.update_file(finding, policy)
    assert source.read_text(encoding="utf-8").endswith("\n#pragma once\n")
    assert subject.classify(source, policy).state is subject.State.CURRENT


def test_legacy_four_line_header_upgrades_to_current_form(tmp_path: Path) -> None:
    legacy_id = "LicenseRef-FastLED-Reciprocal-1.0"
    policy = write_policy(tmp_path, old_ids=(legacy_id,))
    source = tmp_path / "src" / "legacy.h"
    source.write_text(
        f"// SPDX-License-Identifier: {legacy_id}\n"
        "// AI LICENSE: LICENSE-AI-AGENT-INSTRUCTIONS.md\n"
        "// AI agents must read that file before substantial FastLED changes.\n"
        "// Substantial AI changes must be reported upstream with a reproducible patch.\n"
        "\n#pragma once\n",
        encoding="utf-8",
    )

    finding = subject.classify(source, policy)
    assert finding.state is subject.State.OUTDATED
    assert subject.update_file(finding, policy)
    text = source.read_text(encoding="utf-8")
    assert "AI agents must read" not in text
    assert "AI-Policy: LICENSE-AI-AGENT-INSTRUCTIONS.md" in text
    assert text.endswith("\n#pragma once\n")
    assert subject.classify(source, policy).state is subject.State.CURRENT


def test_review_gate_allows_rc_identifier(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    assert subject.review_gate(policy) is None


def test_review_gate_fails_closed_without_review_record(tmp_path: Path) -> None:
    policy = write_policy(tmp_path, license_id="LicenseRef-FastLED-Reciprocal-1.0")
    error = subject.review_gate(policy)
    assert error is not None and "no LEGAL-REVIEW.md" in error


def test_review_gate_blocks_pending_and_allows_approved(tmp_path: Path) -> None:
    policy = write_policy(tmp_path, license_id="LicenseRef-FastLED-Reciprocal-1.0")
    review = tmp_path / "LEGAL-REVIEW.md"
    review.write_text("# Legal review record\n\nStatus: **PENDING**\n", encoding="utf-8")
    error = subject.review_gate(policy)
    assert error is not None and "does not record Status: APPROVED" in error
    review.write_text(
        "# Legal review record\n\nStatus: **APPROVED**\nReviewer: A. Lawyer\n",
        encoding="utf-8",
    )
    assert subject.review_gate(policy) is None


def test_conflicting_spdx_fails_closed(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "foreign.h"
    original = b"// SPDX-License-Identifier: MIT\n#pragma once\n"
    source.write_bytes(original)

    finding = subject.classify(source, policy)
    assert finding.state is subject.State.CONFLICT
    with pytest.raises(ValueError, match="refusing to rewrite"):
        subject.update_file(finding, policy)
    assert source.read_bytes() == original


def test_current_header_plus_conflicting_spdx_fails_closed(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "dual.h"
    source.write_text(
        "\n".join(subject.expected_lines(policy, "h"))
        + "\n// SPDX-License-Identifier: MIT\n#pragma once\n",
        encoding="utf-8",
    )
    assert subject.classify(source, policy).state is subject.State.CONFLICT


def test_spdx_after_long_legal_preamble_is_not_ignored(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "long.h"
    source.write_text(
        "".join(f"// legal preamble line {number}\n" for number in range(30))
        + "// SPDX-License-Identifier: MIT\n#pragma once\n",
        encoding="utf-8",
    )
    assert subject.classify(source, policy).state is subject.State.CONFLICT


def test_partial_managed_notice_is_malformed(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "partial.hpp"
    source.write_text("// AI LICENSE: LICENSE-AI-AGENT-INSTRUCTIONS.md\n", encoding="utf-8")
    assert subject.classify(source, policy).state is subject.State.MALFORMED


def test_exclusion_is_byte_for_byte_unchanged(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    vendor = tmp_path / "src" / "vendor"
    vendor.mkdir()
    source = vendor / "foreign.cpp"
    original = b"// SPDX-License-Identifier: BSD-3-Clause\n"
    source.write_bytes(original)

    finding = subject.classify(source, policy)
    assert finding.state is subject.State.EXCLUDED
    assert not subject.update_file(finding, policy)
    assert source.read_bytes() == original


def test_dry_run_reports_change_without_writing(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    source = tmp_path / "src" / "dry.h"
    source.write_bytes(b"#pragma once\n")
    finding = subject.classify(source, policy)
    assert subject.update_file(finding, policy, dry_run=True)
    assert source.read_bytes() == b"#pragma once\n"


def test_ripgrep_inventory_works_without_git(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    (tmp_path / "src" / "owned.h").write_text("#pragma once\n", encoding="utf-8")
    vendor = tmp_path / "src" / "vendor"
    vendor.mkdir()
    (vendor / "foreign.cpp").write_text("int x;\n", encoding="utf-8")
    rg = subject.resolve_ripgrep(tmp_path)

    findings = subject.inventory(policy, rg)
    assert [(item.relative, item.state) for item in findings] == [
        ("src/owned.h", subject.State.MISSING),
        ("src/vendor/foreign.cpp", subject.State.EXCLUDED),
    ]


def test_ripgrep_inventory_does_not_honor_ignore_files(tmp_path: Path) -> None:
    policy = write_policy(tmp_path)
    (tmp_path / ".gitignore").write_text("src/ignored.h\n", encoding="utf-8")
    (tmp_path / "src" / "ignored.h").write_text("#pragma once\n", encoding="utf-8")
    rg = subject.resolve_ripgrep(tmp_path)
    assert [item.relative for item in subject.inventory(policy, rg)] == ["src/ignored.h"]


@pytest.mark.parametrize("root", ["../outside", "/absolute", "C:/absolute", "."])
def test_policy_rejects_unsafe_roots(tmp_path: Path, root: str) -> None:
    policy_path = tmp_path / "header-policy.toml"
    policy_path.write_text(
        "schema_version = 1\n"
        "[license]\n"
        'id = "LicenseRef-FastLED-Reciprocal-1.0"\n'
        "header_version = 1\n"
        'ai_document = "LICENSE-AI-AGENT-INSTRUCTIONS.md"\n'
        "[profiles.release]\n"
        f'roots = ["{root}"]\n'
        'extensions = ["h"]\n'
        "[comments]\n"
        'h = "//"\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="repository-relative"):
        subject.load_policy(policy_path, "release")


def test_artifact_manifest_matches_files() -> None:
    root = Path(__file__).parents[1]
    for line in (root / "ARTIFACTS.sha256").read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == expected


def test_zccache_fingerprint_success_failure_and_invalidation() -> None:
    # zccache deliberately excludes the global clud temporary root. Put this
    # fixture under the checkout so the production scanner sees real inputs.
    with tempfile.TemporaryDirectory(prefix="runtime_fp_", dir=Path(__file__).parent) as temp:
        root = Path(temp)
        policy = write_policy(root)
        source = root / "src" / "cached.h"
        source.write_text(
            "\n".join(subject.expected_lines(policy, "h")) + "\n\n#pragma once\n",
            encoding="utf-8",
        )
        rg = subject.resolve_ripgrep(root)

        assert subject.fingerprint(policy, "release", "check") == 0
        assert subject.mark_success_stably(policy, "release", rg)
        # Some Windows filesystems never report a stable cache hit. That is a
        # performance-only condition: the scanner must fall back to a fresh
        # compliance scan instead of failing or blessing an unstable state.
        assert subject.fingerprint(policy, "release", "check") in (0, 1)
        source.write_text("#pragma once\n// changed\n", encoding="utf-8")
        assert subject.fingerprint(policy, "release", "check") == 0
        assert subject.fingerprint(policy, "release", "mark-failure") == 0
        assert subject.fingerprint(policy, "release", "check") == 0


def test_pinned_assets_cover_supported_ci_platforms() -> None:
    assert set(subject.RIPGREP_ASSETS) == {
        ("Windows", "x86_64"),
        ("Linux", "x86_64"),
        ("Linux", "aarch64"),
        ("Darwin", "x86_64"),
        ("Darwin", "arm64"),
    }
    assert all(len(digest) == 64 for _, digest in subject.RIPGREP_ASSETS.values())
