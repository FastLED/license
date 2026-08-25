---
id: AUTH-0059
title: Christoph Hellwig v VMware Global, Inc.
authority_type: case
jurisdiction: Germany, Hamburg courts
date: 2019-02-28
authority_status: final-reported
court: Landgericht Hamburg
procedural_posture: trial-judgment
precedential_weight: persuasive-trial
licenses: [GNU GPL v2]
topics: [scope, derivative-work, copyright-infringement, source-disclosure]
source_quality: primary
source_url: https://www.landesrecht-hamburg.de/jportal/portal/page/bsharprod.psml?doc.id=KORE218712016&showdoccase=1&st=ent
original_language: German
translation_status: researcher-translation
last_verified: 2026-08-25
related_matter_ids: [PR-0004]
---

# AUTH-0059: *Hellwig v VMware*

## Citation and source

- Full citation: LG Hamburg, 8 July 2016, 310 O 89/15; affirmed/rejected on appeal by Hanseatisches OLG Hamburg in February 2019 (docket/full text not publicly retrieved).
- Direct primary source: [Hamburg state-law portal record](https://www.landesrecht-hamburg.de/jportal/portal/page/bsharprod.psml?doc.id=KORE218712016&showdoccase=1&st=ent) for LG judgment; [ifrOSS report identifying court/date/docket](https://www.ifross.org/?q=en/artikel/hellwig-vmware-landgericht-hamburg-h-lt-urheberrechte-f-r-nicht-belegt).
- Later history: reporting identifies the OLG dismissal and that no further remedy was pursued; official appellate text not located.

## Procedural posture and weight

Final reported German dismissal. German original controls; no official English
translation. The state portal's JavaScript presentation prevented full-text
capture, so English summary is limited and secondary-confirmed.

## Claims, relief, and holding

- Licence/version: GPLv2 Linux contributions; ESXi 5.5.0 vmklinux/vmkernel.
- Claims: Hellwig sought relief based on alleged incorporation/combination without GPL-compliant source disclosure.
- Requested versus awarded relief: claimant sought GPL/copyright enforcement; court awarded no source or other substantive GPL remedy and dismissed the claim.
- Holding: the claimant did not sufficiently establish protectable authorship and/or relevant code adoption on the pleaded proof; courts did not reach a merits holding on derivative work or dynamic linking.

## What it does not establish

- That VMware's architecture complied with GPLv2, or that dynamic linking never creates a covered work.
- A general standing rule for every Linux contributor.

## Key facts and reasoning

The dispute concerned alleged use of Hellwig's kernel work in VMware's ESXi.
Proof and pleading were dispositive before the technical GPL boundary was
adjudicated.

## Treatment in this repository

- Related matters: [PR-0004](../../matters/case-census/international-open-source-license-enforcement-census.md).
- Recheck trigger: official OLG judgment/full text or later German high-court review.
