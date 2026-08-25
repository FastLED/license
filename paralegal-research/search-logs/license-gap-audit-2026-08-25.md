# License-gap audit search log — 2026-08-25

> Preliminary research for attorney review, not legal advice. This log records
> an auditable expansion boundary; it does not prove that no other license,
> docket, settlement, or decision exists.

## Scope and method

- Matter: [PR-0002](../matters/license-comparison/copyleft-source-availability-license-landscape.md).
- Date searched: 2026-08-25 (America/Los_Angeles).
- Routing: actor (licensor/licensee/distributor/service operator/recipient);
  conduct (distribution, deployment, network service, commercial use,
  conversion); jurisdiction (text-selected law only unless an existing case
  card applies); issue (textual obligation/status, not legal advice); exact
  named version where available.
- Inclusion rule: an authenticated official steward, project, or OSI text plus
  material reciprocity, deployment, delayed-conversion, commercial-use, or
  enforcement relevance. "Official" includes a publisher-maintained repository
  where the publisher identifies it as the license text.
- Exclusion rule: no authenticated text, merely a generic family name where
  the project text controls, duplicate version/variant, or no material relation
  to the matrix dimensions.
- Local review: read repository and paralegal `AGENTS.md`, `INDEX.md`,
  `TAXONOMY.md`, issue #17, PR-0002, all then-current license cards, and
  `license-landscape-2026-08-25.md`; searched the corpus for each license name,
  version, `case`, `court`, `judgment`, `enforcement`, and `remedy`.

## Included instruments and authenticated sources

| Card | Instrument and classification | Official/steward source checked | Material reason |
|---|---|---|---|
| AUTH-0130 | Artistic License 1.0 — historical OSI-approved | [OSI text](https://opensource.org/license/Artistic-1.0), [OSI registry](https://opensource.org/licenses) | *Jacobsen* comparator; modified-package/source conditions |
| AUTH-0131 | Artistic License 2.0 — OSI-approved | [OSI text/approval](https://opensource.org/license/Artistic-2.0) | Modified source/compiled-source instructions and patent terms |
| AUTH-0132 | Affero GPL v1 — historical reciprocal, not current OSI listing | [Original Affero text](http://www.affero.org/oagpl.html), [SPDX record](https://spdx.org/licenses/AGPL-1.0-or-later.html) | Pre-AGPLv3 network-source trigger |
| AUTH-0133 | CAL 1.0 — OSI-approved | [OSI text/approval](https://opensource.org/license/CAL-1.0) | Third-party recipient autonomy and express specific-performance language |
| AUTH-0134 | Parity 7.0.0 — non-OSI public reciprocal | [Publisher text](https://paritylicense.com/versions/7.0.0.html) | Operation/analyse-with-software public-source trigger |
| AUTH-0135 | Prosperity 3.0.0 — source-available commercial-use restricted | [Publisher repository text](https://github.com/licensezero/prosperitylicense.com/blob/main/3.0.0.md) | 30-day commercial trial |
| AUTH-0136 | CeCILL 2.1 — OSI-approved | [Official CeCILL text](https://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html), [steward status](https://www.cecill.info/index.en.html) | French-law reciprocal/compatibility comparator |
| AUTH-0137 | JPL 1.1 — project-specific public reciprocal | [Jelurida PDF](https://www.jelurida.com/sites/default/files/JPLv1.1-NRS.pdf) | Object-source/airdrop terms and existing Dutch case |
| AUTH-0138 | Sybase Open Watcom 1.0 — historical OSI-approved | [OSI text/approval](https://opensource.org/license/Watcom-1.0) | Internal deployment and public-source duration |
| AUTH-0139 | CERN-OHL-S 2.0 — OSI-approved open hardware | [CERN OHL](https://cern-ohl.web.cern.ch/home), [OSI text/approval](https://opensource.org/license/CERN-OHL-S-2.0) | Strong reciprocal design-source/product comparator, explicitly non-software |
| AUTH-0140 | Sustainable Use 1.0 (n8n) — fair-code/source-available | [n8n official text](https://docs.n8n.io/privacy-and-security/sustainable-use-license) | Internal/noncommercial and no-charge distribution restriction |
| AUTH-0141 | RSALv2 — source-available | [Redis agreement](https://redis.io/legal/rsalv2-agreement/), [Redis overview](https://redis.io/legal/licenses/) | Service/functionality restriction and reinstatement |
| AUTH-0142 | Confluent Community 1.0 — source-available | [Confluent text](https://www.confluent.io/confluent-community-license), [FAQ](https://www.confluent.io/confluent-community-license-faq/) | Competing-service exclusion, assent, forum/arbitration |
| AUTH-0143 | CockroachDB Community Agreement — product agreement, not OSI | [Cockroach Labs agreement](https://www.cockroachlabs.com/cockroachdb-community-license/) | Paid self-hosted/trial and release-specific Core-license boundary |

## Status checks

- The OSI registry was used only to identify current OSI approval. It supports
  OSI status for Artistic-1.0/2.0, CAL-1.0, CeCILL-2.1, Watcom-1.0, and
  CERN-OHL-S-2.0. CERN-OHL-S remains categorized here as open hardware, not
  software, despite OSI approval.
- Affero GPL v1 is historical and distinct from GNU AGPL-3.0; the current OSI
  registry check did not supply a separate AGPLv1 entry.
- Parity is a public reciprocal license but not OSI-approved. Prosperity,
  Sustainable Use, RSALv2, and Confluent Community are source-available or
  fair-code/commercially restricted instruments, not open source by OSI status.
- CockroachDB's current agreement does not itself classify every Core release;
  the text directs the reviewer to the applicable release license file.

## Judicial-treatment searches and bounded results

Searched the local corpus and official/steward/OSI pages with each exact name
and version plus `case`, `court`, `opinion`, `judgment`, `enforcement`, and
`remedy`. No additional reported decision was located for Artistic-1.0,
Artistic-2.0, Affero GPL v1, CAL-1.0, Parity-7.0.0, Prosperity-3.0.0,
CeCILL-2.1, Watcom-1.0, CERN-OHL-S-2.0, n8n Sustainable Use, RSALv2,
Confluent Community, or the current CockroachDB agreement.

Two qualified exceptions are already in the corpus:

- [*Jacobsen v. Katzer*](../authorities/cases/jacobsen-v-katzer.md) is a
  Federal Circuit condition-of-license decision concerning an Artistic License.
  It is not a version-wide source-publication or remedy decision; exact text
  correspondence must be verified for a version-specific proposition.
- [*Jelurida v. Apollo*](../authorities/cases/jelurida-v-apollo.md) records a
  Dutch appellate interim order requiring specified JPL compliance within the
  EU and a penalty mechanism. It is not a final worldwide JPL construction or
  a general source-publication rule.

These are bounded negative findings only. They do not exclude private disputes,
unreported decisions, dockets, settlements, arbitration, later history, or
foreign-language materials outside the recorded search set.

## Excluded candidates and reasons

| Candidate | Disposition |
|---|---|
| Artistic License (Perl) 1.0 / Clarified Artistic | Excluded as adjacent historical variants: the requested Artistic 1.0 and 2.0 cards cover the relevant *Jacobsen* comparison; exact variant text needs project-specific review. |
| GNU AGPL-3.0 | Already represented by AUTH-0007; not duplicated. |
| CERN-OHL-W-2.0 and CERN-OHL-P-2.0 | Excluded as sibling variants; requested strong-reciprocity variant is the material comparator. |
| CeCILL-B/C | Excluded as different permissive/component variants; not necessary to answer the requested CeCILL-2.1 reciprocal comparison. |
| Redis SSPLv1/AGPLv3 alternatives | Already represented by AUTH-0019/AUTH-0007; RSALv2 card is limited to RSALv2. |
| Historical CockroachDB BUSL/older CCL release terms | Excluded pending an exact release and authenticated release file; current agreement expressly delegates Core licensing to the applicable release file. |
| Other projects named "Sustainable Use License" | Excluded because the name is non-unique; only n8n's authenticated v1 text is carded. |

## Residual gaps and recheck triggers

- Docket-level and non-English searches for each exact version, including later
  history for *Jelurida*, remain outside this audit.
- Verify the actual release text, notices, parameters, special conditions, and
  dual-license election before applying any card to a product.
- Recheck OSI registry status, publisher/steward revisions, project license
  files, judicial/arbitral outcomes, and translations before relying on a
  classification or enforcement proposition.
