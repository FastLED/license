# Legal review record

Status: **PENDING**

Before tagging `v1.0.0`, adopting this license in FastLED, or stamping the
non-release-candidate identifier `LicenseRef-FastLED-Reciprocal-1.0`, an
open-source licensing attorney must review and approve the license text.
The header tool enforces this mechanically: `tools/license_headers.py`
refuses `update`/`apply` for a non-`-rc` identifier until this file records
`Status: APPROVED`.

Approval must record reviewer identity, date, reviewed commit, and any
required changes. Removing this gate without documented review is not
approval.

## AI first-pass review (2026-08-24)

An AI multi-agent first-pass review was completed and filed as issues
[#2](https://github.com/FastLED/license/issues/2)–[#8](https://github.com/FastLED/license/issues/8)
(meta: #8). The license was restructured in response. That review is input
to — not a substitute for — the attorney review above.

## Decisions applied in the restructuring (pending attorney ratification)

These were applied with the review's recommended defaults, plus steward
direction on timing. The reviewing attorney must confirm each on the
record:

1. **Single-instrument construction.** The license is now one
   self-contained document: a modified MPL 2.0 (renamed per its Section
   10.3, FastLED as steward, Mozilla references limited to the permitted
   differs-from note) with the Additional Terms as Section 11 and
   rewritten Exhibits. `MPL-2.0.txt` remains only as the unmodified base
   text for provenance comparison.
2. **Section 11.3 is an express condition of the copyright grant only**
   (Section 2.7). The contributor patent grant under 2.1(b) is
   deliberately NOT conditioned on Section 11.3 — contributors never
   agreed to have their patents armed as a sales-disclosure tripwire.
   Confirm this allocation.
3. **Exhibit B is attached; Secondary-License distribution is closed**
   (Sections 1.5, 3.3, 11.6). This makes the license deliberately
   GPL-incompatible in exchange for making Section 11.3 non-bypassable.
   Confirm this trade-off with the steward; it cannot be had both ways.
4. **Zero-day timing is intentional and per-version** (steward decision,
   2026-08-24). The development period before first commercial transfer
   is the compliance window; developing in a public fork is standing
   compliance (11.3(b)). There is no post-transfer cure that
   retroactively authorizes: units reproduced or transferred before
   publication remain unlicensed (11.3(f)), while publication reinstates
   prospectively under Section 5.1. Confirm the condition/covenant
   framing and the 11.3(f) interaction with Section 5.1.
5. **The trigger is "Triggering Transfer",** per-version and recurring,
   bound to the party that created or commissioned the modifications,
   with carve-outs for intra-group transfers, contract manufacturers,
   leases that convey no copy, and downstream resellers, plus a
   free-firmware-with-paid-product limb and an explicit SaaS statement
   (11.1). The term "First Sale" was removed to avoid collision with the
   17 U.S.C. §109 exhaustion doctrine.
6. **AI-agent guidance is fully de-legalized** (Section 11.7): not part
   of the license, excluded from the Section 3.4 notice-integrity rule,
   header lines reduced and marked removable, document reordered
   authorization-first, machine-readable `ai-policy.toml` added.
7. **Release-candidate status moved from prose into the identifier**
   (`LicenseRef-FastLED-Reciprocal-1.0-rc1`); the former LICENSE §4
   self-review clause was removed from the instrument and lives here.

## Attorney checklist

- the Section 11.1 definitions (Official FastLED Repository, Modified
  FastLED, Triggering Transfer, Publicly Available);
- the Section 11.3 condition: mechanics, duration, third-party
  interference safe harbor, 11.3(f) remedy model, separate-license valve;
- Section 2.7 condition scope (copyright-only) and the Jacobsen/MDY
  condition-vs-covenant framing;
- the Exhibit B / GPL-incompatibility trade-off (decision 3 above);
- the modified Sections 1.4, 1.5, 1.8, 3.1, 3.3, 3.4, 4, 9, 10 against
  MPL 2.0, and whether the Section 10.3 rename obligations are satisfied;
- contributor copyright/patent grants, provenance, and the MIT
  relicensing path (sublicensing theory; notice preservation — see the
  ownership-audit item in README);
- compatibility with downstream licenses, package registries, and SCA
  tooling; and
- the informational, non-remedial character of the AI-agent guidance and
  `ai-policy.toml`.

## Open items deliberately not decided here

- Whether to modify Section 8 (defendant's-forum litigation venue,
  inherited from MPL) for an enforcement-oriented license.
- Whether to add a BUSL/FSL-style sunset or reversion clause.
- The strategic comparison recorded in issue #8: unmodified MPL-2.0 plus
  a published upstreaming norm plus commercial licensing, versus this
  bespoke instrument. The steward has elected to proceed with the bespoke
  instrument; counsel should still price the comparison.
