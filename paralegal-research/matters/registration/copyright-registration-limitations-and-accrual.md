---
id: PR-0014
title: Copyright registration, limitations, and accrual
question: "How do U.S. copyright registration, remedy eligibility, limitations, accrual, and continuing conduct constrain enforcement of reciprocal/source-availability obligations?"
short_answer: "For a United States work, 17 U.S.C. section 411(a) generally requires preregistration or registration (or a refusal after proper delivery) before instituting an infringement action; Fourth Estate adopts the registration, not merely application, approach. Section 411 is a claim-processing precondition, not a jurisdictional bar. Section 412 separately restricts statutory damages and fees for specified timing patterns, while sections 504-505 remain the remedy provisions. Section 507(b) supplies a three-year period after accrual. Petrella recognizes separate accrual for successive infringing acts; Warner Chappell holds that, if a claim is timely under a discovery rule, the Act has no separate three-year damages cap, while expressly not deciding whether the discovery rule governs. These copyright rules do not automatically govern a contract claim, which depends on state law and any choice-of-law clause."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, state-contract-law-forum-dependent]
licenses: [GPL-2.0, GPL-3.0, AGPL-3.0, LGPL-2.1, LGPL-3.0, MPL-2.0, analogous-source-availability]
actors: [copyright-owner, licensor, contributor, distributor, service-operator, recipient]
conduct: [reproduce, distribute, convey, provide-network-access, post-termination-conduct]
topics: [registration, statutory-damages, fees, limitations, accrual, continuing-conduct]
confidence: high
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0011, PR-0013]
supersedes: []
---

# PR-0014: Copyright registration, limitations, and accrual

> Preliminary research for attorney review. Not legal advice and not a license or policy decision.

## Scope and assumptions

This memo covers a U.S. federal infringement claim involving a U.S. work and expressly does not decide foreign-work exceptions, preregistration categories, registration validity, ownership, or any state-law contract limitations period. It treats each version/release and each asserted act separately.

## Short answer

Registration prerequisites and remedy eligibility are different questions. Section 411(a) generally controls when an infringement action concerning a U.S. work may be instituted; *Fourth Estate* says registration occurs when the Copyright Office registers or refuses it, not when an application is filed. *Reed Elsevier* holds that section 411(a) is nonjurisdictional. Section 412, summarized in AUTH-0006, separately can foreclose statutory damages and attorney fees even when the action may proceed. Neither provision decides whether an open-license term was breached or whether a source-performance contract claim exists.

Section 507(b)'s three years runs from claim accrual. Under *Petrella*, successive infringing acts ordinarily create separately accruing claims; ongoing distribution is not one indefinitely rolling historical claim. *Warner Chappell* rejects a separate three-year damages lookback for a claim timely under the discovery rule, but it assumed rather than decided the discovery rule's availability. A later cure or license reinstatement does not itself determine accrual for earlier conduct. State contract claims can have different accrual, tolling, notice, and limitations rules.

## Analysis

### Sequence the gates correctly

1. Identify each work, claimant, United States-work status, and registration/refusal/preregistration record.
2. Identify each allegedly infringing act and filing date; apply section 507(b) accrual doctrine.
3. Separately test section 412's timing conditions for statutory damages and fees.
4. Only then evaluate actual damages/profits, injunction, or state-law remedies.

Calling registration a prerequisite to all relief is too broad. It generally gates institution of a U.S.-work infringement action under section 411(a); section 412 concerns particular enhanced monetary remedies. Contract performance or damages do not automatically share the federal registration prerequisite, although preemption, jurisdiction, and state law may matter.

### Continuing conduct needs dates, not labels

Each new unlicensed reproduction or distribution may be a new act under the separate-accrual rule. A recipient's continued possession, a network service, a source repository, and a continuing failure to publish may raise different claim and accrual questions; none should be treated automatically as a fresh copyright infringement without mapping the relevant exclusive right and license text. The current Supreme Court record leaves the discovery-rule predicate unresolved in *Warner Chappell*.

### Registration does not cure a proof problem

Registration does not establish that code was copied, that an entire product is covered, that the claimant owns the rights at issue, or that license permission ended. Conversely, lack of timely registration may leave some remedies unavailable without deciding the merits of an alleged license breach. GPL/AGPL/LGPL/MPL terms do not override these statutory requirements for an infringement claim.

## Scenario matrix

| Scenario | Procedural/remedy consequence | Main uncertainty |
|---|---|---|
| U.S. work application pending when suit is filed | Section 411(a) ordinarily prevents institution until registration/refusal | Exceptions and exact registration record |
| Registration obtained after infringement began | Suit may proceed when §411 is satisfied | Section 412 may still bar statutory damages/fees |
| Repeated post-termination distributions | Analyze each act and its accrual date | Date/proof of each distribution and discovery rule |
| Later cure/reinstatement | May bear on future permission | Does not alone decide prior accrual or remedies |
| Recipient contract action for source | State limitations/formation law may govern | Preemption, beneficiary standing, governing law |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [17 U.S.C. §§411(a), 507(b)](../../authorities/statutes/us-copyright-registration-and-limitations.md) | Registration prerequisite and civil limitations text | Does not resolve every exception/accrual rule |
| [Copyright remedies statute](../../authorities/statutes/us-copyright-remedies.md) | Section 412 eligibility distinction and sections 502-505 remedies | No registration validity determination |
| [*Fourth Estate*](../../authorities/cases/fourth-estate-v-wall-street.md) | Registration approach under §411(a) | U.S.-work infringement action |
| [*Reed Elsevier*](../../authorities/cases/reed-elsevier-v-muchnick.md) | Section 411(a) is nonjurisdictional | Does not eliminate the prerequisite |
| [*Petrella*](../../authorities/cases/petrella-v-mgm.md) | Separate accrual and laches limits in copyright | Discovery-rule question not resolved there |
| [*Warner Chappell v. Nealy*](../../authorities/cases/warner-chappell-v-nealy.md) | No separate damages lookback for a timely discovery-rule claim | Assumes, does not decide, discovery-rule availability |

## What would change the answer

- Work nationality, registration applications/certificates/refusals, and statutory exceptions.
- Exact infringement, discovery, cure, and filing dates.
- Chosen state law and whether a contract claim supplies an extra element.
- A Supreme Court decision on the discovery-rule predicate or statutory amendment.

## Open questions for counsel

- What registrations cover the exact release and what effective/publication dates apply?
- Is a state contract claim independently viable, timely, and not preempted?
- Which discrete acts are provable within the relevant period?

## Repository implications

This research does not support language promising statutory damages or fees regardless of registration timing, or describing cure as a limitations reset.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial registration/limitations research | Agent; attorney review pending |
