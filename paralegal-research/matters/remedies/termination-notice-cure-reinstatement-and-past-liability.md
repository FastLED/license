---
id: PR-0011
title: Termination, notice, cure, reinstatement, and past liability
question: "When an alleged GPL-, AGPL-, LGPL-, or MPL-style license breach occurs, what do termination, notice, cure, and reinstatement provisions do to current and past liability?"
short_answer: "The exact license version controls the permission timeline. GPLv2 and LGPLv2.1 terminate automatically on breach and do not supply an express cure; GPLv3, AGPLv3, and LGPLv3 use GPLv3 section 8's provisional and, in specified circumstances, permanent reinstatement; MPL 2.0 uses its own notice-and-cure mechanism. Reinstatement can restore permission prospectively on the text and facts, but it is not a blanket release of already-accrued copyright or contract claims. No general U.S. rule turns a later cure into automatic immunity, and state-law notice, waiver, and damages questions require the selected forum's law."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, state-contract-law-forum-dependent]
licenses: [GPL-2.0, GPL-3.0, AGPL-3.0, LGPL-2.1, LGPL-3.0, MPL-2.0]
actors: [copyright-owner, licensor, distributor, modifier, service-operator, recipient]
conduct: [distribute, convey, provide-network-access, omit-notice, withhold-source, cure, continue-after-termination]
topics: [termination, notice, cure, reinstatement, past-liability]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0013, PR-0015]
supersedes: []
---

# PR-0011: Termination, notice, cure, reinstatement, and past liability

> Preliminary research for attorney review. Not legal advice and not a license or policy decision.

## Scope and assumptions

This is a U.S. federal copyright baseline with an express state-contract-law limit. It assumes a claimant with the necessary copyright or contract standing, identifies the exact version and allegedly noncompliant release, and separates a current request to stop or cure conduct from money or other relief for earlier acts. It does not decide whether any particular combination is covered, whether a network-only act infringes an exclusive right, or whether an individual notice was effective.

## Short answer

"Termination" is not one doctrine across these instruments. GPLv2 section 4 and LGPLv2.1 section 13 say that rights terminate automatically upon a prohibited act and do not give an express cure path. GPLv3 section 8, incorporated by AGPLv3 and LGPLv3, likewise provides automatic termination but adds provisional reinstatement when the violation stops and permanent reinstatement in the text's specified first-notice circumstances. MPL 2.0 section 8 instead gives a notice-and-cure route with its own periods and conditions. These clauses describe license permission; they do not answer ownership, infringement, contract formation, damages, or the remedy.

A timely cure can be central to whether ongoing conduct remains unlicensed. It should not be described as an automatic erasure of past acts: the texts do not contain a universal retrospective release, and the reviewed U.S. GPL record contains no controlling final decision that does so. In *Fisher*, GPLv3 cure and conveyance were fact disputes, not a final immunity holding. Forum-specific contract doctrines (notice, material breach, waiver, limitation of damages) may affect a contract claim independently.

## Analysis

### Build a version-and-event timeline before characterizing liability

For each release, record the governing text, the claimed triggering act, when permission ended if it did, notice sent and received, cessation, cure steps, reinstatement trigger, and conduct after that point. GPLv2/LGPLv2.1 lack GPLv3's stated cure/reinstatement language; importing it changes the result. GPLv3/AGPLv3/LGPLv3 section 8 distinguishes provisional and permanent reinstatement. MPL 2.0 is file-level and has a distinct section 8 process. License text is operative evidence, not a judicial holding. See the [license landscape](../license-comparison/copyleft-source-availability-license-landscape.md) and the linked license cards below.

### Current conduct is different from a claim for historical conduct

If permission is valid again, a prohibitory copyright injunction ordinarily targets future unlicensed acts, not conduct now authorized. That does not resolve remedies for a prior period: actual damages/profits require statutory proof, statutory damages and fees have registration-timing limits, and a contract claim turns on applicable state law. The statute separately supplies the copyright remedial menu; it does not make a cure clause a damages release. [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md) and [AUTH-0090](../../authorities/statutes/us-copyright-registration-and-limitations.md) identify those separate gates.

### Notice is a textual and evidentiary issue, not a universal prerequisite

GPLv2's automatic-termination text is unlike GPLv3's specified notice/reinstatement route and MPL's notice-and-cure design. Whether a particular email, recipient, address, alleged repeat violation, or cure satisfies the text is fact-sensitive. A court may also need to decide whether the challenged term is a copyright condition or a contract covenant. *Jacobsen* and *MDY* are the relevant but forum-limited frameworks; no card in this corpus establishes a version-neutral notice rule.

### Reported enforcement materials do not collapse the distinction

The BusyBox settlements reported publication and conditional reinstatement, but settlements show negotiated terms, not a judicial construction of every cure clause. *Fisher* left material GPLv3 questions for factfinding. *Artifex* and *SFC v. Vizio* do not establish retrospective immunity. The absence of a final U.S. AGPL section 13 merits judgment is a bounded research gap, not proof that none exists.

## Scenario matrix

| Scenario | Likely claim question | Relief a court could consider | Main uncertainty |
|---|---|---|---|
| GPLv2 distributor later posts source | Was the earlier distribution unlicensed under §4? | Past copyright remedies if proven; future restraint only for unlicensed acts | No express GPLv2 cure; facts and applicable law |
| GPLv3/AGPLv3 first violation cured after notice | Did §8's stated conditions reinstate permission? | Declaration or tailored prospective relief; historical remedies remain separately analyzed | Notice, timing, repeat-violation status, covered conduct |
| MPL 2.0 file-level noncompliance | Was notice/cure under §8 satisfied? | Contract/copyright relief under the chosen theory | Exact file, notice, governing law |
| Network-only AGPL allegation | Does §13 create an enforceable claim and what is the current permission status? | Potential contract/equitable theory; not an established routine source order | Copyright nexus, standing, affirmative-relief standards |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [GPL-2.0](../../authorities/licenses/gnu-gpl-v2.md), [LGPL-2.1](../../authorities/licenses/gnu-lgpl-v2-1.md) | Automatic termination; no express cure in the standard text | License text only |
| [GPL-3.0](../../authorities/licenses/gnu-gpl-v3.md), [AGPL-3.0](../../authorities/licenses/gnu-agpl-v3.md), [LGPL-3.0](../../authorities/licenses/gnu-lgpl-v3.md) | Section 8 termination/reinstatement mechanics | License text only |
| [MPL-2.0](../../authorities/licenses/mozilla-public-license-v2.md) | Separate notice-and-cure structure | License text only |
| [*Fisher v. SAS Automation*](../../authorities/cases/fisher-v-sas-automation-summary-judgment.md) | Cure/conveyance questions may remain factual | Trial-level partial summary judgment; no final GPL remedy |
| [*Jacobsen*](../../authorities/cases/jacobsen-v-katzer.md), [*MDY*](../../authorities/cases/mdy-industries-v-blizzard.md) | Conditions/covenants affect theory | Circuit-specific and fact/text limited |
| [BusyBox/Monsoon](../../authorities/cases/busybox-monsoon-settlement.md) | Conditional reinstatement can be negotiated | Settlement, not awarded relief |

## What would change the answer

- The exact license version, notice record, conduct, and cure chronology.
- A selected state and governing-law clause for a contract claim.
- Proof that an asserted condition has a copyright nexus, or a final decision construing the exact clause.
- A later final U.S. AGPL section 13 or GPLv3 section 8 merits decision.

## Open questions for counsel

- Does the chosen forum treat the relevant obligation as a condition, covenant, or both?
- What release/version and rightsholder chain supports claims for each historical act?
- Is a cure/reinstatement provision intended to release prior claims, or should that consequence be stated separately in a settlement?

## Repository implications

This analysis does not justify changing `LICENSE` or treating any cure clause as a universal past-liability release.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial remedies-doctrine research | Agent; attorney review pending |
