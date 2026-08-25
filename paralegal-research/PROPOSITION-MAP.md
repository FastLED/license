# Proposition map

> Preliminary research-navigation aid for attorney review; not legal advice,
> a license recommendation, or an enforcement decision. Matter memos remain
> the canonical research records. FastLED is a comparison target only.

## Route before reading authorities

Capture the actor, conduct/trigger, jurisdiction (including state law where
material), exact license and version, relevant dates, requested remedy, and
technical facts. Then read the linked matter memo, its assumptions, status,
open questions, and verification date before using individual cards. A license
text describes an obligation; it does not by itself establish assent, standing,
infringement, or a remedy.

**Status key.** `partial` means an analogous or incomplete record, not a
default answer. All current matters remain `legal_review: pending`. Every
route also requires the stale-source check in the last column.

| Common question and useful synonyms | Start with canonical matter(s) | Authority categories to load next | Facts that cannot be assumed | Recheck before relying |
|---|---|---|---|---|
| Which license family is this? Is it open source, source available, or file-level copyleft? `classification`, `OSI`, `license comparison`, `compatibility` | [PR-0002](matters/license-comparison/copyleft-source-availability-license-landscape.md) | Exact official license card; OSI registry or steward status; exact-version judicial treatment | Exact instrument/version, exceptions, dual-license election, release date | Official text, OSI/steward status, compatibility lists, new exact-version decision |
| What cases exist? Was a case a holding, complaint, order, default, or settlement? `case census`, `enforceability`, `docket` | [PR-0003](matters/case-census/us-open-source-license-enforcement-census.md) (U.S.); [PR-0004](matters/case-census/international-open-source-license-enforcement-census.md) (non-U.S.) | Official opinion/order/docket; authority-card posture and later history; settlement record | Forum, clause, license version, procedural posture, actual disposition | Docket/finality, appeal, unsealed settlement, later decision, official copy |
| Did a public license form a contract, and who accepted it? `assent`, `formation`, `clickwrap`, `parties` | [PR-0005](matters/doctrine/public-license-formation-and-assent.md) | State contract law; formation/assent cases; exact notice and acceptance mechanism | Recipient/actor, notice, manifestation of assent, selected law, text/version | Current controlling state law, forum/law clause, changed interface/notice record |
| Is a breached term a copyright condition or only a contract covenant? `license scope`, `copyright nexus`, `condition versus covenant` | [PR-0006](matters/doctrine/copyright-condition-versus-contract-covenant.md); [PR-0007](matters/doctrine/copyright-preemption-and-nexus.md) | Copyright statutes; binding circuit condition/covenant and preemption cases; exact license card | Exclusive-right act, clause wording, nexus, assent, state claim's extra element | Selected circuit/state law, subsequent controlling authority, exact clause/version |
| Who owns the work and may sue or demand performance? `standing`, `assignment`, `contributor`, `steward`, `beneficiary` | [PR-0008](matters/doctrine/ownership-standing-and-third-party-beneficiaries.md) | Ownership/assignment statutes and cases; contributor agreements; beneficiary-law authority | Per-component chain of title, exclusive-right transfer, claimant role, governing law | Current ownership/registration records, assignments, state beneficiary law |
| Does code/linking/containerization make a covered or derivative work, and what source is required? `linking`, `aggregation`, `Corresponding Source`, `scope` | [PR-0009](matters/scope/covered-work-derivative-linking-and-source-scope.md) | Exact license definitions; derivative-work authority; technical evidence | Files/code copied, architecture, build/relink path, symbols, delivery form, exceptions | Exact dependency/build/source tree; controlling jurisdiction; new linking authority |
| Did distribution, conveyance, SaaS, network use, or deployment trigger an obligation? `hosted`, `remote access`, `AGPL`, `SSPL`, `RPL`, `External Deployment` | [PR-0010](matters/scope/distribution-network-use-and-deployment-triggers.md) | Exact license trigger card; on-point disposition; condition/covenant authority | Modified versus unmodified program, copies/conveyance, users/audience, service architecture, entity/affiliate facts | Official license text and any newly final on-point case; product/version and deployment facts |
| **AGPL §13 network-only use: can a court enforce it or order source?** `remote interaction`, `AGPL source offer`, `network-only` | [PR-0010](matters/scope/distribution-network-use-and-deployment-triggers.md), then [PR-0001](matters/remedies/agpl-noncompliance-judicial-remedies.md) and [PR-0003](matters/case-census/us-open-source-license-enforcement-census.md) | GNU AGPL-3.0 text; binding forum-specific nexus/remedy authority; final AGPL §13 merits disposition if located | Modified AGPL program, actual remote interaction, users, whether copies were conveyed, claimant/standing, requested theory and remedy | **Unresolved:** no located final U.S. merits ruling supplies an AGPL §13 network-only remedy. Recheck full dockets, final decisions, governing state law, and current AGPL text; do not borrow GPL distribution cases as the answer. |
| Did termination, cure, reinstatement, notice, or later compliance restore rights or erase earlier exposure? `cure`, `reinstatement`, `past liability` | [PR-0011](matters/remedies/termination-notice-cure-reinstatement-and-past-liability.md) | Exact termination/cure text; timing evidence; governing remedy/defense law | Version, breach/knowledge/notice dates, first/repeat violation, later conduct | Current license text, notice and cure timeline, controlling state/federal law |
| Can a court stop conduct, impound copies, require source, enforce a judgment, or hold someone in contempt? `injunction`, `specific performance`, `source disclosure`, `discovery`, `contempt` | [PR-0012](matters/remedies/injunction-specific-performance-impoundment-and-contempt.md) | Copyright remedies statutes; equitable-remedy and procedure authority; state specific-performance law | Claim and standing, infringement versus contract theory, requested relief, feasibility/supervision, existing order | Current statute/rules, selected state equitable law, docket/order text, later compliance |
| Can the owner recover a commercial-license price, damages, profits, fees, or statutory damages? `reasonable royalty`, `dual license`, `commercial license`, `fees` | [PR-0013](matters/remedies/damages-profits-fees-and-commercial-license-valuation.md); [PR-0014](matters/registration/copyright-registration-limitations-and-accrual.md) | Copyright remedies/registration statutes; damages and fee cases; comparable transaction evidence | Registration dates, work nationality, infringement dates, comparable licenses, causation/apportionment, contract claim | Current statutes/cases, registration record, limitations/accrual dates, actual comparable transactions |
| Is the claim blocked or limited by authorization, waiver, estoppel, misuse, unclean hands, impossibility, mootness, or disclaimers? `defenses`, `voluntary cessation` | [PR-0015](matters/defenses/open-source-enforcement-defenses-and-remedial-limits.md) | Exact grant/termination text; defense elements in governing forum; remedy authority | Scope of permission, notices/representations, reliance, later conduct, requested claim/remedy | Governing state law, later conduct, release/settlement, current equitable precedent |
| How can public code, binaries, version history, notices, and source availability be preserved or attributed? `evidence`, `hash`, `chain of custody`, `binary comparison` | [PR-0016](matters/evidence/evidence-preservation-version-attribution-and-source-availability.md) | Evidence/procedure rules; official preservation guidance; authenticated artifact records | Lawful acquisition, capture time/method, version identity, hashes, handlers, provenance | Current rules/local practice, source availability, relevant repository/product version |
| Where may a claim be brought and can source be obtained in discovery? `jurisdiction`, `venue`, `choice of law`, `protective order` | [PR-0017](matters/procedure/pleading-jurisdiction-venue-choice-of-law-and-discovery.md) | Jurisdiction/venue statutes; local rules; discovery/protective-order authority | Parties' contacts, territorial acts, claims, clauses, registration, discovery target | Current local rules/case law, forum clause, docket posture, confidentiality facts |
| Which supply-chain actor is responsible: manufacturer, OEM, reseller, customer, or service provider? `secondary liability`, `downstream`, `reseller` | [PR-0018](matters/supply-chain/downstream-recipients-manufacturers-resellers-and-secondary-liability.md) | Exclusive-right statutes; direct/secondary-liability cases; exact license/contract | Who copied, compiled, flashed, imported, distributed, controlled, knew, or induced; transaction timeline | Current circuit doctrine, contracts/agency facts, technical provenance and transfer evidence |
| Is a source release, payment, audit, or commercial license a settlement term or a judicial remedy? `consent decree`, `compliance`, `post-judgment` | [PR-0019](matters/remedies/settlement-compliance-and-post-judgment-structures.md); [PR-0012](matters/remedies/injunction-specific-performance-impoundment-and-contempt.md) | Settlement/consent-decree text; final order; procedural enforcement rules | Whether there is a negotiated agreement, entered order, bound person, and clear obligation | Unsealed terms, finality, enforcement jurisdiction, order modification/history |
| What changes outside the United States? `foreign judgment`, `France`, `Germany`, `EU`, `translation`, `cross-border` | [PR-0020](matters/procedure/comparative-and-cross-border-enforcement.md), then [PR-0004](matters/case-census/international-open-source-license-enforcement-census.md) | Country-specific primary law/court material; conflicts/recognition law; qualified translation | Territorial acts, selected forum/law, assets, service, local procedure, original-language text | Official/full judgment, finality, certified or qualified translation, local counsel, current treaty/national law |

## Mandatory distinctions

- **Open-source is not source-available.** Use the exact classification in
  [PR-0002](matters/license-comparison/copyleft-source-availability-license-landscape.md).
  Do not infer a reciprocal disclosure duty from source access or a use
  restriction.
- **Requested relief, awarded relief, default relief, and settlement terms are
  different propositions.** Route to [PR-0003](matters/case-census/us-open-source-license-enforcement-census.md),
  [PR-0004](matters/case-census/international-open-source-license-enforcement-census.md),
  [PR-0012](matters/remedies/injunction-specific-performance-impoundment-and-contempt.md),
  and [PR-0019](matters/remedies/settlement-compliance-and-post-judgment-structures.md)
  as appropriate.
- **FastLED is not a default answer.** Its release candidate is a comparison
  card in [PR-0002](matters/license-comparison/copyleft-source-availability-license-landscape.md).
  It is not adopted, attorney-approved, OSI-approved, or judicially tested.

## Integration status

This map routes the complete PR-0001--PR-0020 working corpus. Use the canonical
[matter index](INDEX.md) and [authority index](authorities/INDEX.md) for stable
identifiers. The completed license-gap and case-gap audits are incorporated in
PR-0002 through PR-0004 and their linked search logs.
