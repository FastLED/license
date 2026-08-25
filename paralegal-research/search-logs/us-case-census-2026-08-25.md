# U.S. open-source-license case census — search log

> Research log for attorney review, not legal advice. Searches were run on
> 2026-08-25. Court documents, not search-result summaries, control the cards.

## Scope, inclusion, and exclusion

Included: U.S. opinions, orders, complaints, judgments, and publicly disclosed
settlements that address GPL-family or comparable public-license enforcement,
license construction, or a meaningful defense. A separate docket order in the
same case is listed only when it resolves a materially different question.

Excluded from substantive propositions: commentary alone; a GPL mention with
no issue decided; press reports that did not supply a primary record; and
non-U.S. decisions assigned to the comparative lane. *Planetary Motion* and
*KBS v. Dijk* are retained as expressly limited negative/relevance checks.

## Databases and queries

| Source/database | Queries or docket checks | Result/use |
|---|---|---|
| GovInfo, U.S. Courts collection | `XimpleWare 5:13-cv-05161`; `Fisher 3:20-cv-00216`; party names and docket numbers | Primary PDF orders for XimpleWare and Fisher. |
| Ninth Circuit / published appellate opinion reproductions | `Neo4j PureThink 21-16029`; `Wallace IBM 06-2454`; `Planetary Motion Techsplosion 261 F.3d 1188` | Published appellate dispositions; official docket/order URL used when located. |
| CourtListener/Justia docket document indexes | Case number plus `order`, `dismiss`, `summary judgment`, `settlement` | Leads and accessible docket-PDF mirrors; card labels say when source is a court-document mirror rather than court-hosted. |
| SDNY docket index and FSF/SFLC archival pages | `1:08-cv-10764`; `BusyBox Xterasys 07-CV-10455`; `High-Gain 07-CV-10456`; `Verizon GPL` | Complaint/docket identity and disclosed settlement reports. |
| General web, primary-source-first | quoted party names plus `GPL`, `AGPL`, `opinion`, `docket`, `complaint` | Located case leads; secondary accounts are not used as holdings. |

## Searches with material results

- `Planetary Motion Techsplosion GPL` — GPL is a fact in a published trademark
  appeal; no GPL claim or remedy was adjudicated.
- `Wallace Free Software Foundation` and `Wallace IBM 06-2454` — district
  dismissal and Seventh Circuit published antitrust decision.
- `XimpleWare Versata Ameriprise 5:13-cv-05160 5:13-cv-05161` — TRO denial,
  customer dismissal, and later dismissal orders. GovInfo documents 85 and 142
  were reviewed directly.
- `Neo4j PureThink 5:18-cv-07182 21-16029` and `Neo4j Graph Foundation
  3:19-cv-06226` — district orders and nonprecedential appellate disposition;
  Graph Foundation action described as settled in the appellate order.
- `Knowledge Based Solutions Dijk 16-cv-13041` — proprietary-software
  jurisdiction/contract case; no GPL/open-source license identified.
- `Trent P Fisher SAS Automation 3:20-cv-00216 GPL` — GovInfo summary-judgment
  order directly reviewed; GPLv3 coverage/conveyance/cure not finally decided.
- `Free Software Foundation Cisco 1:08-cv-10764` — complaint and public
  settlement announcement; no merits judgment found.
- `BusyBox Monsoon Xterasys High-Gain Verizon` — archived SFLC announcements
  identify settlements/complaints; no contested merits opinion found in the
  documented search, apart from existing Westinghouse default card.
- `Great Minds FedEx 886 F.3d 91` and `Drauglis Kappa Map` — published
  comparable Creative Commons public-license construction cases.

## Negative searches and unresolved leads

| Search/lead | Current result | Follow-up needed |
|---|---|---|
| Final merits U.S. AGPL §13 network-source judgment | None located | PACER/CourtListener full-docket audit if this proposition becomes decisive. |
| XimpleWare final disposition after 2014 orders | No final merits opinion located in public indexed materials | Obtain docket sheet/PACER documents before stating final status. |
| Fisher final disposition after trial setting | No final merits order located in reviewed primary sources | Obtain docket sheet/PACER documents. |
| BusyBox High-Gain and Verizon termination/settlement terms | Complaint and public reports, but no authenticated final order/complete terms located | PACER retrieval or counsel confirmation. |
| Neo4j Graph Foundation settlement terms | Ninth Circuit says action settled; terms not located | Do not infer relief; obtain unsealed record only if material. |
| GPL/LGPL/AGPL/MPL broad census | No material published U.S. MPL merits decision identified in this pass | Search separately by MPL text and product names if a later matter requires it. |

## Primary-source URLs reviewed

- [GovInfo — XimpleWare, No. 5:13-cv-05161, Doc. 85](https://www.govinfo.gov/content/pkg/USCOURTS-cand-5_13-cv-05161/pdf/USCOURTS-cand-5_13-cv-05161-1.pdf)
- [GovInfo — XimpleWare, No. 5:13-cv-05161, Doc. 142](https://www.govinfo.gov/content/pkg/USCOURTS-cand-5_13-cv-05161/pdf/USCOURTS-cand-5_13-cv-05161-3.pdf)
- [GovInfo — Fisher, No. 3:20-cv-00216, Doc. 129](https://www.govinfo.gov/content/pkg/USCOURTS-ohsd-3_20-cv-00216/pdf/USCOURTS-ohsd-3_20-cv-00216-4.pdf)
- [GovInfo — Wallace district order, No. 1:05-cv-00678](https://www.govinfo.gov/content/pkg/USCOURTS-insd-1_05-cv-00678/pdf/USCOURTS-insd-1_05-cv-00678-1.pdf)
- [Ninth Circuit — Neo4j order, No. 21-16029](https://cdn.ca9.uscourts.gov/datastore/memoranda/2022/03/14/21-16029.pdf)
- [FSF/Cisco complaint PDF](https://www.fsf.org/licensing/complaint-2008-12-11.pdf/view)

## Verification note

No search result, vendor statement, or settlement announcement is treated as a
court holding. Where an official court-hosted PDF was unavailable, the card
identifies the accessible docket-document mirror and narrows the proposition.
