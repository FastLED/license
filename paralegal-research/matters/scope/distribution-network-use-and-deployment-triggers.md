---
id: PR-0010
title: Distribution, network use, and deployment triggers
question: "Which acts trigger public-license or source-available obligations: distribution/conveyance, remote network use, internal deployment, or a hosted service?"
short_answer: "Most traditional reciprocal licenses trigger their source obligations on distribution or GPLv3-style conveyance, not private internal use. AGPLv3 adds a modified-program remote-interaction offer; OSL defines External Deployment; RPL defines Deploy to include internal/external use; SSPL §13 addresses offering program functionality as a service. MPL/EPL/CDDL are distribution-focused and EUPL adds distribution or communication of derivatives. ELv2's managed-service restriction and other source-available use limits are distinct. Exact definitions, recipient, modification, and version determine the result; the reviewed U.S. authorities do not establish a final AGPL §13 network-only remedy."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, US-state-contract, European-Union]
licenses: [GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, source-available]
actors: [distributor, modifier, service-operator, customer, recipient, copyright-owner]
conduct: [distribute, convey, deploy, provide-network-access, provide-hosted-service, withhold-source]
topics: [scope, distribution, network-use, deployment, source-disclosure]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0002, PR-0003, PR-0006, PR-0007, PR-0009]
supersedes: []
---

# PR-0010: Distribution, network use, and deployment triggers

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: a distributor, modifier, service operator, affiliate, customer, or
remote user. Trigger: transfer of copy/object code, conveyance, public
communication, hosted functionality, or internal/external deployment. This
memo reports license text and limited court record; it does not decide whether
a real deployment meets technical definitions, whether corporate affiliates are
one licensee, or a remedy.

## Short answer

The trigger must be read from the selected instrument. GPLv2's source clauses
are distribution based; GPLv3/AGPLv3 use conveyance for object-code obligations.
AGPL §13 is an additional trigger only where a modified version enables remote
network interaction, requiring an offer to those users. MPL, EPL, and CDDL are
distribution focused; EUPL uses distribution or communication of derivatives.
OSL's External Deployment and RPL's Deploy reach beyond a transfer, while SSPL
§13 addresses a service offering and defined Service Source Code. BUSL/FSL use
restrictions and ELv2's managed-service restriction are not reciprocal public
source triggers.

No reviewed final U.S. merits judgment determines the exact remedy for an AGPL
§13 network-only violation; PR-0001 and PR-0003 therefore remain controlling
repository cautions. A text trigger can create a licensing obligation without
automatically establishing copyright infringement, contract formation, or
compelled performance; see PR-0006 and PR-0007.

## Analysis

### Trigger matrix from official texts

| License pattern | Trigger/audience | Boundary/limit |
|---|---|---|
| GPL-2 | Distribution of modified work or executable/object code; source recipient/offer routes | Private use is outside these distribution clauses |
| GPL-3 | Conveying covered work/object code; Corresponding Source routes | No general SaaS trigger |
| AGPL-3 | GPL-3 conveyance plus modified version's remote network interaction; offer to remote users | Must be a modified version and actual interaction; §13 remedy unresolved |
| LGPL-2.1/3 | Distribution/conveyance of library/combined work under version-specific routes | Application/relink/source boundaries vary |
| MPL-2/EPL-2/CDDL-1 | Distribution of covered/program/executable forms | Larger-work/file distinction; no general network trigger |
| EUPL-1.2 | Distribution or communication of derivative works | Applicable Member-State law and derivative definition |
| OSL-3 | Distribution/communication and External Deployment | Exact definition and assent/copyright nexus unresolved |
| RPL-1.5 | Deploy includes internal/external use/distribution; public source for licensed software/extensions | Required Components and entity facts matter |
| SSPL-1 | GPL-style conveyance plus provider makes functionality available to third parties as a service | Service Source Code definition may reach management code |
| BUSL/ELv2/Commons Clause/FSL/PolyForm | Use, competition, sale, managed-service, or additional-use limits as written | Not automatically a reciprocal source publication rule |

These are official-text propositions from the license cards. They are not
holdings concerning a specific cloud, API, container, appliance, affiliate, or
customer configuration.

### Distribution and remote use are not interchangeable

Copyright distribution/conveyance facts can support a conventional infringement
theory if permission is conditional and lost. Network/deployment terms can be
contractual/license conditions but require a separate analysis of nexus,
formation, claimant, and remedy. The audience also changes: GPL source is
generally connected to conveyed copies; AGPL users receive a §13 opportunity;
RPL invokes the open-source community; SSPL says all network users. A source
repository accessible to the public may not answer whether it contains the
defined source, is timely, identifies the version, or reaches the required
audience.

### Relevant authority and contrary limits

*Fisher* leaves factual GPLv3 conveyance/cure issues unresolved. *Artifex* and
*XimpleWare* concern alleged distribution; neither decides AGPL network-only
operation. *SFC v. Vizio* concerns claimed distributed-device source and
beneficiary performance, not AGPL §13. Thus do not generalize a distribution
case to hosted service or vice versa. The CJEU's *IT Development* supplies an
EU reserved-act limitation principle, not a remote-source rule.

## Scenario matrix

| Scenario | Textual first question | Main uncertainty |
|---|---|---|
| Appliance shipped with GPLv2 binary | Was it distributed and was complete source/offer supplied? | Scope, offer validity, owner/standing |
| Unmodified GPLv3 program offered only as SaaS | Was anything conveyed? | No GPLv3 general network trigger |
| Modified AGPLv3 application offered through browser/API | Does remote interaction with modified Program occur? | Modification, interaction, §13 enforcement theory |
| RPL code used only within enterprise | Does "Deploy" include the use/entity? | Definition, formation, enforceability |
| ELv2 product provided as managed service | Is provider offering the software itself to third parties? | Exact service/product facts |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0007](../../authorities/licenses/gnu-agpl-v3.md), [AUTH-0010](../../authorities/licenses/gnu-gpl-v3.md), [AUTH-0009](../../authorities/licenses/gnu-gpl-v2.md) | GNU trigger text | License texts only |
| [AUTH-0013–0021](../../authorities/licenses/) | File/deployment/service family trigger text | Exact version/facts control |
| [AUTH-0003](../../authorities/cases/artifex-v-hancom.md), [AUTH-0033](../../authorities/cases/ximpleware-v-versata-tro.md), [AUTH-0042](../../authorities/cases/fisher-v-sas-automation-summary-judgment.md) | Limited U.S. distribution litigation | Pretrial/interim; no network-source rule |
| [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) | Recipient source-performance theory | Pending, not a holding |
| [AUTH-0050](../../authorities/cases/it-development-v-free-mobile.md) | EU limitation/infringement route | Not network/public-license case |

## What would change the answer

- The binary/source delivery, API/service architecture, modification history,
  user population, entity/affiliate facts, and exact license/version.
- A final on-point AGPL/OSL/RPL/SSPL deployment judgment or statutory change.

## Open questions for counsel

- Which facts evidence conveyance, external deployment, or service availability
  and who was the legally relevant user/recipient?
- Is the requested source tied to a copyright claim, contract performance, or
  both, and what remedy is actually available in the chosen forum?

## Repository implications

This research does not classify any deployment or recommend a license change.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial scope synthesis for issue #17 | Agent; attorney review pending |
