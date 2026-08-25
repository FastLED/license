# Issue #17 coverage audit

> Audit date: 2026-08-25. Preliminary paralegal research for attorney review,
> not legal advice, a license recommendation, an enforcement decision, or a
> change to `LICENSE`.

This is an information-architecture and completeness audit against
[issue #17](https://github.com/FastLED/license/issues/17). It records the
working-tree corpus visible on the audit date. Matter memos and authority cards
remain the canonical research records; this report does not add merits research.

## Executive assessment

The corpus now has PR-0001 through PR-0020, five reproducible research logs,
and 102 indexed authority cards: 60 cases, 32 license-related texts, and 10
statutes, rules, guidance, or settlement records. It substantially covers the
issue's routing and doctrine architecture. Its legal coverage is intentionally
uneven: many doctrine matters are `partial`, all remain attorney-review
pending, on-point AGPL network-only remedies are unresolved, and comparative
material has important primary-source and translation limits.

Retrieval integration is complete: [INDEX.md](INDEX.md) enumerates every
matter, [the authority index](authorities/INDEX.md) enumerates every reusable
card, and [PROPOSITION-MAP.md](PROPOSITION-MAP.md) routes common questions and
synonyms to the smallest useful research set.

## Matter coverage

| Area | Matter IDs | Recorded coverage / confidence | Material limit |
|---|---|---|---|
| Baseline remedies | [PR-0001](matters/remedies/agpl-noncompliance-judicial-remedies.md) | Answered; U.S./California AGPL-style remedies baseline | Not a final AGPL §13 network-only remedy record; source performance and paid license are not automatic remedies |
| License text and status | [PR-0002](matters/license-comparison/copyleft-source-availability-license-landscape.md) | Partial; official-text comparison of the issue's minimum family set | Exact version, exception, technical boundary, and jurisdiction remain controlling |
| U.S. and international censuses | [PR-0003](matters/case-census/us-open-source-license-enforcement-census.md), [PR-0004](matters/case-census/international-open-source-license-enforcement-census.md) | Partial; posture-aware census with search logs | Not exhaustive; several docket, finality, official-copy, and translation gaps |
| Formation, copyright route, and claimant | [PR-0005](matters/doctrine/public-license-formation-and-assent.md)--[PR-0008](matters/doctrine/ownership-standing-and-third-party-beneficiaries.md) | Partial, generally medium confidence | State law, assent evidence, copyright nexus, ownership, assignment, and beneficiary status are fact/forum-specific |
| Scope and triggers | [PR-0009](matters/scope/covered-work-derivative-linking-and-source-scope.md), [PR-0010](matters/scope/distribution-network-use-and-deployment-triggers.md) | Partial; PR-0009 low and PR-0010 medium confidence | No universal linking result; no located final U.S. AGPL §13 network-only merits remedy |
| Termination and remedies | [PR-0011](matters/remedies/termination-notice-cure-reinstatement-and-past-liability.md)--[PR-0015](matters/defenses/open-source-enforcement-defenses-and-remedial-limits.md) | Partial; PR-0014 high for its statutory timing question, others medium | State equitable/contract law, actual proof, cure timing, and comparability remain decisive |
| Evidence, procedure, supply chain, settlement | [PR-0016](matters/evidence/evidence-preservation-version-attribution-and-source-availability.md)--[PR-0019](matters/remedies/settlement-compliance-and-post-judgment-structures.md) | Answered as U.S.-focused issue-spotting frameworks; medium confidence | They do not decide a particular artifact, forum, actor, order, or confidential-source disclosure |
| Cross-border framework | [PR-0020](matters/procedure/comparative-and-cross-border-enforcement.md) | Answered framework, low confidence | Country-specific merits, procedure, recognition, and translation are not interchangeable |

## Acceptance-criteria audit

| Issue #17 criterion | Assessment | Evidence and residual gap |
|---|---|---|
| Preserve/reuse PR-0001 and AUTH-0001--0008 | Covered | PR-0001 remains canonical and the censuses reuse the original cards. Their scope is still narrow and attorney review is pending. |
| Search logs with scope, negative results, and leads | Covered | [U.S. log](search-logs/us-case-census-2026-08-25.md), [international log](search-logs/international-case-census-2026-08-25.md), and [license log](search-logs/license-landscape-2026-08-25.md). No duplicate fresh search was performed for this audit. |
| Minimum license set, official cards, normalized comparison | Covered for text/status | [PR-0002](matters/license-comparison/copyleft-source-availability-license-landscape.md), its official-text cards, and the license-gap search log cover the specified minimum set plus additional historical, deployment, source-available, and open-hardware comparators. |
| Case cards separate posture, relief, limits, history, source, and date | Substantially covered; incomplete source access | Census cards and authority cards distinguish the categories, but several foreign originals and U.S. dockets/finality records remain unavailable or unchecked. The separate case-gap audit lane is pending integration. |
| Never conflate complaint, interlocutory ruling, default, settlement, and holding | Covered in architecture | PR-0003, PR-0004, PR-0012, and PR-0019 expressly route these separately. Application still requires opening the specific card. |
| Sixteen doctrine topics have scoped memos, assumptions, limits, and counsel questions | Covered | PR-0005--PR-0020 supply the requested topic set. Fourteen of the twenty total matters are `partial`; scoped coverage is not a final merits answer. |
| Distinguish U.S. copyright law from state contract/equity law | Covered as a routing requirement; incomplete for any particular state | PR-0005--PR-0008 and PR-0011--PR-0015 identify the distinction. State-specific research is necessarily forum-dependent. |
| Comparative primary sources and translation provenance | Partial | Strongest accessible records include CJEU, French cassation/remand, and Dutch material. German, Chinese, Korean, and some French material has source or translation limits below. |
| No automatic source-publication or commercial-license remedy claim | Covered | PR-0001, PR-0003, PR-0010, PR-0012, and PR-0019 preserve the limit. **AGPL §13 network-only relief is unresolved.** |
| Separate open-source and source-available classifications | Covered | PR-0002 classifies instruments separately; source access/use restrictions do not become copyleft by analogy. |
| Unique, indexed, cross-linked, machine-searchable IDs | Covered | [INDEX.md](INDEX.md) lists PR-0001--PR-0020 and [the authority index](authorities/INDEX.md) lists every reusable authority card by stable identifier. All cards expose normalized posture, weight, license/topic, source-quality, source-URL, language, and translation metadata. |
| Local links resolve and whitespace checks pass | Covered | Repository-wide validation found no broken local Markdown links, trailing whitespace, extra blank lines at EOF, duplicate identifiers, or unindexed matter/authority records. `git diff --check` passes. |
| Attorney-review gate and no `LICENSE` change | Covered | All matter frontmatter remains pending review; this audit changes no license text. |
| Final coverage report | Covered | This document, read with [PROPOSITION-MAP.md](PROPOSITION-MAP.md). |

## Inaccessible sources, translations, and jurisdiction limits

- **Germany:** Sitecom, D-Link, Skype, and Fantec have uneven public primary
  copies; some records depend on reproductions, portals, or summaries. Exact
  relief and scope need court-certified text/docket confirmation.
- **France:** the 2019 first-instance Entr'Ouvert record has secondary/index
  access limits; the 2024 Paris remand appeal's finality and dispositive
  details require current French-original checking.
- **China and South Korea:** available official summaries/reports or original
  decisions do not remove the need for full judgments and qualified/certified
  translation when wording is material. Party/docket anonymity also limits
  attribution in the Chinese materials.
- **Italy, Spain, and the United Kingdom:** the recorded searches did not
  retrieve an authenticated, accessible reciprocal-license merits decision for
  a card. This is a bounded negative result, not proof of no law or case.
- **United States:** XimpleWare and Fisher final dispositions, selected BusyBox
  settlement terms, and Neo4j/Graph Foundation terms need docket/unsealed-record
  verification if material. U.S. federal rules do not supply every state's
  contract, equity, limitations, or beneficiary law.
- **Every foreign route:** a foreign decision, treaty, or translation does not
  itself answer forum, choice of law, service, provisional relief, recognition,
  or enforcement in another country.

## Questions reserved for counsel

1. Select the target forum(s), governing law, license version, claimant, and
   requested remedy before relying on an analogy.
2. Confirm per-component ownership, assignments, contributor authority,
   registration, and the evidence needed to attribute a relevant product and
   version.
3. Decide whether a contract/beneficiary theory exists and whether state-law
   specific performance or other affirmative relief is available.
4. Obtain qualified translations and local-law review where a non-English
   source could materially change advice or a filing.
5. Decide whether the unresolved AGPL §13 network-only question requires a
   docket-level PACER/CourtListener audit in a selected forum rather than
   distribution-case analogy.
6. Define the refresh cadence and the facts that require a new scoped matter
   before deploying the corpus as an AI retrieval source.

## Stale-source triggers

Recheck a matter when its exact license text, OSI/steward status, docket,
appeal/finality, statute/rule, governing state law, foreign translation, or
technical/deployment facts change. All visible current matter and authority
records report `last_verified: 2026-08-25`; that date is not attorney approval
and does not eliminate a targeted current-law check.

## Integrated gap-audit result

The completed license-gap audit added historical, network/deployment,
source-available, project-specific, and open-hardware comparators. The
completed case-gap audit added four usable decisions and preserved excluded or
inaccessible leads in its search log. These additions narrow the known gaps;
they do not make the census exhaustive or remove the attorney-review gate.
