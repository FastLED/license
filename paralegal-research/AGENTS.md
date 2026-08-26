# Agent workflow for legal research

These instructions apply throughout `paralegal-research/`. Read them before
doing legal research for this repository.

The FastLED Reciprocal License is reusable text, not a project ownership
vehicle. Keep these roles distinct in every memo and answer:

- canonical text maintainer or steward: publishes and versions license text;
- Contributor or applicable rights holder: grants rights in particular
  Covered Software;
- commercial licensor: grants separate permission only when independently
  authorized for the relevant software; and
- enforcement claimant: must establish the standing required for the
  particular claim.

Never infer software ownership, commercial-licensing authority, beneficiary
status, or enforcement standing from maintenance of this license repository.
Do not route a general license-text question into a FastLED codebase ownership
audit unless the requested scenario specifically concerns FastLED adoption or
enforcement.

Section 11.7 and Exhibit C make the generic AI Coding Agent Notice part of the
draft License and require adopters to include it. Do not classify the notice as
an optional FastLED-only policy. Separately analyze (a) the human or entity's
license condition to include the notice and (b) whether any sentence addressed
to an automated agent could create obligations or remedies beyond the express
text.

Read `TAXONOMY.md` before assigning metadata or describing the weight of an
authority. For systematic research, use `templates/SEARCH-LOG.md` and preserve
negative searches and unresolved leads.

## 1. Route the question before researching

Normalize the request into five fields:

- **actor** — licensor, copyright owner, contributor, distributor, service
  operator, customer, or other claimant/defendant;
- **conduct or trigger** — distribution, remote network use, missed source
  publication, notice omission, post-termination conduct, or another event;
- **jurisdiction** — country, court system, and state law when relevant;
- **issue or remedy** — liability, standing, injunction, damages, cure,
  specific performance, evidence, or procedure;
- **time/version** — relevant license version, product release, and date.

Then read `ANSWERING-GUIDE.md`, route through `PROPOSITION-MAP.md`, and
check `INDEX.md` plus `authorities/INDEX.md` before creating anything. Read
`COVERAGE.md` when the question touches a known gap. Start with:

```console
rg -n -i "<key phrase>|<synonym>|<case>|<statute>" paralegal-research LICENSE LEGAL-REVIEW.md README.md
```

Search synonyms as well as the user's wording. For example, search `source
disclosure`, `corresponding source`, `specific performance`, `injunction`, and
`cure` for a request framed as “make the infringer publish.”

## 2. Decide whether the question is already answered

Read the candidate memo's scope, short answer, assumptions, open questions,
and `last_verified` date. Classify the request as follows:

- `answered` — the memo covers the same material actor, conduct, jurisdiction,
  remedy, and license version; its authorities remain current; and no open
  point would materially change the answer.
- `partial` — the memo is analogous, but a different jurisdiction, claimant,
  license clause, procedural posture, or unresolved fact matters.
- `unresearched` — no memo addresses the material question.
- `superseded` — a newer memo expressly replaces the old one.

Do not create a duplicate memo merely because the phrasing differs. Update the
existing memo when the legal question is materially the same. Create and
cross-link a child or related matter when the difference could change the
answer. A memo may become stale without changing its `research_status`; update
`last_verified` only after checking all time-sensitive authorities.

Allowed frontmatter values are:

- `research_status`: `unresearched`, `in-progress`, `partial`, `answered`, or
  `superseded`.
- `legal_review`: `not-requested`, `pending`, `approved`, or
  `changes-required`.

## 3. Research in authority order

Prefer sources in this order:

1. Operative repository text and version history.
2. Statutes, regulations, court opinions, orders, and dockets.
3. Official license text and materials from the canonical text publisher or
   steward, remembering that this role does not establish rights in software
   governed by the text.
4. Reputable secondary legal analysis for context and leads.
5. Community posts or anonymous material only as leads to stronger sources.

For technical legal questions, use primary authority for the final proposition
whenever available. Record the court, jurisdiction, date, procedural posture,
precedential weight, direct URL, and verification date.

Never collapse these categories:

- a court's holding;
- a party's allegation or requested relief;
- a settlement term;
- a default judgment;
- dicta or commentary;
- an inference from multiple sources.

If a complaint asks for source disclosure, that does not prove a judge ordered
it. If parties settle on publication, that does not establish a generally
available judicial remedy. State those limits in the memo and authority card.

## 4. File the result

Use `templates/MATTER.md` for a new question and assign the next `PR-####` ID.
Use `templates/AUTHORITY.md` and the next `AUTH-####` ID when a source is
nuanced, likely to be reused, or important to the answer. A routine source can
remain in a matter's source table.

File matters by their primary issue, not by the name of the person asking:

- `matters/remedies/`
- create another lowercase topic folder only when needed, such as `standing/`,
  `scope/`, `registration/`, or `procedure/`.

File reusable authority cards by source type:

- `authorities/cases/`
- `authorities/statutes/`
- `authorities/licenses/`

Every completed research pass must:

1. update the canonical matter rather than only a chat or issue;
2. add or update authority cards where warranted;
3. update `INDEX.md` for matters and `authorities/INDEX.md` for reusable
   authorities in the same change;
4. link related and superseded matters in both directions;
5. state facts, assumptions, contrary authority, uncertainty, and open
   questions;
6. use absolute dates and set `last_verified` to the actual verification date;
7. distinguish a descriptive conclusion from a recommendation;
8. leave the license text unchanged unless drafting was expressly requested.

For a concurrent research swarm, the coordinator may reserve non-overlapping
ID ranges. Each research agent writes only its assigned matter drafts and
authority cards. The coordinator alone updates shared indexes, deduplicates
authorities, and performs the final cross-link pass.

## 5. GitHub and external actions

Repository memos are canonical. If the user asks for an issue, create one with
a concise summary, scope limits, open questions, and a link to the memo once
the memo is available. Add the issue URL to the memo. Do not open issues,
contact counsel, publish findings, or change external systems without user
authorization.

## 6. Quality gate

Before declaring a matter answered, verify:

- the short answer responds to the normalized question;
- every important proposition has a direct, accessible source;
- requested relief is not described as awarded relief;
- current cases and statutes were checked recently;
- holdings are separated from settlements and commentary;
- every new `PR-####` and `AUTH-####` identifier appears in its canonical
  index and is not duplicated;
- the memo explains what would change the answer;
- local links resolve and `git diff --check` passes;
- legal review is not implied unless `legal_review: approved` is supported by
  an identified attorney review.
