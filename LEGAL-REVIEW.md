# Legal review record

Status: **PENDING**

Before tagging `v1.0.0`, recommending adoption, or stamping the
non-release-candidate identifier `LicenseRef-FastLED-Reciprocal-1.0`, an
open-source licensing attorney must review and approve the license text. The
header tool enforces this mechanically: `tools/license_headers.py` refuses
`update` or `apply` for a non-`-rc` identifier until this file records
`Status: APPROVED`.

Approval must record reviewer identity, date, reviewed commit, and any
required changes. Removing this gate without documented review is not
approval.

## AI first-pass review

An AI multi-agent first-pass review of rc1 was filed as GitHub issues #2-#8
on 2026-08-24. The license was restructured in response. Rc2 then separated
the reusable license text from the rights, repositories, and commercial
licensing decisions of any particular adopting project. That work is input
to, not a substitute for, attorney review.

## Decisions applied pending attorney ratification

1. **Reusable-text architecture.** The FastLED Reciprocal License may be
   applied to software from any project. The canonical repository and its
   maintainers publish and version the text only. They do not become the
   owner, commercial licensor, beneficiary, or enforcement claimant for an
   adopter's software. Each Contributor grants rights only in its
   Contributions. Any separate commercial license must come from the
   applicable Contributors or someone independently authorized by them.
   Confirm Sections 10.1 and 11.3(g).
2. **Single-instrument construction.** The license is one self-contained
   document: a modified MPL 2.0 renamed under its Section 10.3, with Mozilla
   references limited to the permitted differs-from note, the Reciprocal
   Terms in Section 11, and rewritten Exhibits. `MPL-2.0.txt` remains only as
   provenance material.
3. **Sections 11.3 and 11.7(a) condition only the copyright grant.** Section
   2.7 does not condition the Contributor patent grant in Section 2.1(b) on
   the public-availability rule or required AI-notice inclusion. Confirm this
   allocation.
4. **Exhibit B closes Secondary-License distribution.** Sections 1.5, 3.3,
   and 11.6 make the license deliberately GPL-incompatible in exchange for
   making Section 11.3 non-bypassable. Confirm this trade-off before
   recommending adoption.
5. **Zero-day timing is intentional and per version.** The development period
   before a commercial Triggering Transfer is the compliance window.
   Publication after the transfer restores rights only prospectively under
   Sections 5.1 and 11.3(f). Confirm the condition-versus-covenant framing and
   remedy consequences.
6. **The Triggering Transfer is recurring and modifier-bound.** It includes
   the free-software-with-paid-product scenario and excludes specified
   intra-group, manufacturing, lease, reseller, and network-only conduct.
   Confirm each boundary and the interaction with applicable exhaustion law.
7. **The AI Coding Agent Notice is generic and mandatory.** Exhibit C and
   `LICENSE-AI-AGENT-INSTRUCTIONS.md` contain the same project-agnostic notice.
   Section 11.7(a) requires every adopter and source distributor to include a
   complete copy as a copyright-license condition. Section 11.7(b) separately
   states that an automated agent is not made a contracting party or
   enforcement target and that its operating guidance adds no further
   condition. Confirm that distinction and every distribution path.
8. **Release-candidate status is explicit.** The current identifier is
   `LicenseRef-FastLED-Reciprocal-1.0-rc2`; the final identifier remains gated.

## Attorney checklist

- the Section 10 distinction between canonical text publication and each
  adopter's software ownership, licensing authority, and standing;
- the Section 11.1 definitions of optional Upstream Repository, Modified
  Covered Software, Triggering Transfer, and Publicly Available;
- the Section 11.3 condition, duration, third-party-interference safe harbor,
  prospective-only model, and project-specific separate-license valve;
- Section 2.7 condition scope and the *Jacobsen*/*MDY* condition-versus-covenant
  framing;
- the Exhibit B and GPL-incompatibility decision;
- the modified Sections 1.4, 1.5, 1.8, 3.1, 3.3, 3.4, 4, 9, and 10 against MPL
  2.0, including compliance with MPL Section 10.3;
- Contributor copyright and patent grants and the requirement that each
  adopter separately validate provenance, authority, and third-party notices;
- compatibility with downstream licenses, registries, and SCA tooling; and
- the mandatory inclusion and agent-directed legal-effect boundaries of the
  generic AI Coding Agent Notice.

## Open items

- Whether to modify Section 8's defendant-principal-place litigation rule.
- Whether to add a BUSL/FSL-style sunset or reversion clause.
- Whether unmodified MPL 2.0 plus a nonbinding upstreaming norm and
  project-specific commercial licensing would better meet adopter goals than
  this bespoke instrument.
