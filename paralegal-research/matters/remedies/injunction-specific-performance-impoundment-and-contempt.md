---
id: PR-0012
title: Injunction, specific performance, impoundment, and contempt
question: "What relief can a U.S. court consider for reciprocal or source-availability noncompliance, and how do prohibitory injunctions, source performance, discovery, impoundment, and contempt differ?"
short_answer: "For proven copyright infringement, 17 U.S.C. sections 502-503 permit tailored injunctions and impoundment/disposition, subject to ordinary equitable rules. An order stopping future unlicensed copying or distribution is different from affirmative delivery or public release of source. The latter ordinarily requires a valid affirmative claim, standing, governing state law, feasibility, and equitable proof; the reviewed U.S. GPL/AGPL record does not establish a routine final public-source order. Discovery of source under confidentiality protections is evidence-gathering, not merits performance. Contempt enforces an existing clear order against bound persons; it does not supply a new source-disclosure remedy."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, state-contract-law-forum-dependent]
licenses: [GPL-2.0, GPL-3.0, AGPL-3.0, LGPL-2.1, LGPL-3.0, MPL-2.0, analogous-source-availability]
actors: [copyright-owner, beneficiary, distributor, service-operator, recipient]
conduct: [reproduce, distribute, convey, provide-network-access, withhold-source]
topics: [prohibitory-injunction, mandatory-injunction, specific-performance, source-disclosure, impoundment, discovery, contempt]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0011, PR-0013]
supersedes: []
---

# PR-0012: Injunction, specific performance, impoundment, and contempt

> Preliminary research for attorney review. Not legal advice and not a license or policy decision.

## Scope and assumptions

This memo assumes U.S. federal copyright jurisdiction and flags an independent state contract/specific-performance theory. It covers GPL/AGPL/LGPL/MPL and analogous source-availability disputes only at the license-agnostic level. It does not determine coverage, ownership, registration, or the enforceability of a specific project term.

## Short answer

Copyright relief can prohibit future unlicensed acts within the owner's exclusive rights. Under *eBay*, a permanent injunction is not automatic; the traditional equitable factors apply. A preliminary injunction also requires the *Winter* showing. Section 503 permits impoundment and disposition of infringing articles, not a generalized takeover of a defendant's development environment.

An order to disclose, publish, or deliver source is affirmative performance. It is not interchangeable with an order to stop distributing an unlicensed binary. It may be sought on a contract/beneficiary/specific-performance theory, but *SFC v. Vizio* is procedural and does not establish a final source-production award. Source review in discovery can be protected under Rule 26(c), and should not be described as a public source-release judgment. Rule 65(d) identifies who may be bound by an injunction; Rule 70 supplies mechanisms after a judgment requires a specific act. Contempt is post-order enforcement, not an initial remedy.

## Analysis

### Prohibitory injunction: stop conduct, do not create a license

The baseline order prohibits proven future infringement such as copying, modification, or distribution without permission. A defendant's practical option to comply with an available public license, stop, or negotiate separate permission does not mean the court compelled either side to enter a new commercial contract. *Jacobsen* supports that license conditions can delimit permission; it does not award source publication. *eBay* rejects categorical injunction rules, so infringement and a source-availability license alone do not dispense with equitable proof.

### Affirmative source performance is a distinct remedy

Specific performance depends on the plaintiff's claim and standing, the precise promise, adequacy of damages, feasibility/supervision, defenses, and selected state law. A public release can have effects beyond litigants and may expose unrelated confidential material; a narrow delivery to a defined beneficiary is not the same order. In *SFC v. Vizio*, a beneficiary asserted source-related performance, but the cited procedural record contains no final merits or actual source-disclosure award. Settlements and requests in BusyBox matters likewise cannot be relabeled awarded relief.

### Confidential discovery is not compliance performance

Source code relevant to coverage, copying, provenance, or damages may be discoverable. Rule 26(c) permits good-cause protections for trade secrets and confidential commercial information. Such production is ordinarily to parties/experts on specified terms and does not establish that public recipients are entitled to the material or that the defendant has complied with a license. Court-specific local rules and sealing standards remain material. See [AUTH-0111](../../authorities/statutes/us-federal-discovery-and-protective-orders.md).

### Impoundment, order specificity, and contempt

Section 503 and [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md) govern impoundment/disposition in copyright cases. Rule 65(d) requires an order to state its terms specifically and identifies persons bound; Rule 70 governs enforcement of a judgment for a specific act. A contempt motion thus asks whether an existing, clear, valid order was violated by a bound person. It cannot remedy ambiguity by retrospectively adding publication, commercial licensing, or nonparty obligations.

## Scenario matrix

| Scenario | Relief potentially considered | What it is not |
|---|---|---|
| Proven unlicensed GPL distribution | Tailored prohibitory injunction; statutory relief where eligible | An order forcing a commercial license |
| Claim for source to identified recipients | State-law specific performance or mandatory injunction if elements are met | An automatic consequence of every copyleft breach |
| Code needed to test covered-work claim | Confidential discovery/protective order | Public disclosure or final compliance finding |
| Infringing devices/media | Section 503 impoundment/disposition on the statutory record | A blanket order for all source repositories |
| Violation after injunction/consent decree | Contempt/enforcement of the actual order | A new merits remedy against nonparties |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [Copyright remedies statute](../../authorities/statutes/us-copyright-remedies.md) | Sections 502-503 injunction/impoundment baseline | Does not create contract performance |
| [*eBay v. MercExchange*](../../authorities/cases/ebay-v-mercexchange.md) | Traditional factors for permanent injunction | Patent case; general equitable rule, not source-license-specific |
| [*Winter*](../../authorities/cases/winter-v-nrdc.md) | Preliminary-injunction standard | Environmental case; not a source-license merits holding |
| [Federal Rules 26/37](../../authorities/statutes/us-federal-discovery-and-protective-orders.md) | Protected source discovery is distinct from publication | Procedure; does not establish underlying entitlement |
| [Federal Rules 65(d)/70](../../authorities/statutes/federal-rules-discovery-injunction-performance.md) | Order specificity and specific-act enforcement | Procedure; does not establish underlying entitlement |
| [*SFC v. Vizio*](../../authorities/cases/sfc-v-vizio.md) | Beneficiary/source-performance theory is being litigated | Pending/procedural; no final award |
| [BusyBox/Westinghouse](../../authorities/cases/busybox-westinghouse.md) | GPL default judgment included permanent injunctive/ancillary relief | Default-only, distribution facts, not general precedent |
| [*XimpleWare* TRO](../../authorities/cases/ximpleware-v-versata-tro.md) | Requested emergency source-related relief can be denied | Interlocutory; no merits decision |

## What would change the answer

- The governing state law, contract formation and beneficiary facts.
- A finalized source-performance judgment in *SFC v. Vizio* or comparable case.
- Evidence concerning irreparable harm, balance of hardships, public interest, feasibility, and precise code scope.
- The text of any already-entered injunction, consent decree, or protective order.

## Open questions for counsel

- Should requested source relief be framed as delivery, publication, or discovery, and to whom?
- Can the requested order be drafted with Rule 65 specificity and without requiring ongoing judicial supervision?
- What confidential components, third-party rights, and export/security constraints affect feasibility?

## Repository implications

This memo does not support drafting a provision that promises automatic public source production, compulsory commercial assent, or contempt before an order exists.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial remedies-doctrine research | Agent; attorney review pending |
