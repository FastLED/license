---
id: PR-0019
title: Settlement, compliance, and post-judgment structures
question: "How should negotiated compliance structures, consent decrees, and post-judgment enforcement be distinguished from contested judicial remedies in license-agnostic software disputes?"
short_answer: "A negotiated source release, notice, audit, payment, commercial license, or compliance undertaking is a settlement term unless a court actually orders it after contested adjudication. A consent decree or stipulated injunction may be enforceable as a court order against persons bound by it, but it is still not precedent that the same relief is generally available. Post-judgment enforcement depends on the judgment's text, jurisdiction, parties bound, due process, and applicable enforcement rules; it cannot enlarge an unresolved merits remedy."
research_status: answered
legal_review: pending
jurisdictions: [US-federal, US-state]
licenses: []
actors: [copyright-owner, contributor, distributor, service-operator, recipient, defendant]
conduct: [cure, reproduce, distribute, provide-network-access, withhold-source]
topics: [settlement, consent-decree, compliance, injunction, contempt, post-judgment]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0017, PR-0018]
supersedes: []
---

# PR-0019: Settlement, compliance, and post-judgment structures

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

This memo distinguishes categories of outcome in a U.S.-focused software
dispute: voluntary settlement, court-entered consent decree/stipulated
injunction, contested merits remedy, and post-judgment enforcement. It does
not draft settlement language, a consent decree, demand, notice, or enforcement
communication. It assumes the exact license/version, claim, parties, and forum
will be identified before any remedy conclusion. Foreign recognition is treated
only in PR-0020.

## Short answer

Settlement can address matters parties choose to resolve—such as source
delivery/publication, notices, correction, audit/cooperation, payment, release,
or a separately negotiated commercial license. It establishes an agreement, not
a generally available judicial remedy. The public BusyBox/Monsoon material is
an example of reported negotiated terms and is expressly classified as a
settlement, not a holding. [AUTH-0008](../../authorities/cases/busybox-monsoon-settlement.md).

An injunction after a contested copyright case is governed by the applicable
statutory and equitable standards. Specific performance/source disclosure may
require a separate valid claim and equitable analysis; PR-0001 found no routine
final U.S. AGPL judgment compelling public source publication. A consent decree
or stipulated injunction can be enforceable through the entering court, but
only according to its valid terms and persons bound. It cannot show that the
same term would have been awarded after trial.

## Analysis

### Classify outcome before drawing a proposition

Use four labels in the matter record:

| Outcome | What it can support | What it cannot support |
|---|---|---|
| Private settlement | Parties agreed to specified obligations, if authentic/public | A judicial holding or remedy for strangers |
| Consent decree/stipulated injunction | An order's actual terms and enforcement against bound persons | A contested merits precedent or obligation beyond its terms |
| Contested judgment | The court's actual holding/remedy in its forum | Unproven requested relief or a broader license-family rule |
| Post-judgment order | Enforcement/modification of the existing judgment | A new merits theory or a larger injunction than entered |

The desired words—"source disclosure," "audit," "commercial license," or
"compliance"—do not identify a legal category. Record whether they appear in a
request, agreement, judgment, or later compliance report, and preserve the
operative document rather than relying on a press summary.

### Agreement and contested remedy are distinct

The Copyright Act's ordinary federal remedies include injunctions, impoundment/
disposition, damages/profits or statutory damages, costs, and discretionary
fees, subject to statutory and equitable limits. [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md).
The statute does not itself make a commercial license, public source release,
audit, or negotiated cure an automatic judgment term. *Artifex* supports a
pleaded commercial-license-value damages theory; it does not create a compelled
commercial agreement. [AUTH-0003](../../authorities/cases/artifex-v-hancom.md).

If a license has termination/reinstatement language, determine whether the
party's future permission was restored and separately assess any past conduct,
release, waiver, and remedy. For AGPLv3, see the exact reinstatement text in
[AUTH-0007](../../authorities/licenses/gnu-agpl-v3.md); no inference should be
exported to another license version.

### Post-judgment administration must follow the actual order

Federal Rule 69 generally uses state execution procedure for money judgments;
Rule 70 addresses enforcement of a judgment for a specific act; 28 U.S.C.
§ 1963 allows registration of qualifying federal judgments in other districts.
[Rule 69](https://www.uscourts.gov/sites/default/files/document/federal-rules-of-civil-procedure.pdf), [Rule 70](https://www.uscourts.gov/sites/default/files/document/federal-rules-of-civil-procedure.pdf), and [28 U.S.C. § 1963](https://uscode.house.gov/view.xhtml?edition=2023&num=0&req=granuleid%3AUSC-2023-title28-section1963) should be read with forum-specific law. Contempt and compliance proceedings require attention to clarity of order, notice, the person bound, and due process; they are not an occasion to recast a settlement wish as a remedy.

## Scenario matrix

| Scenario | Classification | Research consequence |
|---|---|---|
| Public announcement says source was released | Settlement/compliance report unless operative order says otherwise | Locate agreement/order; do not call it awarded relief |
| Court enters stipulated injunction | Consent decree/order | Analyze text, jurisdiction, parties bound, enforcement reservation |
| Court enjoins unlicensed distribution after merits finding | Contested remedy | Record exact conduct, conditions, duration, and appeal status |
| Party cures under license | Factual/license-text event | Assess terms and past claims separately |
| Money/property judgment in another federal district | Post-judgment registration/execution | Check § 1963, Rule 69, and judgment finality |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0008](../../authorities/cases/busybox-monsoon-settlement.md) | Publicly described negotiated compliance terms | Settlement only, nonprecedential |
| [AUTH-0004](../../authorities/cases/busybox-westinghouse.md) | Default-judgment injunction record | Default only; not contested merits |
| [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md) | Statutory copyright remedy categories | Does not grant automatic affirmative performance |
| [AUTH-0003](../../authorities/cases/artifex-v-hancom.md) | Commercial-license value theory at pleading stage | Not a compelled-license rule |
| [PR-0001](agpl-noncompliance-judicial-remedies.md) | Existing narrow U.S. remedy synthesis | AGPL-style scenario; not a cross-license rule |

## Research checklist for counsel review

- Obtain the operative settlement, decree, judgment, docket entry, and later
  order; identify redactions and whether terms are public/authenticated.
- Label every material point as requested relief, settlement term, awarded
  relief, consent-order term, or enforcement action.
- Identify persons/entities bound, order clarity, effective dates, appeal/
  modification status, jurisdiction retained, and any governing-law terms.
- Separate license-text cure/reinstatement from release of past claims and from
  a court's contempt/enforcement authority.
- For a contemplated post-judgment step, verify the selected forum's rules and
  state execution law; do not reuse this checklist as enforcement communication.

## What would change the answer

- Actual agreement/order text, court, state law, appeal status, license cure
  language, party relationships, or proposed enforcement location.

## Open questions for counsel

- Whether a particular settlement is enforceable as contract only or as a court order.
- Whether a requested affirmative obligation meets the applicable equitable standard.
- What person is bound and what compliance mechanism the exact order permits.

## Repository implications

No settlement, consent-decree, compliance program, or `LICENSE` text is
proposed. Any such instrument requires independent legal and business approval.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial research for issue #17 | Agent; attorney review pending |
