# FastLED licensing

This repository is the versioned source of truth for the proposed **FastLED
Reciprocal License 1.0**, its AI-agent instructions, and the source-header
compliance tooling used by FastLED releases.

> [!IMPORTANT]
> The license is a release candidate pending review by an open-source licensing
> attorney. It must not be described as OSI-approved, as the Mozilla Public
> License 2.0, or as legal advice. FastLED remains MIT-licensed until a FastLED
> release explicitly adopts a reviewed version.

The candidate is structurally based on MPL 2.0. It preserves file-level
copyleft and the Larger Work boundary while requiring same-day public source
or a complete public bug-report patch for modifications of FastLED when they
are first sold. Independent
applications, sketches, firmware logic, products, and other larger works may
remain proprietary.

## Contents

- `LICENSE` — FastLED Reciprocal License 1.0 release candidate.
- `LICENSE-AI-AGENT-INSTRUCTIONS.md` — behavioral, legally non-remedial AI
  instructions.
- `LICENSE-MIT-LEGACY` — the historical FastLED MIT license.
- `NOTICE-TEMPLATE.txt` — canonical source discovery notice.
- `header-policy.toml` and `header-policy.schema.json` — policy format and an
  integration example.
- `tools/license_headers.py` — one-command inventory, check, update, and apply
  tool.

## Header tool

Only [uv](https://docs.astral.sh/uv/) is required:

```console
uv run tools/license_headers.py inventory --profile release
uv run tools/license_headers.py check --profile release
uv run tools/license_headers.py update --profile release
uv run tools/license_headers.py apply --profile release
```

The tool uses a compatible system ripgrep or downloads a pinned, SHA-256
verified ripgrep with `zccache download`. Successful checks are fingerprinted
with `zccache fp`, so unchanged runs do not invoke ripgrep again. Policy and
tool changes invalidate the same fingerprint as source changes.

`update` is fail-closed: it inserts missing managed notices and replaces only
known older FastLED notices. Unknown SPDX identifiers, malformed legal
preambles, and unclassified source are reported for review. Exclusions require
a reason and provenance. Rewriting is atomic and preserves BOMs, shebangs,
encoding lines, newline style, final-newline state, and file mode.

## Versioning and adoption

Reviewed releases are immutable tags. An adopting repository copies the
license documents and tool, records the source tag/commit and SHA-256 manifest,
and never follows mutable legal text during a build or release. The initial
reviewed release is intended to be `v1.0.0`; no such reviewed release exists
until legal approval is recorded in `LEGAL-REVIEW.md`.

## References

- [Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/)
- [SPDX custom LicenseRef syntax](https://spdx.github.io/spdx-spec/v2.3/using-SPDX-short-identifiers-in-source-files/)
