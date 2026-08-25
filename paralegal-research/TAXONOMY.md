# Research taxonomy

Use this controlled vocabulary when indexing legal research. The purpose is to
let an agent retrieve by legal proposition and procedural weight instead of
matching only the words in a question.

## Research unit

- **Matter memo** — answers one normalized legal question.
- **Authority card** — records what one source supports and does not support.
- **License card** — authority card for one identified license and version.
- **Case census** — routes to case cards; it is not a substitute for them.
- **Search log** — makes the research boundary and negative searches auditable.

## Required routing dimensions

Every matter should identify:

- `actors`: copyright owner, contributor, steward, exclusive licensee,
  distributor, modifier, service operator, recipient, customer, association,
  manufacturer, reseller, or other material role;
- `conduct`: reproduce, modify, prepare derivative work, distribute, convey,
  transfer, deploy, provide network access, omit notice, withhold source,
  remove source, cure, or continue after termination;
- `jurisdictions`: country, court system, circuit/state when material, and
  governing contract law;
- `licenses`: exact name and version, never merely “GPL-like”;
- `doctrines`: formation, condition-covenant, copyright-nexus, preemption,
  ownership, standing, scope, termination, registration, limitations,
  defenses, evidence, procedure, or conflicts;
- `remedies`: prohibitory-injunction, mandatory-injunction,
  specific-performance, source-disclosure, impoundment, destruction, actual-
  damages, profits, statutory-damages, fees, declaratory-relief, contempt, or
  settlement-only terms;
- `time`: license version date, conduct dates, decision date, and verification
  date.

## Authority types

Use one of:

- `case`
- `statute`
- `regulation`
- `license`
- `license-condition`
- `license-draft`
- `settlement`
- `administrative-material`
- `official-guidance`
- `secondary-source`

Use `license-condition` when the text is an add-on to another license rather
than a complete standalone grant. Use `license-draft` for an unadopted draft;
that label is a status warning, not a prediction about enforceability. An
announcement about a settlement remains `settlement`, even when published by
a party or respected organization.

## Case posture

Use the most specific applicable value:

- `complaint`
- `temporary-restraining-order`
- `preliminary-injunction`
- `motion-to-dismiss`
- `judgment-on-pleadings`
- `summary-judgment`
- `trial-judgment`
- `default-judgment`
- `appellate-merits`
- `appellate-procedural`
- `settled`
- `dismissed-without-merits`
- `not-applicable` — non-case authorities only

If one card covers several decisions, record the posture of each decision in a
procedural-history table rather than assigning the strongest label to the
entire litigation.

## Precedential weight

- `binding` — binding in the stated forum on the stated proposition.
- `persuasive-published` — published but not binding in the target forum.
- `persuasive-trial` — reasoned trial-level ruling.
- `nonprecedential` — designated unpublished or nonprecedential.
- `default-only` — relief entered without contested merits adjudication.
- `none-settlement` — party agreement, not judicial authority.
- `none-allegation` — party position only.
- `not-applicable` — statutes, licenses, guidance, and other non-case
  authorities.

Never infer weight without naming the target jurisdiction.

## Proposition treatment

Label important propositions as:

- `holding`
- `dicta`
- `party-allegation`
- `requested-relief`
- `awarded-relief`
- `settlement-term`
- `official-license-text`
- `inference`
- `unresolved`

The same case may carry several labels. For example, a complaint may request
source publication, an interlocutory order may let the claim proceed, and a
later settlement may require delivery. None of those facts alone is an
`awarded-relief` holding.

## Source and translation quality

Record:

- `source_quality`: `primary`, `official-reproduction`, `official-summary`, or
  `secondary`;
- `source_url`: a direct URL rather than a search-results page;
- `original_language`;
- `translation_status`: `not-needed`, `official`, `court-provided`,
  `researcher-translation`, or `secondary-translation`.

When only a secondary translation is available, cite the original decision as
well and avoid conclusions that depend on a disputed word without counsel or a
qualified translation.

## Confidence

- `high` — directly supported by current primary authority and no material
  contrary authority was found within the recorded search scope.
- `medium` — supported, but posture, jurisdiction, or factual analogy limits
  transfer.
- `low` — based on sparse authority, unresolved litigation, translation, or a
  reasoned inference.

Confidence describes the research record, not the likelihood of winning a
particular case.
