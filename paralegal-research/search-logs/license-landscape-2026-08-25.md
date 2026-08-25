# License-landscape search log — 2026-08-25

> Research log for attorney review, not legal advice. This records what was
> searched and is not proof that unlocated authority does not exist.

## Scope and method

- Matter: [PR-0002](../matters/license-comparison/copyleft-source-availability-license-landscape.md).
- Date searched: 2026-08-25 (America/Los_Angeles).
- Inclusion: the exact requested license/version; operative steward text;
  OSI status; official project licensing statements; existing repository
  authority cards; direct court/government materials if located.
- Exclusion: project-wide status where an exact release is multi-licensed;
  unverified blogs as legal authority; a worldwide exhaustive docket census.
- Negative-result convention: “not located” means only that the stated search
  set did not surface a reported decision; it is not a claim that no action,
  settlement, docket, or unpublished decision exists.

## Repository pre-search and issue routing

- Read `AGENTS.md`, `paralegal-research/AGENTS.md`,
  `paralegal-research/INDEX.md`, `BACKLOG.md`, both templates, and existing
  AUTH-0007 before web research.
- Searched local corpus with: `rg -n -i "license landscape|copyleft|source.available|GPL|MPL|EUPL|SSPL|BUSL|PolyForm|FSL|reciprocal" paralegal-research LICENSE LEGAL-REVIEW.md README.md`.
- Read issue: `gh issue view 17 --repo FastLED/license`. The index contained
  PR-0001 only; its AGPL-remedies scope is related but does not answer this
  license-text landscape question.

## Primary sources checked

| Family | Direct authority checked | Result used |
|---|---|---|
| OSI status | [OSI approved licenses](https://opensource.org/licenses) | Current approved-list classification; OSL/RPL exact pages also checked |
| GNU | [GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html), [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html), [LGPL-2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html), [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html), [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html) | Terms, source timing, termination, patents |
| File/copyleft | [MPL-2.0](https://www.mozilla.org/en-US/MPL/2.0/), [EPL-2.0](https://www.eclipse.org/legal/epl-2.0/), [CDDL-1.0](https://docs.oracle.com/en/servers/x86/x9-2/license-manual/common-development-and-distribution-license-cddl.html), [EUPL-1.2](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12) | Boundary, notice/source, termination, patents, forum |
| Network/copyleft | [OSL-3.0](https://opensource.org/license/OSL-3.0), [RPL-1.5](https://opensource.org/license/RPL-1.5), [SSPL-1.0](https://www.mongodb.com/legal/licensing/server-side-public-license) | Deployment/service trigger and conditions |
| Source-available | [BUSL-1.1](https://mariadb.com/bsl11/), [ELv2](https://www.elastic.co/licensing/elastic-license/faq), [Commons Clause](https://commonsclause.com/), [PolyForm Shield](https://polyformproject.org/licenses/shield/1.0.0), [FSL](https://fsl.software/) | Restriction, conversion, and publisher status |
| FastLED | [local operative rc1](../../LICENSE), [public repository copy](https://github.com/FastLED/license/blob/main/LICENSE) | Draft comparison only; no adoption conclusion |

## Web queries and results

| Query family | Sources/results | Use or disposition |
|---|---|---|
| `official GPL 2 GPL 3 MPL 2 OSI license` | FSF, Mozilla, OSI | Used official text/status |
| `Eclipse EPL 2 Oracle CDDL 1 EUPL 1.2 official` | Eclipse, Oracle, Joinup/European Commission, OSI | Used operative text/status |
| `MongoDB SSPL 1 MariaDB BUSL 1.1 Elastic License 2 official` | MongoDB, MariaDB, Elastic | Used primary text and project statements |
| `Commons Clause PolyForm Shield FSL 1.1 MIT official` | commonsclause.com, PolyForm Project, fsl.software/fair.io | Used primary text/publisher characterization |
| Exact license/version plus `case`, `court`, `opinion`, `judgment`, `enforcement` | Existing corpus plus official/steward/OSI searches | No reported decision located for the bounded exact-version set listed below; deferred to the case-census lane |

## Negative-result searches and unresolved leads

- No reported decision was located in this pass construing the exact listed
  LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5,
  SSPL-1.0, BUSL-1.1, ELv2, Commons Clause, PolyForm Shield, FSL-1.1-MIT, or
  FastLED rc1. This is bounded to the searches above and the existing corpus.
- GPL/AGPL-related judicial materials already collected under AUTH-0001–0008
  were reused; they are not proof of an all-version reading.
- Required follow-up: CourtListener/PACER/state and non-U.S. official court
  databases; exact-party/product aliases; docket records, complaints, orders,
  and later history; local-law/translation verification for EUPL-related cases.

## Recheck triggers

- OSI registry/status change, steward revision, or project dual-license change.
- An exact-version court decision, government docket, official settlement
  document, or an attorney-selected governing jurisdiction.
- Adoption or attorney-reviewed revision of the FastLED release candidate.
