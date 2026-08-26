# FastLED Reciprocal License

This repository publishes the canonical text and supporting materials for the
proposed **FastLED Reciprocal License 1.0**. Despite its name, the license is a
general-purpose instrument that may be applied to software from any project.
It is not limited to the FastLED codebase.

> [!IMPORTANT]
> The current text is release candidate `1.0-rc3`, identified as
> `LicenseRef-FastLED-Reciprocal-1.0-rc3`. It is preliminary legal drafting,
> is not OSI-approved, and has not completed the attorney gate in
> `LEGAL-REVIEW.md`. The identifier without an `-rc` suffix is reserved for a
> reviewed release.

## License text and software rights are separate

The license does not require a universal "owner." Zachary Vorhies currently
maintains the canonical license-text repository and its version history. That
text-maintenance role does not make Zach, FastLED, or this repository the
owner, separate-permission grantor, or enforcement claimant for software that another
project places under the license.

The roles are intentionally separate:

| Role | Authority |
|---|---|
| Canonical text maintainer | Publishes and versions the reusable license text |
| Adopting rights holder or Contributor | Applies the license and grants rights in its Contributions |
| Separate-permission grantor | Grants separate written permission only when independently authorized for the relevant software |
| Enforcement claimant | Enforces only rights or promises for which it has the required ownership, authorization, or standing |

Publishing or copying `LICENSE` does not transfer software copyrights or
appoint the text maintainer to enforce an adopter's code.

## Design

The license is one self-contained instrument derived from Mozilla Public
License 2.0 under MPL Section 10.3. It is a monetization-triggered reciprocal
open-source license that is not OSI-approved. It preserves a file-level
Covered Software boundary: independent files in a Larger Work may remain
proprietary under Section 11.2.

The license's mission is to return privately maintained improvements to the
official source project when those improvements materially enable non-exempt
monetization. Before the first Monetization Event for each modified version,
the modifier must publish the Compliance Source for the covered portion
through the official upstream project as a public pull request, public fork,
or complete reproducible patch. Genuine educational, scholarly, media, and
unrestricted-donation activities are exempt under the exact boundaries in
Section 11.1.

An adopting project identifies its **Upstream Repository** and **Official
Reporting Location** in or with the Exhibit A notice. Those project-specific
designations do not alter the canonical license text and do not make either
repository's maintainer a rights holder.

Separate written permission is optional and project-specific. Section 11.3(g)
recognizes only written authorization from all necessary software
rightsholders or their authorized licensing entity. No one is required to
offer that permission, and the canonical license repository cannot grant
exceptions for third-party software merely because it publishes this text.

GPL-family compatibility is enabled by default through the MPL-style
Secondary License mechanism. If a recipient validly elects GPL 2.0 or later,
LGPL 2.1 or later, or AGPL 3.0 or later, the elected license controls where its
terms conflict with this license. The FastLED license and applicable provenance
notices travel with the covered code to the extent the elected license permits.
An adopter may instead attach Exhibit B to opt out of Secondary Licenses.

Each canonical version is immutable. Verbatim copying is permitted, but the
license text may not be altered and still presented as the FastLED Reciprocal
License. An adopter selects either the pinned version only or that version or
later; omission defaults to the pinned version only. A software rightsholder
who wants different terms publishes a separately licensed release or fork
without changing grants already made for earlier releases.

The generic `LICENSE-AI-AGENT-INSTRUCTIONS.md` notice is part of the license
and must be included by every adopting project under Section 11.7(a). The
inclusion obligation binds the human or legal entity exercising the copyright
license. The notice does not pretend that an automated agent is a contracting
party or independently subject to damages.

## Contents

- `LICENSE` — current reusable release-candidate text.
- `MPL-2.0.txt` — unmodified MPL 2.0 source retained for provenance; it is not
  incorporated into the license.
- `PROVENANCE.md` — derivation and immutable-version records.
- `LEGAL-REVIEW.md` — attorney-review gate and unresolved drafting decisions.
- `paralegal-research/` — license-agnostic research corpus for attorney review.
- `NOTICE-TEMPLATE.txt` — optional source notice for adopters.
- `header-policy.toml`, `header-policy.schema.json`, and
  `tools/license_headers.py` — optional example tooling for repositories that
  want automated source-file notices.
- `LICENSE-AI-AGENT-INSTRUCTIONS.md` — required generic AI Coding Agent Notice,
  also reproduced as Exhibit C and incorporated by Section 11.7.
- `ai-policy.toml` — machine-readable summary of the required notice and its
  legal boundary.
- `LICENSE-MIT-LEGACY` and `NOTICE-TEMPLATE-MIT-LEGACY.txt` — FastLED migration
  examples, not requirements imposed on other adopters.

## Applying the license to a project

1. Obtain project-specific legal review and confirm that the people applying
   the license have sufficient rights in the software they are offering.
2. Copy an immutable reviewed license release into the adopting repository.
3. Attach the Exhibit A notice or the corresponding SPDX identifier to the
   Covered Software. Record whether the adoption is this version only or this
   version or later, plus the project's Upstream Repository and Official
   Reporting Location.
4. Include `LICENSE-AI-AGENT-INSTRUCTIONS.md` as the complete generic Exhibit C
   notice. It is required for every adopting project, whether or not that
   project expects AI-assisted development.
5. Preserve third-party notices and licenses. Do not overwrite separately
   licensed or generated material with a project-wide header.
6. If the project offers separate written permissions, publish its own contact
   and authorization process separately from the canonical license text.

No change to the FastLED software repository is necessary to draft, publish,
study, or use this license text. FastLED remains under its existing license
unless and until the FastLED project separately adopts a reviewed version.

## Optional header tool

Repositories that choose to use the example tool need only [uv](https://docs.astral.sh/uv/):

```console
uv run tools/license_headers.py inventory --profile release
uv run tools/license_headers.py check --profile release
uv run tools/license_headers.py update --profile release
uv run tools/license_headers.py apply --profile release
```

The included policy is a starting point, not part of the legal instrument.
Each adopter must replace its roots, exclusions, and provenance while
retaining the required generic AI Coding Agent Notice. The tool refuses to stamp the final
non-`-rc` identifier until `LEGAL-REVIEW.md` records approval.

Reviewed releases should be immutable tags with a recorded content digest.
Adopters should copy a selected release rather than follow mutable legal text
during a build or release.

## References

- [Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/)
- [SPDX custom LicenseRef syntax](https://spdx.github.io/spdx-spec/v2.3/using-SPDX-short-identifiers-in-source-files/)
- Preliminary research and attorney-review issues are tracked in this
  repository's GitHub issue list.
