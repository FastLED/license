---
id: AUTH-0150
title: Versata Software, Inc. v. Ameriprise Financial, Inc.
authority_type: case
jurisdiction: US-Western-District-of-Texas
court: United States District Court for the Western District of Texas
date: 2014-03-11
authority_status: remanded
procedural_posture: summary-judgment
precedential_weight: persuasive-trial
licenses: [GNU-GPL-v2]
topics: [preemption, third-party-beneficiary, source-disclosure, contract]
source_quality: primary
source_url: https://www.govinfo.gov/content/pkg/USCOURTS-txwd-1_14-cv-00012/pdf/USCOURTS-txwd-1_14-cv-00012-0.pdf
original_language: English
translation_status: not-needed
last_verified: 2026-08-25
related_matter_ids: [PR-0003]
---

# AUTH-0150: *Versata Software, Inc. v. Ameriprise Financial, Inc.*

## Citation and source

- No. 1:14-cv-00012-SS, Doc. 28 (W.D. Tex. Mar. 11, 2014), [official GovInfo PDF](https://www.govinfo.gov/content/pkg/USCOURTS-txwd-1_14-cv-00012/pdf/USCOURTS-txwd-1_14-cv-00012-0.pdf).
- The order remanded the action to the 53rd Judicial District Court of Travis County. A later state-court merits disposition was not located in this audit.
- Original language: English; no translation is needed.

## Procedural posture and weight

Cross-motions for summary judgment on Copyright Act preemption in a removed
state-contract action. This is a reasoned federal trial-court ruling, persuasive
only, and its GPL discussion does not decide an underlying GPL breach.

## Claims and requested relief

Versata sued Ameriprise under a master licence for post-termination use/return
of Versata's DCM software. Ameriprise counterclaimed that Versata's alleged use
of XimpleWare VTD-XML under the GNU GPL required DCM derivative-work source
to be made available to users. The order identifies a GPL contract theory and
the parties' preemption motions; it does not supply a complete prayer for the
counterclaim or a final request for source delivery. Ameriprise was not alleged
to own XimpleWare's copyright.

## Holdings and relief actually awarded

- The court granted Ameriprise summary judgment that Versata's own
  post-termination return/use claim was preempted.
- It denied Versata's summary-judgment motion: on the pleaded theory,
  Ameriprise's GPL-source counterclaim was **not** preempted. The asserted
  failure to disclose derivative-work source was an additional contractual
  element, not merely reproduction or distribution.
- The court expressly did **not** decide whether Ameriprise had third-party-
  beneficiary standing to enforce the GPL, whether the GPL was breached, what
  DCM code was covered, or whether source had to be delivered. It remanded for
  lack of a remaining federal jurisdictional basis; it awarded no source,
  damages, or injunction relief on the GPL counterclaim.

## What it supports

- A carefully pleaded state-law claim seeking performance of a GPL-related
  source obligation may survive Copyright Act preemption under this court's
  extra-element analysis.
- Preemption and entitlement are distinct: survival of the state claim leaves
  standing, formation, scope, breach, and remedy for later adjudication.

## What it does not establish

- That every GPL source term is a covenant or is never preempted.
- A downstream customer's third-party-beneficiary standing, a derivative-work
  finding, or a court-ordered source release.
- A binding Fifth Circuit rule or the final result of the remanded dispute.

## Key facts and reasoning

The order described the counterclaim as arising after Ameriprise alleged that
Versata had incorporated GPL-covered VTD-XML in DCM. Applying the Fifth
Circuit's two-part preemption analysis, the court treated the alleged affirmative
source-disclosure promise as qualitatively different from the Copyright Act's
exclusive rights. That characterization was for the pleaded claim and did not
resolve the parties' disputed factual premise.

## Treatment in this repository

- Related matter: [PR-0003](../../matters/case-census/us-open-source-license-enforcement-census.md).
- Related litigation: [XimpleWare TRO](ximpleware-v-versata-tro.md) and the
  [later customer dismissal](ximpleware-v-versata-later-dismissal.md).
- Recheck trigger: authenticated Travis County disposition, appellate review,
  or use of the order outside its pleaded-contract/preemption question.
