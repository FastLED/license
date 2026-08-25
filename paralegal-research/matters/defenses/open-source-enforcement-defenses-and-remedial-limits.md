---
id: PR-0015
title: Open-source enforcement defenses and remedial limits
question: "What defenses and remedial limits may affect enforcement of GPL-, AGPL-, LGPL-, MPL-, or analogous source-availability terms?"
short_answer: "Authorization is foundational: a valid public license can defeat infringement within its scope, while the claimant must prove termination or an exceeded condition. Waiver, estoppel, unclean hands, and impossibility are fact- and forum-dependent equitable or contract doctrines, not automatic consequences of public licensing or delayed enforcement. Copyright misuse is a narrow, fact-specific defense against leveraging copyright beyond its lawful scope. Later compliance does not automatically moot a damages claim, and voluntary cessation ordinarily bears a heavy burden to moot prospective relief. License warranty/liability disclaimers allocate private warranty and damages risk only to the extent enforceable; they do not themselves erase statutory infringement remedies, registration limits, or court authority."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, state-contract-law-forum-dependent]
licenses: [GPL-2.0, GPL-3.0, AGPL-3.0, LGPL-2.1, LGPL-3.0, MPL-2.0, analogous-source-availability]
actors: [copyright-owner, licensor, contributor, distributor, modifier, service-operator, recipient]
conduct: [reproduce, distribute, convey, provide-network-access, cure, continue-after-termination]
topics: [authorization, waiver, estoppel, misuse, unclean-hands, impossibility, mootness, voluntary-cessation, disclaimers]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0011, PR-0012, PR-0014]
supersedes: []
---

# PR-0015: Open-source enforcement defenses and remedial limits

> Preliminary research for attorney review. Not legal advice and not a license or policy decision.

## Scope and assumptions

This is a license-agnostic U.S. federal baseline with explicit state-law limits. It identifies possible defenses and limits; it does not conclude that any defense applies to a repository, contributor, product, or license. Ownership, scope, condition/covenant classification, registration, and the remedy sought must be separately established.

## Short answer

The first defense is often authorization: a defendant that acted within a valid nonexclusive public license may not have infringed. The claimant then must prove a condition limiting permission, a breach, termination, and the relevant unlicensed act. *Jacobsen* and *MDY* guide that inquiry in their stated jurisdictions; *Effects Associates* illustrates that nonexclusive permission may be express or implied from conduct, but its fact pattern is not an open-source rule.

Waiver and estoppel require a forum-specific record (conduct, knowledge, reliance, and prejudice as applicable); delay alone is not a universal release. Copyright misuse is not a generalized objection to reciprocal terms: *Practice Management* addresses a particular copyright holder's leveraging arrangement. Unclean hands and impossibility are equitable/contract defenses whose elements and consequences follow the chosen law. Cure may bear on future permission and prospective relief, but voluntary cessation ordinarily does not itself moot a live dispute, especially a damages claim. Warranty/liability disclaimers in license text are not a judicial remedy bar and may be limited by applicable law.

## Analysis

### Authorization and scope come before a remedial debate

Public license text is affirmative permission within its scope. A claimant cannot treat every technical or notice defect as infringement without identifying the right exercised, the condition/covenant theory, the alleged breach, and a termination timeline. The exact version matters: GPLv3/AGPLv3/LGPLv3 reinstatement language is not GPLv2/LGPLv2.1 text, and MPL 2.0 is separately structured. An implied license analysis is not a substitute for reading the published license, but conduct can matter where a party alleges authorization outside or alongside it.

### Waiver, estoppel, unclean hands, and impossibility are not categorical open-source defenses

These doctrines vary materially by state law. Evidence can include communications, repeated acceptance of performance, notice, reliance, prejudice, claimant misconduct related to the relief, and whether a promised act is objectively or legally possible. They may limit a contract remedy or equitable relief without transferring copyright, excusing unrelated infringement, or creating a future commercial license. A short source-posting delay or public availability of code does not alone prove any of them.

### Misuse is narrow and fact-specific

*Practice Management* held that the asserted copyright was unenforceable during misuse on its record because the copyright holder conditioned a government license to exclude competing coding systems. The case does not hold that reciprocal licensing, dual licensing, commercial alternatives, or a demand for compliance is misuse. Whether a license condition unlawfully extends copyright power requires its own factual and legal analysis.

### Mootness, voluntary cessation, and remedy type

*Friends of the Earth v. Laidlaw* states the ordinary voluntary-cessation principle: a defendant's stopping challenged conduct does not ordinarily moot a case unless it is absolutely clear the conduct cannot reasonably recur. Its environmental facts are not copyright-specific. Even where prospective relief no longer has a live function, claims for completed conduct and money remedies need separate analysis. The doctrine does not turn a cure into an admission, a release, or a contempt order.

### Disclaimers

GPL-family and MPL texts contain warranty and liability disclaimers. Their effect is a construction/enforceability issue under governing law and applicable consumer, tort, statutory, and public-policy limits. They do not answer ownership, authorization, registration, statutory damages/fees eligibility, or whether a court can issue an injunction. A disclaimer cannot be treated as a prewritten waiver of an unknown litigant's statutory remedy absent a legally valid basis.

## Scenario matrix

| Defense/limit | Potential role | What it does not establish |
|---|---|---|
| Authorization / implied license | Conduct was within permission | That every later use was authorized |
| Waiver / estoppel | May limit a claim/remedy on state-law facts | Automatic loss of copyright from delay |
| Copyright misuse | May bar enforcement while misuse continues | That ordinary copyleft reciprocity is misuse |
| Unclean hands / impossibility | May affect equitable or contract relief | A universal excuse for infringement |
| Cure / voluntary cessation | May affect future permission or prospective relief | Mootness of all historical monetary claims |
| Warranty/liability disclaimer | May allocate contractual warranty/liability risk | Elimination of statutory copyright remedies |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [*Jacobsen*](../../authorities/cases/jacobsen-v-katzer.md), [*MDY*](../../authorities/cases/mdy-industries-v-blizzard.md) | Permission scope and condition/covenant analysis | Forum/text specific |
| [*Effects Associates*](../../authorities/cases/effects-associates-v-cohen.md) | Nonexclusive authorization may be implied from conduct | Ninth Circuit, non-open-source facts |
| [*Practice Management*](../../authorities/cases/practice-management-v-ama.md) | Fact-specific copyright misuse defense | Ninth Circuit, unique government-exclusivity facts |
| [*Friends of the Earth*](../../authorities/cases/friends-of-the-earth-v-laidlaw.md) | Voluntary cessation does not ordinarily moot a case | Environmental case; apply by analogy |
| [GPL-family and MPL cards](../license-comparison/copyleft-source-availability-license-landscape.md) | Version-specific termination and disclaimer language | Operative text, not enforceability holding |
| [*Fisher*](../../authorities/cases/fisher-v-sas-automation-summary-judgment.md) | Cure/termination can present factual questions | No final merits/remedy result |

## What would change the answer

- Governing law, forum, communications, notice, and reliance evidence.
- Exact license/version, claimed breach, cure history, and past/current acts.
- The remedy requested and whether a live monetary or prospective controversy remains.
- A controlling state-law decision on a pleaded waiver, estoppel, impossibility, or disclaimer issue.

## Open questions for counsel

- Which party holds which rights, and what authorization did it actually grant?
- What conduct supports each equitable defense and how does the selected state define its elements?
- Are third-party components, confidentiality, export controls, or lost-source facts relevant to impossibility?
- Do consumer/procurement rules alter any warranty/liability disclaimer?

## Repository implications

This research does not support adding a self-executing waiver of statutory rights, treating a disclaimer as immunity from enforcement, or assuming cure moots past claims.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial defenses/remedial-limits research | Agent; attorney review pending |
