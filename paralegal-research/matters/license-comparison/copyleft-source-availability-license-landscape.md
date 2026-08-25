---
id: PR-0002
title: Copyleft and source-availability license landscape
question: "How do the specified reciprocal, open-source, and source-available instruments differ in trigger, scope, disclosure, termination, commercial alternatives, patents, compatibility, forum/law, and known judicial treatment?"
short_answer: "The OSI-approved instruments are public licenses with materially different reciprocal triggers and boundaries: GPL-family licenses center on conveying covered works, file-level licenses center on changed covered files, and OSL/RPL, CAL, and Watcom add network, third-party, or deployment concepts. SSPL, BUSL, ELv2, Commons Clause, PolyForm Shield, FSL before conversion, RSALv2, Confluent Community, Prosperity, Sustainable Use, and the FastLED release candidate are source-available or restricted instruments, not OSI-approved open source. Historical Artistic/AGPLv1 instruments, project-specific JPL, and CERN-OHL-S's non-software hardware scope require separate treatment. Text comparison identifies obligations but does not determine a work boundary, enforceability, claimant, compatibility, or remedy in a concrete jurisdiction."
research_status: partial
legal_review: pending
jurisdictions:
  - not-applicable-license-text-comparison
licenses:
  - GNU GPL versions 2 and 3
  - GNU LGPL versions 2.1 and 3
  - GNU AGPL version 3
  - Artistic Licenses 1.0 and 2.0
  - Affero General Public License version 1
  - Mozilla Public License 2.0
  - Eclipse Public License 2.0
  - Common Development and Distribution License 1.0
  - European Union Public Licence 1.2
  - CeCILL 2.1
  - Open Software License 3.0
  - Reciprocal Public License 1.5
  - Cryptographic Autonomy License 1.0
  - Parity Public License 7.0.0
  - Prosperity Public License 3.0.0
  - Jelurida Public License 1.1
  - Sybase Open Watcom Public License 1.0
  - CERN Open Hardware Licence Version 2 Strongly Reciprocal
  - Server Side Public License 1.0
  - Business Source License 1.1
  - Elastic License 2.0
  - Commons Clause License Condition 1.0
  - PolyForm Shield License 1.0.0
  - Functional Source License 1.1 MIT
  - Sustainable Use License 1.0
  - Redis Source Available License 2.0
  - Confluent Community License 1.0
  - CockroachDB Community License Agreement
  - FastLED Reciprocal License 1.0-rc1
actors:
  - licensor
  - steward
  - distributor
  - modifier
  - service-operator
  - recipient
conduct:
  - modify
  - distribute
  - convey
  - deploy
  - provide-network-access
  - withhold-source
topics:
  - license-comparison
  - copyleft
  - source-availability
confidence: medium
last_verified: 2026-08-25
github_issues:
  - https://github.com/FastLED/license/issues/17
related_matter_ids: [PR-0001]
supersedes: []
---

# PR-0002: Copyleft and source-availability license landscape

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: a licensor, distributor, modifier, service operator, or recipient. Conduct:
copying, modification, conveyance/distribution, deployment, or product/service
use under the exact listed version. Jurisdiction: no particular country; this is
operative-text/status research, not an enforcement opinion. Time/version: the
versions named in the matrix, verified 2026-08-25. “Commercial alternative”
means whether the text/steward materials identify a separate paid or negotiated
path; it does not imply an entitlement to one. The comparison excludes a
project-specific adoption decision, claimant standing, remedies, and the full
case census assigned elsewhere in issue #17.

This expansion adds historical software texts, deployment/third-party triggers,
commercial-use and fair-code restrictions, and one project-specific DLT text.
It separately identifies CERN-OHL-S-2.0 as open-hardware/design-source scope,
not a software-license precedent. The current CockroachDB Community Agreement
is product-level: its own text directs reviewers to each Core release's license
file, so the agreement does not classify every CockroachDB release.

## Short answer

The current [OSI approved-license registry](https://opensource.org/licenses)
supports classifying GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0,
EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, Artistic-1.0/2.0, CAL-1.0,
CeCILL-2.1, and Watcom-1.0 as OSI-approved. CERN-OHL-S-2.0 is also OSI-approved
but is an open-hardware instrument. The rest in this assignment are not listed
there and their stewards describe them as source-available/restricted,
fair-code, project-specific, or, for the FastLED item, a release-candidate
draft.
“Source available” does not itself identify a disclosure duty: BUSL and FSL use
time/competitive-use restrictions; ELv2 and Commons Clause restrict selected
commercial/service conduct; PolyForm Shield restricts competing purpose; SSPL
has an expansive service-source condition. Every classification is for the
named instrument, not an entire project or later multi-license election.

## Analysis

### Status is distinct from source publication

OSI approval is an official status, not shorthand for whether a repository is
public. The OSI registry identifies the approved instruments above. MariaDB’s
[BUSL text](https://mariadb.com/bsl11/) expressly says it is not Open Source;
the [Commons Clause publisher](https://commonsclause.com/) says its combined
instrument is not open source; and [Fair Source](https://fair.io/about/) draws
the same distinction before delayed OSI-license conversion. The FastLED draft
identifies itself as a renamed MPL-derived release candidate and says Mozilla
has not reviewed it; it must remain behind the repository attorney-review gate.

### Textual obligations are not judicial outcomes

The matrix summarizes the license text, not a holding. Existing U.S. cards
record limited GPL/AGPL-related decisions and procedural outcomes, including
[*Jacobsen*](../../authorities/cases/jacobsen-v-katzer.md),
[*MDY*](../../authorities/cases/mdy-industries-v-blizzard.md),
[*Artifex*](../../authorities/cases/artifex-v-hancom.md), and
[BusyBox/Westinghouse](../../authorities/cases/busybox-westinghouse.md).
They do not establish a complete interpretation of a version or a universal
source-publication remedy. In targeted searches of official steward/OSI sources
and the existing corpus on 2026-08-25, no reported decision was located that
construed the precise listed version for LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0,
CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, BUSL-1.1, ELv2, Commons Clause,
PolyForm Shield, FSL-1.1-MIT, or the FastLED rc1. This is a bounded negative
finding, not proof that no case, docket, settlement, arbitral result, or
unreported decision exists. The issue’s case-census lane must test it against
court/docket databases.

The expansion found one material exception: the existing Dutch appellate card
for [*Jelurida v Apollo*](../../authorities/cases/jelurida-v-apollo.md) records
an interim JPL compliance order, not a universal JPL merits/remedy rule. For
the newly added Artistic-1.0, Artistic-2.0, Affero GPL v1, CAL-1.0, Parity-7.0,
Prosperity-3.0, CeCILL-2.1, Watcom-1.0, CERN-OHL-S-2.0, Sustainable Use (n8n),
RSALv2, Confluent Community, and CockroachDB agreement texts, no additional
reported exact-instrument decision was located in the recorded official/steward
and corpus search. This bounded result does not negate *Jacobsen*'s Artistic
License holding or unlocated litigation.

## Normalized comparison matrix

Abbreviations: “recipient” means recipients of the conveyed/distributed work;
“public” means an audience wider than particular recipients; “N/S” means not
stated by the named standard text; “sep.” means a separate-license path can
exist but its commercial terms are not fixed by the public license.

| Instrument / status | Trigger and covered boundary | Disclosure audience, timing, duration | Cure / reinstatement | Commercial alternative | Patents; compatibility; forum/law | Judicial-treatment record |
|---|---|---|---|---|---|---|
| [GPL-2.0](../../authorities/licenses/gnu-gpl-v2.md) — OSI | Distribution of Program/whole work based on it; private modification outside distribution clauses | Recipient source with object code or written offer; offer ≥3 years | Automatic termination; no express cure | Fees/sep. licensing permitted | No express patent grant; compatibility fact/version specific; N/S | Existing GPL-related cards; no version-wide holding located |
| [GPL-3.0](../../authorities/licenses/gnu-gpl-v3.md) — OSI | Conveying covered work / work based on Program; aggregate carve-out | Corresponding Source to recipients; s.6(b) offer ≥3 years | s.8 automatic, provisional/permanent reinstatement | Fees/sep. permissions | Express contributor patent terms; anti-further restrictions; N/S | Existing GPL-related cards; no version-wide holding located |
| [LGPL-2.1](../../authorities/licenses/gnu-lgpl-v2-1.md) — OSI | Library modifications; combined work conditions distinguish work using Library | Library source and s.6 relinking/modification material to recipients; offer route ≥3 years | Automatic termination; no express cure | Permits commercial distribution / sep. licensing of independent work | No express standalone patent grant; incorporates GPL-2 where stated; N/S | No exact-version reported decision located in bounded search |
| [LGPL-3.0](../../authorities/licenses/gnu-lgpl-v3.md) — OSI | Library / Application / Combined Work conditions | Minimal Corresponding Source and relinking material to recipients on conveyance | GPL-3 s.8 | Commercial distribution / sep. permissions | GPL-3 patent terms; compatibility depends on combination; N/S | No exact-version reported decision located in bounded search |
| [AGPL-3.0](../../authorities/licenses/gnu-agpl-v3.md) — OSI | GPL covered-work conveyance plus modified-program remote interaction | Corresponding Source to network users on s.13 interaction; conveyance rules also apply | GPL-3 s.8 | Fees/sep. permissions | GPL-3 patent terms; compatibility fact/version specific; N/S | [PR-0001](../remedies/agpl-noncompliance-judicial-remedies.md); limited existing authority, no routine source-publication judgment |
| [MPL-2.0](../../authorities/licenses/mozilla-public-license-v2.md) — OSI | Distribution of file-level Covered Software / Modifications; separate-file Larger Work carve-out | Source to executable recipients by reasonable means in timely manner | s.5 30/60-day rules | Sep. licenses possible; commercial distribution allowed | Contributor patent grant/retaliation; selected GPL-family secondary licenses; defendant-principal-place forum/law | No exact-version reported decision located in bounded search |
| [EPL-2.0](../../authorities/licenses/eclipse-public-license-v2.md) — OSI | Distribution of Program/Modified Works; linking/interface exclusion | Program source and access statement to recipients on distribution | Reasonable cure after awareness | Commercial/other executable licenses subject to terms | Contributor patent grant; optional GPL secondary designation; N/S | No exact-version reported decision located in bounded search |
| [CDDL-1.0](../../authorities/licenses/common-development-distribution-license-v1.md) — OSI | Distribution of Covered Software files; Larger Work carve-out | Covered source available with executable distribution | 30 days after notice | “Commercial Use” allowed / sep. executable terms | Contributor patent grant/retaliation; compatibility not granted; California/Santa Clara | No exact-version reported decision located in bounded search |
| [EUPL-1.2](../../authorities/licenses/european-union-public-licence-v1-2.md) — OSI | Distribution/communication of work and derivatives | Same-license source/derivative distribution to recipients/public communication audience | 30 days after notice | No fixed paid alternative; commercial use not barred | Contributor patents/retaliation; art.5 compatibility list; licensor-seat EU law/court | No exact-version reported decision located in bounded search |
| [OSL-3.0](../../authorities/licenses/open-software-license-v3.md) — OSI | Distribution/communication plus External Deployment of original/derivative | Source with distributed copy or accessible repository while distribution continues; external deployment treated as distribution | Immediate on relevant breach; no general cure | Licensor may dual license | Patent grant/retaliation; no compatibility clause; N/S | No exact-version reported decision located in bounded search |
| [RPL-1.5](../../authorities/licenses/reciprocal-public-license-v1-5.md) — OSI | “Deploy” (internal/external) and Required Components | Public source to open-source community at deployment | First breach: 30 days after notice; otherwise immediate | Sep. commercial path not prohibited | Patent terms/retaliation; compatibility N/S; California/San Francisco | No exact-version reported decision located in bounded search |
| [SSPL-1.0](../../authorities/licenses/server-side-public-license-v1.md) — source-available, not OSI | GPL-style conveyance plus providing Program functionality as third-party service | Corresponding Source to recipients; s.13 Service Source Code via no-charge network download to all service users | GPL-3 s.8 | MongoDB states commercial licenses available | GPL-3 patent terms; no OSI compatibility status; N/S | No exact-version reported decision located in bounded search |
| [BUSL-1.1](../../authorities/licenses/business-source-license-v1-1.md) — source-available, not OSI | Any use/copy/derivative subject to release-specific Additional Use Grant | No reciprocal disclosure duty; source availability/Change Date are release parameters | Automatic termination; no stated cure | Text directs purchase commercial license or refrain | No patent / compatibility / forum-law rule in standard text | No exact-version reported decision located in bounded search |
| [ELv2](../../authorities/licenses/elastic-license-v2.md) — source-available, not OSI | Any exercise of grant; prohibition on hosted/managed service, key circumvention, notice removal | No reciprocal source disclosure duty or duration | No stated cure/reinstatement | Separate commercial/service offerings possible | No patent / compatibility / forum-law rule stated | No exact-version reported decision located in bounded search |
| [Commons Clause](../../authorities/licenses/commons-clause-v1.md) — source-available condition, not OSI | Underlying license, except no right to “Sell” as defined | Underlying license controls disclosure/audience/timing/duration | Underlying license controls | Negotiation may be required to Sell | Underlying license controls all four fields | No condition-specific reported decision located in bounded search |
| [PolyForm Shield](../../authorities/licenses/polyform-shield-v1.md) — source-available, not OSI | Use/change/distribution except competing purpose | No reciprocal source disclosure duty | First written notice: 32 days + corrective steps | No fixed price; licensor may grant other licenses | Patent grant/defense; no compatibility/forum-law selection | No exact-version reported decision located in bounded search |
| [FSL-1.1-MIT](../../authorities/licenses/functional-source-license-v1-1-mit.md) — source-available before conversion | Release-specific competitive-use restriction | No reciprocal source duty; conversion to MIT after stated two years | Verify exact raw text/release | Conversion plus separate commercial path may exist | Exact raw text governs patent/compatibility/forum; future MIT is separately OSI | No exact-version reported decision located in bounded search |
| [FastLED rc1](../../authorities/licenses/fastled-reciprocal-license-v1-rc1.md) — draft, not OSI | MPL-like file boundary plus Modified FastLED commercial Triggering Transfer; network-only use excluded | Recipient source on executable distribution; public complete source on/before trigger, then ≥3 years/while distributing | MPL-style plus prospective-only result for late s.11.3 publication | Separate written license can excuse s.11.3 | Contributor patent grant; expressly GPL-family incompatible; defendant-principal-place forum/law | No judicial treatment; draft only |
| [Artistic-1.0](../../authorities/licenses/artistic-license-v1.md) — historical OSI | Modified Package distribution under stated alternatives | Modified-package route; compiled standard version needs source instructions; duration N/S | N/S | Distributor fees / outside arrangements | Patent N/S; aggregation; forum/law N/S | *Jacobsen* is Artistic-License condition authority; exact-version fit requires care |
| [Artistic-2.0](../../authorities/licenses/artistic-license-v2.md) — OSI | Modified Package/source/compiled distribution; separate-work/interface boundaries | Modified-source alternative; compiled standard version source instructions, corrected or distribution ceases after awareness | 30 days for invalid compiled-source instructions | Distributor fees / outside arrangements | Patent grant/retaliation; selected relicensing route; forum/law N/S | No exact-version reported decision located in bounded search |
| [Affero GPL v1](../../authorities/licenses/affero-general-public-license-v1.md) — historical, not current OSI listing | GPLv2 distribution plus modified program normally used over network | Complete source offer to network users under added s.2(d); GPLv2 routes otherwise | GPLv2 automatic termination; no express cure | Separate permissions possible | Patent/forum/law N/S | No exact-version reported decision located in bounded search |
| [CAL-1.0](../../authorities/licenses/cryptographic-autonomy-license-v1.md) — OSI | Non-affiliated third party receives Work element | Permissions/materials needed for independent use/modification and no capability/data loss | Text-specific; no fixed general cure summarized | N/S | Patent terms; recipient third-party-beneficiary/specific-performance language; forum/law N/S | No exact-version reported decision located in bounded search |
| [Parity-7.0.0](../../authorities/licenses/parity-public-license-v7.md) — non-OSI public reciprocal | Develop, operate, or analyze with software, beyond prototype exception | Public preferred source within 30 days | 30-day knowledge-based excuse | No fixed paid path | Patent grant/defense; forum/law N/S | No exact-version reported decision located in bounded search |
| [Prosperity-3.0.0](../../authorities/licenses/prosperity-public-license-v3.md) — source-available | Commercial use beyond a 30-day company trial | Notice only; no reciprocal source duty | 30-day notice excuse | Commercial path implicit/outside grant | Patent grant/defense; forum/law N/S | No exact-version reported decision located in bounded search |
| [CeCILL-2.1](../../authorities/licenses/cecill-v2-1.md) — OSI | Modified-software distribution; internal/external module boundary | Source availability under CeCILL on distribution | Textual termination/cure terms | Commercial use/services allowed | Patent terms; named compatibility; French law/Paris courts | No exact-version reported decision located in bounded search |
| [JPL-1.1](../../authorities/licenses/jelurida-public-license-v1-1.md) — project-specific public reciprocal | Covered/DLT work conveyance, modification, DLT fork/configuration rules | Corresponding Source with object code; three-year offer route | Automatic termination; no general cure | Special Conditions may require permission/commercial license | GPL-style scope plus DLT airdrop; exact Special Conditions control | [Dutch interim compliance order](../../authorities/cases/jelurida-v-apollo.md), not universal rule |
| [Watcom-1.0](../../authorities/licenses/sybase-open-watcom-public-license-v1.md) — historical OSI | Deploy, including non-R&D internal organizational use | Public source for deployment duration or 12 months, whichever longer | 30 days after awareness | Additional terms/fees allowed | Patent grant; California/ND Cal. | No exact-version reported decision located in bounded search |
| [CERN-OHL-S-2.0](../../authorities/licenses/cern-ohl-s-v2.md) — OSI open hardware | Make/convey design source or Products | Complete Source or source-location notice; location >=3 years | No stated general cure | Commercial use allowed | Hardware/design source; compatible-source rule; forum/law N/S | No exact-version reported decision located in bounded search |
| [Sustainable Use 1.0 (n8n)](../../authorities/licenses/sustainable-use-license-v1.md) — fair-code/source-available | Use outside internal, noncommercial, or personal purposes; paid/commercial provision | Notice only; no reciprocal source duty | N/S | n8n enterprise agreement | Patent/forum/law N/S | No exact-version reported decision located in bounded search |
| [RSALv2](../../authorities/licenses/redis-source-available-license-v2.md) — source-available | Third-party service/functionality offering | Notices/modification notice; no reciprocal source duty | First notice/cease within 30 days reinstates; later breach permanent | Separate Redis licenses/product paths | Patent grant/retaliation; regional CA/Israel/England law/courts | No exact-version reported decision located in bounded search |
| [Confluent Community 1.0](../../authorities/licenses/confluent-community-license-v1.md) — source-available | Competing online-service "Excluded Purpose" | Notices only; no reciprocal source duty | Automatic permanent termination; no cure | N/S | Patent N/S; CA/Santa Clara or JAMS/Palo Alto | No exact-version reported decision located in bounded search |
| [CockroachDB Community Agreement](../../authorities/licenses/cockroachdb-community-license.md) — product agreement, not OSI | Self-hosted/enterprise and release-specific product terms | Redistribution notices; no reciprocal source duty | Text/license-key/payment specific | Paid enterprise and trial paths | Patent terms; New York/U.S. law; Core text controls Core status | No exact-instrument reported decision located in bounded search |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0007](../../authorities/licenses/gnu-agpl-v3.md), [AUTH-0009–0025](../../authorities/licenses/), and [AUTH-0130–0143](../../authorities/licenses/) | Official-text facts and normalized fields | License text/status, not enforcement holding |
| [OSI registry](https://opensource.org/licenses) | OSI approved status for the listed public licenses | Current registry; does not decide compatibility or enforceability |
| [Search log](../../search-logs/license-landscape-2026-08-25.md) | Search method, source URLs, negative-search scope | Reproducible but not exhaustive case census |

## What would change the answer

- A release-specific parameter, dual-license election, exception, or notice.
- The governing jurisdiction’s copyright/contract law or a technical fact about
  linkage, distribution, service role, or source availability.
- A controlling decision, official steward correction, or OSI registry change.

## Open questions for counsel

- Which deployment and distribution facts should define a project-specific
  boundary analysis?
- Which jurisdiction and potential claimant/standing theory controls a future
  enforcement question?
- Is a certified translation or local-law analysis required for any EUPL matter?

## Repository implications

This comparison does not recommend any license or justify editing `LICENSE`.
The FastLED entry is solely a comparison target and remains subject to
`LEGAL-REVIEW.md`.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial license-text/status landscape and bounded judicial-treatment search | Agent; attorney review pending |
| 2026-08-25 | Gap audit: added historical, deployment, fair-code, source-available, JPL, and open-hardware comparators | Agent; attorney review pending |
