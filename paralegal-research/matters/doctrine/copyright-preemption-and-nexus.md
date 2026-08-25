---
id: PR-0007
title: Copyright preemption and copyright nexus
question: "When are state-law public-license claims preempted under 17 U.S.C. § 301, and when does a claimed breach have a sufficient copyright nexus?"
short_answer: "Section 301 preempts state rights in copyright subject matter only when they are equivalent to §106 rights. A state claim with a genuinely extra contractual element may survive, but circuit doctrine differs and a promise that merely restates copyright control may still be preempted. Separately, a copyright claim must connect the breach to a licensed exclusive act. Neither label answers the other question."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, US-Ninth-Circuit, US-Second-Circuit, California, New-York]
licenses: [GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, source-available]
actors: [copyright-owner, contributor, distributor, service-operator, recipient]
conduct: [reproduce, modify, distribute, convey, deploy, provide-network-access, withhold-source]
topics: [preemption, copyright-nexus, contract]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0005, PR-0006, PR-0008, PR-0010]
supersedes: []
---

# PR-0007: Copyright preemption and copyright nexus

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: a party asserting a state contract/beneficiary claim or federal
infringement claim over licensed software. Trigger: an asserted source, notice,
payment, non-use, network, or deployment promise. This is a U.S. §301 synthesis
only; it does not resolve foreign preemption, choice of law, or remedies.

## Short answer

Section 301(a) asks whether the work falls within copyright subject matter and
whether the asserted state right is equivalent to §106 rights
([AUTH-0070](../../authorities/statutes/us-copyright-subject-matter-and-preemption.md)).
In the Second Circuit, *Forest Park* held a pleaded implied promise to pay is
an extra element and avoided preemption; in the Ninth Circuit, en banc *Montz*
reached that result for California's implied payment-for-use theory. Those are
not holdings that every contract or beneficiary claim survives. Nor does a
non-preempted contract claim automatically establish infringement: under *MDY*,
a copyright claim independently needs a breach of permission connected to an
exclusive right.

## Analysis

### Keep the two inquiries separate

| Inquiry | Question | Source/limit |
|---|---|---|
| §301 subject matter | Is the asserted work within §§102/103 subject matter, including uncopyrightable material fixed in a work? | *Forest Park* says uncopyrightable ideas fixed in a treatment can satisfy this prong; Second Circuit only |
| §301 equivalency | Does state law require an extra qualitative element? | *Forest Park* and *Montz* identify an implied promise to pay; exact promises matter |
| Copyright nexus | Did a condition limit a §106 act? | *MDY* binds Ninth Circuit; different circuits may formulate the issue differently |
| Remedy | Does a surviving theory support the requested source delivery or injunction? | Separate state equitable law and standing; not decided here |

The same source promise may support different theories: an owner may allege
infringement after unlicensed conveyance; a recipient may allege a contract
right to source; and either claim may fail for different reasons. The pending
Vizio litigation is an allegation/procedural example, not a rule.

### Application to license patterns

GPL/LGPL/MPL/EPL/CDDL/EUPL source terms tied to distribution or conveyance are
often framed as permission conditions. If a recipient seeks source as a
contract beneficiary, §301 equivalency and state beneficiary law must be
separately tested. AGPL, OSL, RPL, and SSPL extend text duties to remote use or
deployment; that breadth can strengthen a distinct performance promise but can
also make a §106 nexus less obvious when no copy is distributed. Source-
available use/service restrictions (BUSL, ELv2, Commons Clause, FSL, PolyForm)
are even more text- and state-law dependent; the corpus found no exact-version
merits authority deciding their §301 treatment.

These are inferences from text, not holdings. A court could find an additional
promise, preemption, no contract, no condition, or a different nexus based on
the exact wording and facts.

### Contrary authority and limits

*Forest Park* expressly did not decide whether every promise to pay escapes
preemption, particularly an adhesion-like agreement that creates a de facto
copyright monopoly. The *Montz* dissent would have found the asserted
non-use/non-disclosure theory equivalent, demonstrating the importance of the
promise's content. *Graham* also shows that a valid state contract claim for
nonpayment does not necessarily end copyright permission.

## Scenario matrix

| Scenario | §301 risk | Nexus risk |
|---|---|---|
| Owner alleges GPL conveyance without source | Contract claim may duplicate §106 if only control asserted | Map source term to conveyance and condition |
| Recipient seeks promised source under state law | Extra performance/beneficiary element may survive | Recipient lacks owner status for infringement |
| AGPL network user requests §13 source | State contract claim needs formation/extra element | No-copy §106 connection unsettled |
| ELv2 hosted-service dispute | Contract restriction may be distinct | Must identify exercised exclusive right |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0070](../../authorities/statutes/us-copyright-subject-matter-and-preemption.md) | Statutory two-prong baseline | Text requires circuit application |
| [AUTH-0072](../../authorities/cases/forest-park-pictures-v-universal.md) | New York implied promise to pay | Rule 12 stage; not public license |
| [AUTH-0074](../../authorities/cases/montz-v-pilgrim-films.md) | California implied payment promise | Ninth Circuit, state-law specific |
| [AUTH-0002](../../authorities/cases/mdy-industries-v-blizzard.md) | Separate copyright-nexus requirement | Ninth Circuit only |
| [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) | Recipient source-performance theory alleged | Pending, no merits decision |

## What would change the answer

- Governing state law, the exact promise and remedy, factual manifestation of
  assent, and whether copying/conveyance actually occurred.
- Controlling §301 or AGPL/network-source authority.

## Open questions for counsel

- Does the contemplated pleading seek a right beyond §106, and can it be proved
  without recasting an infringement claim?
- Who has standing for each theory and what state remedy is being sought?

## Repository implications

No contract language or license choice follows from this doctrine synthesis.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial doctrine synthesis for issue #17 | Agent; attorney review pending |
