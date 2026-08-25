---
id: PR-0004
title: International open-source-license enforcement census
question: "What publicly accessible non-U.S. court decisions address enforcement, scope, or consequences of reciprocal/open-source licence terms?"
short_answer: "This bounded 2026-08-25 census finds reported decisions in the CJEU, France, Germany, Italy, the Netherlands, China, and South Korea. They show that outcomes turn on the forum, exact licence text, ownership, proof, and posture: several courts treated noncompliant distribution as unlicensed/infringing or ordered compliance, while other decisions rejected claims or reserved the GPL question. No item establishes an automatic worldwide right to public source release."
research_status: partial
legal_review: pending
jurisdictions:
  - European-Union
  - France
  - Germany
  - Italy
  - Netherlands
  - China
  - South-Korea
licenses:
  - GNU GPL versions 2 and 3
  - Jelurida Public License 1.1
  - BSD-style public licenses
actors:
  - copyright-owner
  - contributor
  - licensor
  - licensee
  - distributor
  - recipient
conduct:
  - modify
  - distribute
  - omit-notice
  - withhold-source
  - continue-after-termination
topics:
  - comparative-enforcement
  - GPL
  - open-source-licenses
  - source-disclosure
  - remedies
confidence: low
last_verified: 2026-08-25
github_issues:
  - https://github.com/FastLED/license/issues/17
related_matter_ids:
  - PR-0001
supersedes: []
---

# PR-0004: International open-source-license enforcement census

> Preliminary research for attorney review. Not legal advice and not a licence,
> enforcement, or policy decision.

## Scope and assumptions

Actor: a copyright owner, contributor, licensee, or downstream distributor.
Trigger: distribution, modification, proprietary relicensing, or a GPL-based
defence. Jurisdictions searched were the EU/CJEU, France, Germany, Italy,
Spain, Netherlands, United Kingdom, China, and South Korea. The review covers
publicly accessible primary decisions or official court case summaries as of
2026-08-25, not every docket, private settlement, or administrative dispute.
It records GPLv2/v3 and the Jelurida Public License (JPL); it does not decide
the effect of any repository licence, including the FastLED draft.

Original-language materials control. Each linked card identifies its language,
official translation if one exists, and whether its English account is the
researcher's limited paraphrase. Proper certified translation and local-counsel
review are required before relying on a non-English text in advice or filing.

## Short answer

The strongest cross-border authorities are the CJEU's binding interpretation in
[*IT Development*](../../authorities/cases/it-development-v-free-mobile.md),
the French remand appellate decision in
[*Entr'Ouvert v Orange*](../../authorities/cases/entrouvert-v-orange-paris-2024.md),
and the Dutch appellate compliance order in
[*Jelurida v Apollo*](../../authorities/cases/jelurida-v-apollo.md). They do
not create a universal source-publication remedy. The CJEU left national
classification and remedies to the national court; the French appeal awarded
damages for a particular GPLv2 distribution; and the Dutch interlocutory case
ordered performance of named JPL clauses within the EU, backed by a penalty.

German trial decisions are useful but mostly non-binding and their public
copies are uneven. They support the proposition that GPL terms can be effective
and that a distributor cannot simply invoke a supplier, while *Hellwig* shows a
GPL claim can fail on proof/standing without a ruling on derivative-work scope.
Official Chinese decisions show both a GPLv3 termination/infringement result
and a refusal to decide an absent upstream owner's GPLv2 dispute. The Korean
Supreme Court decision is a trade-secret decision: it expressly leaves a
possible GPL breach claim to the original owner and does **not** compel source
release.

## Scenario matrix

| Scenario | Located authority | Actual result | Principal limit |
|---|---|---|---|
| Licencee modifies software contrary to a licence limitation | [*IT Development*](../../authorities/cases/it-development-v-free-mobile.md) | CJEU says national law may permit copyright action where a Directive 2009/24 Article 4(2) limitation is infringed | Preliminary ruling; no damages/injunction awarded by CJEU |
| GPLv2 component distributed in proprietary government platform | [*Entr'Ouvert* Paris 2024](../../authorities/cases/entrouvert-v-orange-paris-2024.md) | Infringement and damages on record-specific proof | French law and facts; no affirmative source-publication award identified |
| Distributor omits GPL source | [Fantec](../../authorities/cases/welte-v-fantec.md) | Contractual penalty, information, and costs reported | Regional-court judgment; public official copy not located |
| Licensee distributes JPL-covered software without compliance | [*Jelurida*](../../authorities/cases/jelurida-v-apollo.md) | Named JPL obligations ordered within EU, with Dutch penalty mechanism | Interlocutory relief and a non-GPL licence |
| Defendant invokes GPL against developer's later proprietary claim | [OfficeTen](../../authorities/cases/china-officeten-gplv2.md) | Defence rejected; prior developer's GPL breach reserved | Not GPL enforcement by OpenWRT owner |
| GPL developer seeks source for alleged combined work | [*Hellwig*](../../authorities/cases/hellwig-v-vmware.md) | Claim dismissed for insufficient proof | No merits holding on linking/derivative work |
| Open-source BSD redistribution and asserted upstream GPL consequence | [*Gestionale Open* Milan 2025](../../authorities/cases/gestionale-open-milan-2025.md) | Appellate court confirmed BSD-condition infringement and treated GPL/MySQL issue as separate | Full text is a legal-database reproduction; GPL was not the owner-enforced claim |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [*IT Development v Free Mobile*](../../authorities/cases/it-development-v-free-mobile.md) | EU software-licence limitation can support copyright action under national law | Binding CJEU interpretation; remand result not supplied by the CJEU judgment |
| [*Entr'Ouvert v Orange*, TGI 2019](../../authorities/cases/entrouvert-v-orange-tgi-2019.md) | First-instance contractual-characterization dispute | Superseded in material part by Cassation/remand history |
| [*Entr'Ouvert v Orange*, Cassation 2022](../../authorities/cases/entrouvert-v-orange-cassation-2022.md) | Copyright action's admissibility after GPL breach | Partial quashing/remand, not final infringement merits |
| [*Entr'Ouvert v Orange*, Paris 2024](../../authorities/cases/entrouvert-v-orange-paris-2024.md) | GPLv2 noncompliance found to infringe; damages | French appellate decision; no later official Cassation disposition located in the 2026-08-25 audit |
| [*Sitecom*](../../authorities/cases/sitecom-v-welte.md), [*D-Link*](../../authorities/cases/welte-v-d-link.md), [*Skype*](../../authorities/cases/welte-v-skype.md) | German GPL validity/licence-loss line | Trial-court decisions; public copies are non-official reproductions or archives |
| [*AVM v Cybits*](../../authorities/cases/avm-v-cybits.md) | GPL components limited AVM's copyright claim against firmware modification | Original judgment PDF; not a GPL owner enforcing against a distributor |
| [*Welte v Fantec*](../../authorities/cases/welte-v-fantec.md) | Distributor responsibility for GPLv2 source compliance | Public primary copy not independently retrieved |
| [*Hellwig v VMware*](../../authorities/cases/hellwig-v-vmware.md) | Ownership/proof can dispose of GPL action before scope | Final reported appellate disposition; no derivative-work holding |
| [*Jelurida v Apollo*](../../authorities/cases/jelurida-v-apollo.md) | Compliance order under a public source licence | Dutch interim proceedings; JPL, not GPL |
| [China OfficeTen](../../authorities/cases/china-officeten-gplv2.md), [China Virtual App](../../authorities/cases/china-virtual-app-gplv3.md) | GPL appears respectively as a limited defence and as termination condition | Official case summaries; anonymisation limits party/detail verification |
| [Korean Supreme Court 2006Do8369](../../authorities/cases/korea-gpl-trade-secret-2009.md) | GPL breach does not by itself eliminate copyright in an independently creative derivative | Criminal/trade-secret posture, not GPL enforcement remedy |
| [*Gestionale Open* Milan 2025](../../authorities/cases/gestionale-open-milan-2025.md) | BSD condition enforcement; upstream GPL argument did not itself establish downstream free-use rights | Italian appellate merits judgment; full text is not court-hosted and the GPL issue is limited |

## Search coverage and negative results

The accompanying [search log](../../search-logs/international-case-census-2026-08-25.md) and the [gap-audit log](../../search-logs/case-gap-audit-2026-08-25.md) record repositories, terms, and exclusions. The gap audit located a public full-text legal-database reproduction of a 2025 Milan appellate decision and added it with a source-host and GPL-scope limitation. Searches of Spain and UK official/free repositories did not yield a sufficiently accessible, authenticated reciprocal-licence merits decision for an authority card. This is a negative-search record, not a claim that those jurisdictions have no relevant law.

## What would change the answer

- A final appeal, cassation, settlement, or enforcement order in a listed matter.
- An official full text replacing a non-official German reproduction or court summary.
- Certified translation differing from the limited English paraphrase.
- A decision applying the precise licence version, conduct, and remedy at issue.

## Open questions for counsel

- Which target jurisdictions and language translations merit a docket-level audit?
- Does the intended claim sound in copyright, contract, consumer/competition law,
  or a mixed theory under the selected forum's conflicts rules?
- What ownership and contribution evidence supports standing for each component?
- Is an affirmative compliance order available under the selected forum's
  procedural/equitable rules, as distinct from a prohibition or damages award?

## Repository implications

This comparative census does not recommend a licence, enforcement action, or
change to `LICENSE`. Any drafting or enforcement decision remains subject to
the attorney-review gate in `LEGAL-REVIEW.md`.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial bounded international case census for issue #17 | Agent; attorney review pending |
| 2026-08-25 | Gap audit: added Milan 2025 public-license appellate decision; rechecked *Entr'Ouvert* official history | Agent; attorney review pending |
