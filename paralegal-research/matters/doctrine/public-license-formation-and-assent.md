---
id: PR-0005
title: Public-license formation, assent, and parties
question: "When, and between which parties, can use or distribution under a public or source-available software license form an enforceable license or contract?"
short_answer: "A public license can grant copyright permission without a negotiated bilateral contract, but a contract or beneficiary claim requires the governing jurisdiction's formation rules and evidence of offer, notice, assent, consideration where required, and party identity. Official texts vary: most GNU and file-level licenses make permissions available on stated terms; OSL expressly asks distributors to seek recipient assent; source-available terms may restrict use but do not themselves prove assent. The reported U.S. public-license cases do not establish one universal click-free formation rule."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, US-state-contract, European-Union]
licenses: [GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, source-available]
actors: [copyright-owner, contributor, steward, distributor, recipient, service-operator]
conduct: [reproduce, modify, distribute, convey, deploy, provide-network-access]
topics: [formation, assent, parties]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0002, PR-0007, PR-0008, PR-0010]
supersedes: []
---

# PR-0005: Public-license formation, assent, and parties

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: an owner/contributor offering code, an intermediary distributing it, or
a recipient/service operator relying on the offer. Trigger: copying,
modification, conveyance, deployment, or a claim for performance. This memo
addresses U.S. copyright and selected state-contract formation doctrines, with
the EUPL's selected-law structure noted; it does not select a forum, decide
consumer-law validity, or audit any repository's notices, click path, chain of
title, or release version.

## Short answer

**Holding-level baseline:** copyright permission and contract formation are
different questions. A nonexclusive license can be implied from conduct in the
Ninth Circuit ([AUTH-0075](../../authorities/cases/effects-associates-v-cohen.md));
an implied promise can be sufficiently pleaded under New York or California law
on particular facts ([AUTH-0072](../../authorities/cases/forest-park-pictures-v-universal.md),
[AUTH-0074](../../authorities/cases/montz-v-pilgrim-films.md)). Those decisions
do not decide GPL/AGPL/MPL assent.

**Inference:** distributing code with an identified public-license notice is
strong evidence of an offer of conditional copyright permission. Whether it
also creates an enforceable bilateral contract with each recipient depends on
the selected law and proof that the relevant party knew of and manifested
assent to the material terms. A recipient may have permission yet lack a
contract claim; conversely, a recipient's contract/beneficiary theory may be
available without owning an exclusive copyright right. The pending
[*SFC v. Vizio*](../../authorities/cases/sfc-v-vizio.md) illustrates, but does
not resolve, the latter theory.

## Analysis

### Formation must identify the instrument, manifestation, and parties

Start with the exact release, incorporated notices, version option, and
contributor/owner making the grant. Then map the defendant's act and what
notice preceded it. Under *Effects Associates*, conduct may support an implied
nonexclusive license, but that conclusion followed commissioning and delivery
for a known film use; it is not a rule that software access always equals
assent. Under *Forest Park* and *Montz*, particular allegations supported an
implied promise to pay, but those are state-law, pleading-stage contexts.

For a copyright claim, the relevant parties are normally the owner (or legal
or beneficial owner of the infringed exclusive right) and the alleged user.
For contract, assignment, contribution, or beneficiary claims, the contracting
promisor/promisee and governing-law rules matter separately. A license steward
is not automatically an owner or contracting party; see PR-0008.

### Textual patterns are materially different

| Pattern | Textual formation/party signal | Limit |
|---|---|---|
| GPL-2/3, LGPL-2.1/3, AGPL-3 | Permissions are offered to those exercising stated rights; GPL-3/AGPL-3 use automatic permission on receipt and GPL-2 uses copying/distribution terms | Text alone does not select contract law or establish recipient assent to a separate promise |
| MPL-2, EPL-2, CDDL-1, EUPL-1.2 | Contributor grants and defined recipient/contributor structure identify the scope of licenses; MPL states its §§3 terms are conditions | They do not make every downstream recipient a named enforcement plaintiff |
| OSL-3, RPL-1.5 | OSL §9 asks a distributor to use reasonable efforts for express recipient assent; RPL defines broad deployer obligations | An express-assent solicitation is not proof it occurred or was effective |
| SSPL-1 | GPLv3-style grant plus service condition | No reported formation holding located for the exact text |
| BUSL/ELv2/Commons Clause/FSL/PolyForm | Permission is release-specific or restricted; Commons Clause depends on the underlying license | Source availability/restriction does not itself prove an accepted commercial agreement |

The operative-text cards in [PR-0002](../license-comparison/copyleft-source-availability-license-landscape.md) are the source for those descriptions; they are license text, not judicial holdings.

### Assent evidence and jurisdiction limits

Evidence should distinguish an owner placing a notice in source, a distributor
passing it onward, a recipient actually receiving it, and a service operator
continuing after notice. Screens, package metadata, README, manifest, download
record, click-through records, invoices, and correspondence can change the
formation analysis. California and New York decisions above cannot determine
European, other U.S. state, or foreign law. EUPL Article 15 makes applicable
Member-State law and court depend on the licensor's seat/residence; its text
does not replace local formation law.

## Scenario matrix

| Scenario | Likely claim | Main uncertainty |
|---|---|---|
| Owner sues distributor for copying outside GPL condition | Copyright license/scope | Notice, ownership, and condition/nexus |
| Recipient seeks GPL source from manufacturer | Beneficiary contract/specific performance | Formation, beneficiary intent, preemption, state law |
| OSL distributor displays acceptance prompt | Contract may be stronger if assent proved | Assent mechanics, authority, and applicable law |
| Employee deploys RPL-covered code internally | Textual deployment duty may be triggered | Whether entity/employee is the licensee; enforceability and proof |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0075](../../authorities/cases/effects-associates-v-cohen.md) | Implied nonexclusive license / ownership distinction | Binding Ninth Circuit; non-software facts |
| [AUTH-0072](../../authorities/cases/forest-park-pictures-v-universal.md), [AUTH-0074](../../authorities/cases/montz-v-pilgrim-films.md) | Implied-contract pleading | State-law specific; no public license |
| [AUTH-0003](../../authorities/cases/artifex-v-hancom.md) | GPL contract/copyright theories pleaded | Trial-level, settled |
| [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) | Recipient beneficiary theory alleged | Pending; no merits holding |
| [official license cards](../../authorities/licenses/) | Exact offer/condition wording | Text only |

## What would change the answer

- The actual license notice, version, incorporation path, click/wrap record,
  communications, contributor agreement, or selected law.
- A final merits ruling in *SFC v. Vizio* or an exact-license formation case.

## Open questions for counsel

- Does a planned deployment need an affirmative acceptance record and which
  state's or Member State's law controls it?
- Which legal person owns each relevant contribution and made the offer?

## Repository implications

This research does not establish formation for this repository or support an
edit to `LICENSE`; attorney review remains required.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial doctrine synthesis for issue #17 | Agent; attorney review pending |
