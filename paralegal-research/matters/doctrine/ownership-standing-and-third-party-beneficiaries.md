---
id: PR-0008
title: Ownership, standing, assignments, contributors, and beneficiaries
question: "Who can enforce public-license rights: copyright owners, assignees, contributors, stewards, and downstream recipients?"
short_answer: "For U.S. infringement, the plaintiff generally must be the legal or beneficial owner of the particular exclusive right allegedly infringed when suit is filed; ownership, work-for-hire, assignment, and exclusive-license proof are component and time specific. A nonexclusive license or bare accrued-claim assignment ordinarily does not suffice in the Ninth Circuit. A downstream recipient may attempt a state-law third-party-beneficiary theory, but the pending Vizio litigation supplies no final rule and does not turn a recipient into a copyright owner."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, US-Ninth-Circuit, California, European-Union]
licenses: [GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, source-available]
actors: [copyright-owner, contributor, steward, exclusive-licensee, distributor, recipient, association]
conduct: [reproduce, modify, distribute, convey, withhold-source]
topics: [ownership, assignments, standing, third-party-beneficiary]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0005, PR-0007, PR-0009]
supersedes: []
---

# PR-0008: Ownership, standing, assignments, contributors, and beneficiaries

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: author/contributor, employer, assignee, exclusive or nonexclusive
licensee, project steward, association, distributor, or downstream recipient.
Trigger: seeking infringement, contract, source-performance, or declaratory
relief. This is a U.S. baseline with limited comparative caution; it does not
audit contribution agreements, registrations, work-for-hire status, corporate
authority, or foreign collective-rights rules.

## Short answer

Sections 201, 204, and 501 provide the U.S. baseline
([AUTH-0071](../../authorities/statutes/us-copyright-ownership-transfers-standing.md)).
*DRK Photo* holds in the Ninth Circuit that a party holding only a bare
assignment of accrued infringement claims, without an exclusive §106 right,
lacks §501(b) standing. *Effects Associates* distinguishes a nonexclusive
license from a transfer of ownership. Thus a project steward, compliance
organization, or contributor must prove its own authority for the particular
component and claim; public-license text cannot cure a missing chain of title.

A downstream recipient's requested source can be a state-law beneficiary claim
rather than infringement. *SFC v. Vizio* is pending and should be described
only as a pleaded/ongoing theory. It is not authority that every GPL recipient
is an intended beneficiary, can compel performance, or may sue for copyright
damages.

## Analysis

### Copyright plaintiff and right must match

Map each component to author, employer/work-for-hire evidence, assignment,
exclusive license, and effective date. Under §501(b), a legal or beneficial
owner may sue only for infringement of the right it owns. Under §204(a), a
transfer of ownership normally requires a signed writing; *Effects Associates*
confirms a nonexclusive permission can arise without that writing but is not
ownership. Under *DRK Photo*, re-labeling a claim assignment does not supply
the required exclusive right in the Ninth Circuit.

For multi-contributor code, authorship of a contribution does not automatically
establish ownership of every version, a collective work, later modification,
or patent right. Contributor grants in MPL/EPL/CDDL/EUPL operate as textually
defined licenses, not proof that an unrelated steward owns all contributions.
GPL-family and OSL/RPL text generally license rights each contributor can
grant; due diligence must test whether they could grant them.

### Claim type controls party analysis

| Claim | Plausible claimant | Missing fact that commonly defeats it |
|---|---|---|
| Copyright infringement | Owner/beneficial owner of infringed exclusive right | Chain of title, work/act/right match |
| Contract breach | Contracting party/assignee under chosen law | Formation, assignment, governing law |
| Beneficiary performance | Intended, not merely incidental, beneficiary under state law | Contract intent and state doctrine |
| License defense | User within permission's scope | Notice, version, compliance, authorization |

This distinction matters for AGPL network source, RPL deployment, and OSL
external deployment: a remote user might be the stated audience for an offer
but not necessarily the owner, contracting party, or intended beneficiary who
can sue. The source-available families can similarly identify an affected
customer without creating direct enforcement standing.

### Comparative limits

EUPL's contributor and forum/law provisions are textually material; Member
State law governs. The French and German cases in PR-0004 underscore that proof
of authorship/standing can be dispositive, especially
[*Hellwig v. VMware*](../../authorities/cases/hellwig-v-vmware.md), but they do
not establish a single cross-border contributor rule.

## Scenario matrix

| Scenario | Likely result | Main uncertainty |
|---|---|---|
| Individual contributor sues over own copied files | Potential §501 claim | Authorship, registration, scope |
| Foundation without assignment sues for all project code | May lack rights | Contributor agreements and exclusive rights |
| Recipient seeks GPL source | Contract-beneficiary theory possible | Intent, formation, preemption, remedy |
| Agent takes assignments only after infringement | Ninth Circuit standing risk | Nature/timing of exclusive-right transfer |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0071](../../authorities/statutes/us-copyright-ownership-transfers-standing.md) | Statutory ownership/transfer/standing rules | Does not resolve facts or state contract law |
| [AUTH-0076](../../authorities/cases/drk-photo-v-mcgraw-hill.md) | Bare claim assignment insufficient in Ninth Circuit | Forum/document specific |
| [AUTH-0075](../../authorities/cases/effects-associates-v-cohen.md) | Nonexclusive license is not ownership transfer | Ninth Circuit facts |
| [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) | Beneficiary theory sought | Pending; allegations only |
| [AUTH-0059](../../authorities/cases/hellwig-v-vmware.md) | Proof/standing may dispose of GPL claim | German record and source limitations |

## What would change the answer

- Contributor agreements, employment facts, signed assignments, exclusive
  licenses, registrations, entity authority, timing, and forum law.
- A final Vizio ruling or controlling authority on public-license beneficiaries.

## Open questions for counsel

- Which claimant owns which exclusive right for every component and relevant
  version?
- Is a recipient intended to have a direct performance right under governing
  contract law, and what remedy is available?

## Repository implications

No ownership assertion or enforcement authorization is made here; preserve the
attorney-review gate.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial doctrine synthesis for issue #17 | Agent; attorney review pending |
