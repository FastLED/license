# FastLED licensing

This repository is the versioned source of truth for the proposed **FastLED
Reciprocal License 1.0**, its AI-agent guidance, and the source-header
compliance tooling used by FastLED releases.

> [!IMPORTANT]
> The current text is a release candidate, self-identified by its SPDX
> identifier `LicenseRef-FastLED-Reciprocal-1.0-rc1`. It must not be
> described as OSI-approved, as the Mozilla Public License 2.0, or as legal
> advice. The bare identifier `LicenseRef-FastLED-Reciprocal-1.0` is
> reserved for the attorney-reviewed text, and the header tool refuses to
> stamp it until `LEGAL-REVIEW.md` records approval. FastLED remains
> MIT-licensed until a FastLED release explicitly adopts a reviewed
> version.

## Design

The license is a single self-contained instrument: a modified Mozilla
Public License 2.0 (renamed under MPL §10.3, with FastLED as license
steward) whose Section 11 adds the FastLED Additional Terms. It preserves
file-level copyleft and the Larger Work boundary — independent
applications, sketches, firmware logic, and products may remain
proprietary — and adds one condition: **when a modified FastLED version is
first commercially transferred, its complete source must already be
public** (public fork/repository, or a public base-commit + full-diff
patch).

The timing model is deliberate: the development period before first sale
*is* the compliance window. Working in a public fork from the start is
continuous compliance with nothing further owed (Section 11.3(b)). There
is no post-sale cure that rewrites history — units reproduced or shipped
before publication were never licensed (Section 11.3(f)) — while
publication restores rights going forward under Section 5.1. The trigger
is per modified version and binds the party who created or commissioned
the modification, never downstream resellers, contract manufacturers, or
lessees (Section 11.1).

Two deliberate trade-offs, recorded in `LEGAL-REVIEW.md` for attorney
ratification: Exhibit B is attached, so the code cannot be relicensed
under GPL-family Secondary Licenses (closing the bypass that would
otherwise make Section 11.3 optional); and Section 11.3 conditions only
the copyright grant, not contributors' patent grants.

## Contents

- `LICENSE` — FastLED Reciprocal License 1.0-rc1: the complete,
  self-contained instrument (modified MPL 2.0 + Section 11 + Exhibits).
- `MPL-2.0.txt` — the unmodified MPL 2.0 base text, retained only for
  provenance comparison (see `PROVENANCE.md`). Not part of the license.
- `LICENSE-AI-AGENT-INSTRUCTIONS.md` — informational, non-binding
  guidance for AI coding agents; authorization-first (see LICENSE §11.7).
- `ai-policy.toml` — machine-readable summary of that guidance.
- `LICENSE-MIT-LEGACY` — the historical FastLED MIT license. Ship it in
  every distributed artifact, not just the repository.
- `NOTICE-TEMPLATE.txt` — canonical three-line source header (SPDX line +
  removable AI-policy reference).
- `NOTICE-TEMPLATE-MIT-LEGACY.txt` — additive header variant for files
  with surviving MIT-era third-party authorship.
- `LEGAL-REVIEW.md` — review gate, applied decisions, attorney checklist.
- `paralegal-research/` — indexed, preliminary legal research, reusable
  authority notes, research workflow, and future-question backlog.
- `header-policy.toml` and `header-policy.schema.json` — policy format and
  an integration example.
- `tools/license_headers.py` — one-command inventory, check, update, and
  apply tool.

## Header tool

Only [uv](https://docs.astral.sh/uv/) is required:

```console
uv run tools/license_headers.py inventory --profile release
uv run tools/license_headers.py check --profile release
uv run tools/license_headers.py update --profile release
uv run tools/license_headers.py apply --profile release
```

The tool uses a compatible system ripgrep or downloads a pinned, SHA-256
verified ripgrep with `zccache download`. Successful checks are
fingerprinted with `zccache fp`, so unchanged runs do not invoke ripgrep
again. Policy, tool, license-text, and review-status changes invalidate
the same fingerprint as source changes.

`update` is fail-closed: it inserts missing managed notices and replaces
only known older FastLED notices (including the previous four-line
`-1.0` header, which upgrades to the current three-line `-rc1` form).
Unknown SPDX identifiers, malformed legal preambles, and unclassified
source are reported for review. Exclusions require a reason and
provenance. Rewriting is atomic and preserves BOMs, shebangs, encoding
lines, newline style, final-newline state, and file mode. `update` and
`apply` additionally refuse to stamp a non-`-rc` identifier until
`LEGAL-REVIEW.md` records `Status: APPROVED`.

## Adoption checklist (before FastLED adopts a reviewed release)

1. **Attorney review** per `LEGAL-REVIEW.md`; ratify the recorded
   decisions; tag the reviewed text and switch the policy id to the
   bare identifier.
2. **Ownership audit before the first `apply` in FastLED**: build a
   per-file provenance map (git blame by surviving lines); files with
   material third-party MIT-era authorship take the additive
   `NOTICE-TEMPLATE-MIT-LEGACY.txt` header instead of a replacement —
   MIT's notice-preservation condition is what the relicensing authority
   rests on.
3. **Inbound=outbound**: land DCO sign-off and a `CONTRIBUTING.md`
   statement in the FastLED repository before adoption so post-adoption
   contributions have a clear inbound license.
4. **Register the copyright** in each FastLED release with the U.S.
   Copyright Office within the 17 U.S.C. §412 windows — statutory
   damages and fee-shifting are where the license's leverage lives.
5. **Tooling ecosystem**: submit the reviewed text to the SPDX License
   List (`spdx/license-list-XML`; the BUSL-1.1 precedent shows non-OSI
   status is not disqualifying), to ScanCode LicenseDB, and to the FOSSA
   and Black Duck known-license databases; host the canonical text at a
   permanent URL.
6. **Announcement playbook** (per the HashiCorp/Terraform lesson):
   public rationale post well in advance, a hard version boundary with
   historical releases staying MIT (LICENSE §11.4), and the header
   rewrite as one atomic, reviewable commit.
7. Optionally, contact the top historical contributors by surviving-line
   count for written relicensing consent — not legally required under
   the MIT sublicensing path, but it converts the strongest available
   objection into a non-event.

## Versioning and adoption

Reviewed releases are immutable tags. An adopting repository copies the
license documents and tool, records the source tag/commit and SHA-256
manifest, and never follows mutable legal text during a build or release.
The initial reviewed release is intended to be `v1.0.0`; no such reviewed
release exists until legal approval is recorded in `LEGAL-REVIEW.md`.

## References

- [Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/)
- [SPDX custom LicenseRef syntax](https://spdx.github.io/spdx-spec/v2.3/using-SPDX-short-identifiers-in-source-files/)
- AI first-pass legal review: issues
  [#2](https://github.com/FastLED/license/issues/2)–[#8](https://github.com/FastLED/license/issues/8)
