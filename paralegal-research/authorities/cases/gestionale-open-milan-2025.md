---
id: AUTH-0153
title: Gestionale Open litigation — Milan Court of Appeal 2025
authority_type: case
jurisdiction: Italy, Corte d'Appello di Milano
court: Corte d'Appello di Milano, Sezione specializzata in materia di impresa
date: 2025-05-06
authority_status: current-lower-court
procedural_posture: appellate-merits
precedential_weight: persuasive-published
licenses: [BSD-license, GNU-GPL]
topics: [public-license-conditions, notice, attribution, source-disclosure, scope]
source_quality: official-reproduction
source_url: https://www.doctrine.it/decisions/itcanzeudfyi14peo
original_language: Italian
translation_status: researcher-translation
last_verified: 2026-08-25
related_matter_ids: [PR-0004]
---

# AUTH-0153: *Gestionale Open* litigation — Milan Court of Appeal 2025

## Citation and source

- Corte d'Appello di Milano, Sezione specializzata in materia di impresa,
  judgment no. 1293/2025, filed 6 May 2025, appeal RG 3330/2023, affirming
  Tribunale di Milano, partial judgment no. 7112/2023 in RG 33516/2018.
  [Public full-text reproduction](https://www.doctrine.it/decisions/itcanzeudfyi14peo).
- The accessible document carries the court rubric, judgment number, filing
  date, panel, and dispositive text, but it is hosted by a legal database rather
  than an Italian court/government portal. No later *ricorso per cassazione* was
  located in this audit.
- Original language: Italian. No official English translation was located; all
  English statements in this card are limited researcher translations/paraphrases.

## Procedural posture and weight

Published Milan appellate merits judgment affirming a partial first-instance
judgment. It has persuasive comparative value only. The GPL material arises in
a defence/scope argument; the principal public licence adjudicated was a BSD
licence, not GNU GPL enforcement by a GPL copyright owner.

## Claims and requested relief

The appellees alleged unauthorized redistribution of open-source Gestionale
Open version 10.00 and commercial use of later, non-open update-source versions
to make and distribute competing software. They sought injunctions and related
copyright/trademark relief. Appellants argued, among other things, that the
software's use of MySQL subject to GPL made the versions open source and that
this defeated the claim. The accessible judgment records the requests and the
appeal; it does not identify the anonymised parties reliably enough to expand
their names beyond the published case label.

## Holdings and relief actually awarded

- The court rejected the appeal and confirmed the appealed partial judgment.
  It held that redistributing source or binary version 10.00 without the BSD
  copyright notice, licence conditions, and disclaimer violated the cumulative
  BSD conditions and made that use unlawful under the cited Italian copyright
  provisions.
- It confirmed that the later 10.01/10.02 source versions were not freely
  reusable merely because the base version was open source; the specific PAGO
  contract limited their use and transfer.
- It treated the asserted GPL/MySQL issue as belonging to the relationship with
  the MySQL right holder and held that an upstream GPL breach would not, by
  itself, turn the later versions into open source or defeat the proven violation.
  The court awarded appeal costs as stated in its dispositive text. It did not
  order GPL source publication or resolve a GPL-owner infringement claim.

## What it supports

- A public-license user's permission can depend on satisfying the particular
  notice/licence/disclaimer conditions stated in the licence.
- A party cannot establish a broad downstream open-source entitlement merely by
  alleging an upstream GPL issue outside the litigated right-holder relationship.

## What it does not establish

- The validity, scope, derivative-work boundary, or remedy of GNU GPL.
- That BSD and GPL have interchangeable conditions or consequences.
- A source-disclosure order, a worldwide remedy, or a binding Italian Supreme
  Court rule.

## Key facts and reasoning

The court treated the BSD redistribution conditions as cumulative and found the
record deficient on multiple requirements, not only a copyright notice. It
rejected an asserted presumption that later derivative versions remained open
source, relying on the contractual and factual record. The GPL discussion is
narrow: it prevents a non-right-holder defence from deciding separate MySQL/GPL
rights in this case.

## Treatment in this repository

- Related matter: [PR-0004](../../matters/case-census/international-open-source-license-enforcement-census.md).
- Distinguishing authority: [*Entr'Ouvert v. Orange*](entrouvert-v-orange-paris-2024.md) concerns GPLv2 and French law.
- Recheck trigger: an official Italian judicial copy, a Cassation disposition,
  a certified translation, or proposed use for a GPL rather than BSD proposition.
