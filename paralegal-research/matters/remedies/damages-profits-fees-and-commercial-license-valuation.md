---
id: PR-0013
title: Damages, profits, fees, and commercial-license valuation
question: "What monetary relief may be available for reciprocal/source-availability noncompliance, and what can a commercial-license price prove without compelling assent?"
short_answer: "For infringement, the Copyright Act permits actual damages plus attributable profits or statutory damages, and permits discretionary fees/costs; proof, apportionment, non-duplication, registration timing, and equitable discretion matter. A commercially offered license can be evidence of a hypothetical fair-market license fee or actual loss if it is sufficiently comparable, but it is not an automatically recoverable list price and does not make an alleged infringer a party to a new license. The GPL dual-license allegations in Artifex illustrate the distinction but produced no final damages award. Contract damages and fee shifting are separately governed by the claim and applicable state law."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, state-contract-law-forum-dependent]
licenses: [GPL-2.0, GPL-3.0, AGPL-3.0, LGPL-2.1, LGPL-3.0, MPL-2.0, analogous-source-availability]
actors: [copyright-owner, licensor, distributor, service-operator, customer]
conduct: [reproduce, distribute, convey, provide-network-access, post-termination-conduct]
topics: [actual-damages, profits, statutory-damages, fees, apportionment, commercial-license-valuation]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0011, PR-0014]
supersedes: []
---

# PR-0013: Damages, profits, fees, and commercial-license valuation

> Preliminary research for attorney review. Not legal advice and not a license or policy decision.

## Scope and assumptions

This memo is a U.S. federal copyright baseline. It assumes liability, standing, and a timely claim only where expressly stated, and separately flags a state-law contract claim. It does not calculate a recovery, decide registration timing, or assume that a public license has a commercial alternative.

## Short answer

Under 17 U.S.C. sections 504-505, a prevailing copyright claimant may elect actual damages plus qualifying profits or statutory damages within the statute, and the court may award full costs and reasonable attorney fees in its discretion. A claimant must link damages to the infringement and, for profits, initially show gross revenue before the infringer proves deductible expenses and apportionment. Statutory damages and fees are unavailable for certain preregistration/prepublication timing patterns under section 412; see PR-0014.

A price for a separately offered commercial license may inform a value-of-use or hypothetical-license theory when the product, scope, territory, time, use, parties, and market evidence make it comparable. *On Davis* recognizes that a reasonable license fee can be actual-damages evidence, not a presumed windfall. *Artifex* permitted GPL/commercial-license theories to proceed but settled; it neither awarded the list price nor compelled Hancom to buy a license. The same boundary applies to GPL, AGPL, LGPL, MPL, and source-available instruments: valuation is not compelled contractual assent.

## Analysis

### The statutory choices are separate from a negotiated commercial deal

Section 504 provides alternative copyright monetary measures, and section 505 leaves fees discretionary. The statutory election, proof burden, registration limits, and limitation period are independent of whether the owner usually sells commercial licenses. A defendant can settle for a commercial agreement, but a damages judgment compensates an established wrong; it does not rewrite the parties' future licensing arrangement.

### Commercial price evidence needs a real comparison

*On Davis* permits a jury-facing actual-damages theory based on the fair market value of the use, while warning against speculation. Relevant record facts can include past arms-length licenses, scope of rights, duration, exclusivity, quantity, support/indemnity features, customer class, geography, version, and whether the accused use could lawfully have received that license. A public-license recipient's noncompliance does not, by itself, establish that a proprietary license's list price is the appropriate reasonable royalty.

### Artifex is pleading-stage support, not a valuation judgment

*Artifex v. Hancom* involved a GPL or commercial-license model for Ghostscript. The court allowed the pleaded claims to proceed; the later settlement means there is no final merits award setting price, profits, source performance, or forced assent. It remains useful for careful pleading, not for an automatic commercial-license damage multiplier.

### Fees, profits, and past/current conduct

*Kirtsaeng* confirms section 505's discretionary, evenhanded framework; prevailing status does not itself fix an award. Each alleged infringement has timing consequences, and the Supreme Court's current limitations decisions control which timely claims can support money relief. See [PR-0014](../registration/copyright-registration-limitations-and-accrual.md). A cured current license status may affect future restraint, but it does not set the monetary result for earlier acts.

## Scenario matrix

| Scenario | Potential measure | Principal proof/limit |
|---|---|---|
| Proven unlicensed binary distribution | Actual loss plus attributable profits, or eligible statutory damages | Causation, revenue/apportionment, registration timing |
| Dual-license product with arms-length sales | Hypothetical reasonable license fee may be evidence | Comparable scope and non-speculative market proof |
| Open license with no paid option | Conventional loss/profits proof, if any | Cannot invent a commercial price |
| Contract-only recipient claim | Contract damages/fees under chosen law | Formation, remedy clause, state law, preemption |
| Successful suit with fee request | Section 505 discretionary fees | Objective reasonableness and all relevant circumstances |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [Copyright remedies statute](../../authorities/statutes/us-copyright-remedies.md) | Sections 504-505 damages, profits, statutory damages, costs, fees | Statutory baseline; proof and eligibility remain |
| [*Artifex v. Hancom*](../../authorities/cases/artifex-v-hancom.md) | Dual-license commercial-value theory may be pleaded | Trial-level pretrial ruling; settled, no final damages |
| [*On Davis v. Gap*](../../authorities/cases/on-davis-v-gap.md) | Fair-market license fee can be actual-damages evidence | Second Circuit; fact-specific proof, not automatic price |
| [*Kirtsaeng*](../../authorities/cases/kirtsaeng-v-john-wiley-fees.md) | Section 505 fee discretion | Copyright fees case; does not award fees in this scenario |
| [BusyBox/Westinghouse](../../authorities/cases/busybox-westinghouse.md) | Monetary/ancillary relief after default | Default-only; not valuation precedent |

## What would change the answer

- Registration, publication, application/refusal, infringement, and filing dates.
- Actual license agreements, pricing history, expert method, and apportionment evidence.
- Whether the asserted claim is copyright, contract, or both, and the selected state law.
- A final merits decision in *Artifex* (none located) or an exact-license damages judgment.

## Open questions for counsel

- What noninfringing alternatives and comparable transactions are available?
- Is the claimed fee a lost sale, reasonable royalty, lost profit, or settlement position?
- Would an asserted contract remedy duplicate statutory copyright recovery?

## Repository implications

This research does not support a license term characterizing a commercial list price as automatic damages or authorizing compelled commercial assent.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial remedies-doctrine research | Agent; attorney review pending |
