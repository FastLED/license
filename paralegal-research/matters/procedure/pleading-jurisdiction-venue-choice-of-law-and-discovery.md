---
id: PR-0017
title: Pleading, jurisdiction, venue, choice of law, and discovery
question: "How should a license-agnostic software dispute be routed through U.S. pleading, jurisdiction, venue, choice-of-law, discovery, and protective-order questions without conflating them with the merits?"
short_answer: "A viable merits theory does not by itself establish a proper U.S. court, venue, governing law, discovery entitlement, or public disclosure. Route federal copyright claims, state contract claims, personal jurisdiction, venue, transfer, contractual forum/law clauses, and requested discovery independently. Public investigation precedes and differs from discovery; source-code discovery may be limited or protected, and protected production is not public release."
research_status: answered
legal_review: pending
jurisdictions: [US-federal, US-state]
licenses: []
actors: [copyright-owner, contributor, distributor, service-operator, recipient, customer]
conduct: [reproduce, modify, distribute, provide-network-access, withhold-source]
topics: [pleading, jurisdiction, venue, choice-of-law, discovery, protective-orders]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0016, PR-0018, PR-0020]
supersedes: []
---

# PR-0017: Pleading, jurisdiction, venue, choice of law, and discovery

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

This is an issue-spotting memo for a U.S. dispute involving software and an
identified license or contract. It assumes a potential claimant is considering
federal copyright and/or state-law claims but does not assume ownership,
registration, assent, breach, direct infringement, or a valid forum clause.
It does not provide a complaint, motion, subpoena, discovery request, or legal
strategy. State conflicts law, personal jurisdiction, local rules, and the
chosen license's clauses can change every result.

## Short answer

Federal district courts have exclusive subject-matter jurisdiction over civil
claims arising under federal copyright law, while related state claims may
require an independent basis or supplemental jurisdiction. That says nothing
about personal jurisdiction over a defendant or venue. Venue statutes,
transfer statutes, controlling circuit law, and any forum-selection clause need
separate analysis. Choice of law is not decided solely by the place where a
repository is hosted, a download occurs, or a product is sold.

Federal pleading rules require a legally sufficient claim, but they do not
authorize pre-suit evidence collection. After a case begins, discovery is
subject to scope, proportionality, privilege, timing, and court control. A
protective order can govern confidential source code or business records; it
does not establish a merits remedy or public availability of the production.

## Analysis

### Route claims and jurisdiction before remedies

Identify each claimant, each copyrighted work or contract, the alleged conduct,
the date and place of each act, and the relief category. Copyright claims must
also account for the registration prerequisite for U.S. works in 17 U.S.C.
§ 411(a); [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md)
addresses related registration timing and remedies. Contract claims may involve
different parties, governing law, remedies, and preemption questions. A
recipient's request for source, for example, may rest on a distinct contract or
third-party-beneficiary theory rather than the copyright owner's infringement
claim; the pending posture of [AUTH-0005](../../authorities/cases/sfc-v-vizio.md)
does not decide that question.

Section 1338(a)'s subject-matter grant is only one gate. Personal jurisdiction
requires its own constitutional/statutory analysis; venue requires §§ 1391 and
1400(a), as applicable; §§ 1404(a), 1406(a), and 1631 concern transfer/cure in
specified circumstances. [AUTH-0110](../../authorities/statutes/us-copyright-jurisdiction-and-venue.md).

### Treat contractual clauses and conflicts separately

First establish whether the relevant text is a contract, who assented, what
version governed, and whether a clause actually reaches the claim and parties.
Then apply the selected forum's law to enforceability and conflicts questions.
Federal copyright law can govern an infringement claim even where state law
governs formation or a contract claim. A clause's existence does not itself
give a court personal jurisdiction or make venue proper; both interaction and
controlling precedent are forum-specific.

### Discovery is not an investigative license or public release

Rules 26, 34, and 45 govern party/nonparty discovery after procedural
authorization. They do not authorize entry into systems, bypass of controls,
or compelled collection before a case. Source repositories, build systems,
customer records, and communications may raise proportionality, trade-secret,
privacy, privilege, and ESI questions. A Rule 26(c) order can restrict
disclosure and use. [AUTH-0111](../../authorities/statutes/us-federal-discovery-and-protective-orders.md).

## Scenario matrix

| Scenario | Threshold sequence | Main uncertainty |
|---|---|---|
| Owner alleges unlicensed distribution | Ownership/registration, copyright claim, personal jurisdiction, venue | Condition/covenant and chain-of-title facts |
| Recipient seeks source | Standing/contract theory, state law, clause, remedy | Whether recipient has enforceable rights |
| Out-of-state manufacturer | Contacts, relevant acts, venue, party relationship | Who made/distributed the copy and where |
| Source code sought in litigation | Rules 26/34/45, proportionality, confidentiality | Need, burden, trade-secret protections |
| Public repository review | Lawful access and preservation | Whether it represents the relevant product/version |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0110](../../authorities/statutes/us-copyright-jurisdiction-and-venue.md) | Federal subject matter/venue/transfer statutory framework | Does not decide a particular forum |
| [AUTH-0111](../../authorities/statutes/us-federal-discovery-and-protective-orders.md) | Pleading/discovery/protection mechanisms | Local rules and orders matter |
| [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md) | Registration timing and remedy statutes | Not a jurisdiction or venue rule |
| [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) | Illustrates a distinct recipient/contract theory | Pending/procedural; no final right to source |

## Research checklist for counsel review

- Map each cause of action to claimant, defendant, work/contract, conduct, date,
  and requested relief; identify direct versus secondary theory.
- Verify ownership/registration facts and the exact license or contract version.
- Analyze subject-matter jurisdiction, personal jurisdiction, venue, transfer,
  removal/remand if relevant, and every forum/law clause independently.
- Obtain current local rules and judge practices before any discovery assessment.
- Distinguish public factual preservation from discovery and from protected
  production; identify privilege, privacy, and trade-secret issues.

## What would change the answer

- Selected court/state, parties' domicile and contacts, pleaded claims, actual
  clause language, registration facts, or requested discovery.

## Open questions for counsel

- Applicable state conflicts and forum-selection standards.
- Whether a recipient has standing and whether a state claim survives preemption.
- Scope and format of any ESI/source-code discovery and appropriate protection.

## Repository implications

No pleading or enforcement communication is drafted and no `LICENSE` change is
suggested. Project-specific clauses require attorney review in the target forum.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial research for issue #17 | Agent; attorney review pending |
