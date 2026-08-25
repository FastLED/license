---
id: PR-0003
title: United States reciprocal and public-license enforcement census
question: "What U.S. judicial decisions, docket rulings, and disclosed settlements materially address enforcement or defenses under GPL-family and comparable public licenses?"
short_answer: "The reported U.S. record is narrow. Jacobsen, XimpleWare, Neo4j, and Fisher contain useful rulings on particular public-license questions; many BusyBox and FSF matters ended in settlement or default, and thus do not establish a general remedy rule. No located U.S. final merits judgment establishes automatic source publication or compelled purchase of a commercial license."
research_status: partial
legal_review: pending
jurisdictions:
  - US-federal
licenses:
  - GNU GPL versions 2 and 3
  - GNU AGPL version 3
  - Artistic License
  - Sweden Software License
  - Creative Commons BY-SA and BY-NC-SA
actors:
  - copyright-owner
  - licensor
  - distributor
  - modifier
  - recipient
  - customer
  - association
conduct:
  - modify
  - distribute
  - omit-notice
  - withhold-source
  - continue-after-termination
topics:
  - GPL
  - LGPL
  - AGPL
  - public-license
  - enforcement-census
confidence: medium
last_verified: 2026-08-25
github_issues:
  - https://github.com/FastLED/license/issues/17
related_matter_ids:
  - PR-0001
supersedes: []
---

# PR-0003: United States reciprocal and public-license enforcement census

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: a copyright owner, alleged downstream distributor, licensee, or public-license user. Trigger: alleged distribution, modification, licensing, removal of notices, or attempted use of a public-license defense. Jurisdiction: U.S. federal courts; state-law contract questions are noted but not synthesized. Remedy: claims and disposition, not a recommendation. The census covers GPL, GPLv2, GPLv3, AGPL-related factual settings, and comparable Creative Commons public licenses found in the documented search. It excludes non-U.S. authorities and nonjudicial compliance demands unless a disclosed settlement makes them useful context.

## Short answer

The U.S. decisions do not supply one universal "open-source enforcement" rule. *Jacobsen* is the leading appellate condition-of-license authority but arose under the Artistic License; on remand, a 2009 summary-judgment order and a 2010 dismissal did not produce a public source-performance award. *XimpleWare* accepted, at pleading stage, that alleged GPLv2 source-code distribution could make use unlicensed, while limiting claims against customers. A related *Versata v. Ameriprise* order held only that a pleaded GPL-source contract theory was not preempted, then remanded without deciding third-party-beneficiary standing or source relief. *Neo4j* produced a fact-specific permanent injunction and a nonprecedential Ninth Circuit affirmance concerning a proprietary Sweden Software License and false advertising, not a GPL/AGPL ruling. *Fisher* denied summary judgment because GPLv3 coverage, conveyance, and cure created triable factual questions. *Wallace* rejected an antitrust attack on GPL licensing, not an infringement claim.

BusyBox, FSF/Cisco, and similar matters show requested and negotiated compliance structures. They are settlements or, for Westinghouse, a default judgment; they do not prove that a contested court will order public source disclosure. The disclosed record searched did not locate a final U.S. merits judgment awarding an AGPL §13 network-source remedy or compelling either party to enter a paid commercial license.

## Census and status

| Group | Authority | License/version | Disposition and usable proposition |
|---|---|---|---|
| Public-license conditions | [Planetary Motion](../../authorities/cases/planetary-motion-v-techsplosion.md); [Jacobsen](../../authorities/cases/jacobsen-v-katzer.md) | GPL mentioned; Artistic License | *Planetary Motion* is trademark priority, not GPL enforcement. *Jacobsen* holds only its stated license terms can be copyright conditions. |
| Antitrust challenge | [Wallace/FSF](../../authorities/cases/wallace-v-free-software-foundation.md); [Wallace/IBM](../../authorities/cases/wallace-v-ibm.md) | GPL | Rule 12 dismissals/affirmance; not infringement or remedy rulings. |
| GPLv2 source/distribution | [XimpleWare TRO](../../authorities/cases/ximpleware-v-versata-tro.md); [customer MTD](../../authorities/cases/ximpleware-v-versata-customer-dismissal.md); [later MTD](../../authorities/cases/ximpleware-v-versata-later-dismissal.md) | GPLv2 | Interim or pleading-stage rulings; no final source-publication award identified. |
| GPL source-performance/preemption theory | [*Versata v. Ameriprise*](../../authorities/cases/versata-v-ameriprise-gpl-preemption.md) | GPLv2 as pleaded | State contract theory survived this trial court's preemption analysis; standing, breach, scope, and relief were not decided. |
| GPL covered-work/cure at interim stage | [*Progress v. MySQL*](../../authorities/cases/progress-software-v-mysql.md) | GNU GPL (paragraph 2 in order) | GPL preliminary injunction denied amid factual derivative-work/cure and irreparable-harm disputes; separate trademark injunction does not establish GPL relief. |
| Jacobsen later history | [post-remand order and dismissal](../../authorities/cases/jacobsen-v-katzer-post-remand.md) | Artistic License | The appellate condition decision did not culminate in a public final source-performance or damages award. |
| Neo4j license dispute | [district liability ruling](../../authorities/cases/neo4j-v-purethink-liability-ruling.md); [summary judgment](../../authorities/cases/neo4j-v-purethink-summary-judgment.md); [Ninth Circuit](../../authorities/cases/neo4j-v-purethink-ninth-circuit.md); [Graph Foundation](../../authorities/cases/neo4j-v-graph-foundation.md) | Sweden Software License; AGPL used in alleged replacement | Injunction/affirmance are fact- and license-specific; Graph Foundation action settled. |
| GPLv3 defense | [Fisher pleadings ruling](../../authorities/cases/fisher-v-sas-automation-pleading-ruling.md); [summary judgment](../../authorities/cases/fisher-v-sas-automation-summary-judgment.md) | GPLv3 | Court left coverage, conveyance, and cure issues for factfinder. |
| Contract/standing background | [KBS/Dijk](../../authorities/cases/knowledge-based-solutions-v-dijk.md) | no public license shown | Not an open-source case; excluded from substantive GPL propositions. |
| Settlements/defaults | [FSF/Cisco](../../authorities/cases/fsf-v-cisco.md); [BusyBox/Monsoon](../../authorities/cases/busybox-monsoon-settlement.md); [BusyBox/Xterasys](../../authorities/cases/busybox-xterasys.md); [High-Gain](../../authorities/cases/busybox-high-gain.md); [Verizon](../../authorities/cases/busybox-verizon.md); [Westinghouse](../../authorities/cases/busybox-westinghouse.md) | GPLv2 and GPL components | Requested or negotiated outcomes, and one default, are not contested precedential holdings. |
| Comparable public licenses | [Great Minds](../../authorities/cases/great-minds-v-fedex.md); [Drauglis](../../authorities/cases/drauglis-v-kappa-map.md) | CC BY-NC-SA 3.0; CC BY-SA 2.0 | Published construction of specific CC terms; useful only by analogy. |

## Analysis

### Claims and actual relief must stay distinct

Complaints in the BusyBox and Cisco matters sought infringement remedies and compliance-related relief. The publicly reported resolutions included source availability, notices, compliance personnel, payments, or dismissal. Those are negotiated terms (or, for Westinghouse, default relief) rather than holdings after a contested merits trial. The cards record the source and the distinction.

### The most useful adjudicated GPL-specific points are limited

The two *XimpleWare* rulings recognized that the pleaded form of GPLv2 distribution could amount to breach sufficient to render use unlicensed, but rejected the premise that distribution by one customer necessarily made every customer liable. *Versata v. Ameriprise* separately treats the alleged affirmative source promise as an extra element for preemption purposes, not as a decision that an interested customer may enforce the GPL or obtain the source. *Progress v. MySQL* denied interim GPL relief while derivative-work and cure facts were disputed. *Fisher* did not decide that GPLv3 authorized defendants; it denied summary judgment because a jury could find the software was a covered work, it was conveyed, and curative action began in time. These are district-court rulings, persuasive only.

### License and conduct differences matter

*Neo4j* concerned a Sweden Software License and representations about ONgDB; it should not be cited as an AGPL source-disclosure decision merely because the alleged replacement used AGPL text. *Planetary Motion* distributed code under GPL, but its published holding was about trademark priority. *KBS v. Dijk* concerns proprietary software and personal jurisdiction; it is logged as a negative relevance check, not evidence about open-source licensing.

## Authorities

Every authority used is linked in the table above. The underlying docket documents, official court PDF where located, and searches are recorded in the [search log](../../search-logs/us-case-census-2026-08-25.md). Existing cards AUTH-0001 through AUTH-0008 are reused rather than duplicated.

## What would change the answer

- A final merits judgment in the cited pending/settled dockets, or a later appellate ruling.
- An authenticated docket entry or unsealed settlement that alters the stated disposition.
- A decision applying the exact license version, source obligation, and distribution/network conduct in issue.

### Later-history check: *SFC v. Vizio*

The official court minute order available through SFC's docket collection denied
Vizio's first summary-judgment/adjudication motion on 2023-12-29. SFC's current
docket page, last updated 2026-02-27, describes the state action as ongoing and
lists later 2025 summary-adjudication materials; a final merits or source-delivery
order was not located in this pass. The current case page is a party-hosted docket
collection, so it confirms the stated litigation status but does not turn party
descriptions of later rulings into a general holding. See [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) and the [search log](../../search-logs/case-gap-audit-2026-08-25.md).

## Open questions for counsel

- Which forums and license versions matter for a future project-specific matter?
- Whether any historical private settlement should be collected through PACER or counsel rather than relied on from public announcements.
- Whether the unreported end-of-case status in *Fisher*, *XimpleWare*, High-Gain, or Verizon needs a PACER docket audit.

## Repository implications

This census does not support a change to `LICENSE` or an enforcement decision. It identifies source material for later, forum- and clause-specific attorney review.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial U.S. census and authority map | Agent; attorney review pending |
| 2026-08-25 | Gap audit: added *Versata/Ameriprise*, *Progress/MySQL*, and *Jacobsen* post-remand routing; rechecked *SFC/Vizio* status | Agent; attorney review pending |
