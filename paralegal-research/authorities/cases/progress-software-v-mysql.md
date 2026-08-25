---
id: AUTH-0151
title: Progress Software Corp. v. MySQL AB
authority_type: case
jurisdiction: US-District-of-Massachusetts
court: United States District Court for the District of Massachusetts
date: 2002-02-28
authority_status: settled
procedural_posture: preliminary-injunction
precedential_weight: persuasive-trial
licenses: [GNU-GPL-v2]
topics: [derivative-work, cure, preliminary-injunction, source-disclosure]
source_quality: official-reproduction
source_url: https://law.justia.com/cases/federal/district-courts/FSupp2/195/328/2485211/
original_language: English
translation_status: not-needed
last_verified: 2026-08-25
related_matter_ids: [PR-0003]
---

# AUTH-0151: *Progress Software Corp. v. MySQL AB*

## Citation and source

- 195 F. Supp. 2d 328, No. 01-11031-PBS (D. Mass. Feb. 28, 2002), [reported order reproduction](https://law.justia.com/cases/federal/district-courts/FSupp2/195/328/2485211/).
- The source reproduces the reported order. An official court-hosted PDF and an authenticated final dismissal/settlement instrument were not located in this audit. Public reporting describes a later settlement, but its terms are not treated as a holding here.
- Original language: English; no translation is needed.

## Procedural posture and weight

Short preliminary-injunction order after a hearing. It is a trial-court,
interlocutory ruling, persuasive only; the GPL portion denies interim relief and
does not decide the claims after trial.

## Claims and requested relief

MySQL, a counterclaim plaintiff, sought to enjoin Progress Software and its
NuSphere subsidiary from sublicensing or distributing MySQL and using the
MySQL mark. The GPL dispute concerned whether NuSphere's Gemini program was a
derivative or an independent/separate work under GPL paragraph 2 and whether
distribution required source. The record also involved an interim commercial
agreement and trademark claims.

## Holdings and relief actually awarded

- The court granted limited preliminary trademark relief: it enjoined specified
  uses of the MySQL mark, subject to a bond.
- It denied MySQL's request for preliminary GPL-related distribution relief.
  On the interim record, expert evidence created a factual dispute on Gemini's
  GPL paragraph 2 status; the court also was not persuaded that July 2001 source
  release did not cure the asserted breach.
- Even assuming likelihood of success, the court found no demonstrated
  irreparable GPL harm on that record, including in light of sworn source
  disclosure and Progress's stipulation to withdraw a commercial-user EULA.
  No GPL source-publication injunction, damages, or final infringement finding
  was awarded.

## What it supports

- GPL covered-work/derivative-work and cure questions can defeat preliminary
  relief where the record leaves material factual disputes.
- Later source availability and the equitable record may matter to interim-harm
  analysis; this is not a construction of a general cure rule.

## What it does not establish

- A holding that linked code is, or is not, a GPL derivative work.
- GPL enforceability, a universal right to cure, or a final remedy for a GPL
  breach.
- That trademark relief in the same order was GPL compliance relief.

## Key facts and reasoning

The court applied ordinary preliminary-injunction factors. It separated the
trademark dispute, where it found a likelihood of success and irreparable harm,
from the GPL question. The narrower GPL ruling turns on the evidentiary record
and the balance of harms, not a determination that Progress had complied.

## Treatment in this repository

- Related matter: [PR-0003](../../matters/case-census/us-open-source-license-enforcement-census.md).
- Contrasting authority: [Fisher summary judgment](fisher-v-sas-automation-summary-judgment.md) likewise leaves GPL coverage/conveyance issues fact dependent.
- Recheck trigger: authenticated final docket documents, settlement instrument,
  or use of the reported order for a proposition beyond interim relief.
