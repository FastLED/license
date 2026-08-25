# Paralegal AI answering guide

This is the retrieval and answer contract for an agent using this research
library. It does not authorize legal advice, external communications,
enforcement, or license drafting.

## Load the smallest sufficient context

1. Normalize the question using `AGENTS.md` and `TAXONOMY.md`.
2. Read `INDEX.md` and the proposition map referenced there.
3. Read the most specific matter memo before individual authorities.
4. Open only the authority cards needed to verify the answer and its limits.
5. Recheck pending cases, current statutes, official license status, and stale
   verification dates before relying on them.

Do not load the entire corpus by default. Broad context can hide a controlling
jurisdiction or procedural-posture difference.

## Separate the layers of an answer

Every substantive answer should distinguish:

1. **Question and assumed facts** — actor, conduct, jurisdiction, exact license
   and version, relevant dates, and requested remedy.
2. **License text** — what the instrument says, without calling it enforceable
   merely because it is written.
3. **General legal rule** — statute or binding authority in the relevant forum.
4. **Analogous authority** — persuasive decisions involving another license,
   jurisdiction, or procedural posture.
5. **Application** — a conditional analysis of the supplied facts.
6. **Uncertainty** — missing facts, splits, negative searches, pending cases,
   translations, and issues requiring counsel.
7. **Status** — research status and legal-review status are separate.

Use “holding,” “requested relief,” “awarded relief,” “settlement term,” and
“inference” precisely as defined in `TAXONOMY.md`.

## High-risk answer patterns

### “Can a judge make them release the source?”

Separate:

- an injunction stopping unlicensed copyright conduct;
- specific performance or a mandatory injunction requiring source delivery;
- confidential source production in discovery;
- a negotiated source-publication settlement; and
- enforcement of an existing judgment or consent decree.

Do not turn one category into another.

### “Can they be forced to buy a commercial license?”

Separate voluntary licensing and settlement from damages valuation. A
commercial-license price may be evidence under an applicable damages theory;
that does not itself create assent or empower a court to impose the contract.

### “Does this license cover the whole product?”

Do not answer from license-family labels such as “strong copyleft” or
“file-level.” Retrieve the exact license/version and analyze the actual work,
files, linking, copying, distribution/deployment, source definition, exceptions,
and governing jurisdiction.

### “Did this case prove the license is enforceable?”

Identify the exact clause, claim, posture, holding, remedy, jurisdiction, and
later history. A claim surviving dismissal, a default judgment, or a settlement
does not establish the same proposition as a final contested appellate ruling.

## Application to a project-specific license

Answer the general doctrine first. Then compare the project's exact clause to
the authority and identify every textual or factual difference that could
change the result. A custom license should not inherit GPL, AGPL, MPL, or
source-available case outcomes merely by analogy.

For the FastLED draft specifically, preserve the attorney gate in
`../LEGAL-REVIEW.md`; do not describe the release candidate as adopted,
attorney-approved, OSI-approved, or judicially tested.

## Output format

Prefer this compact structure:

```text
Question and assumptions
Short answer
Controlling rule and authority
Analogous authority and its posture
Application
What could change the answer
Counsel-review questions
Research/legal-review status
```

Link to the canonical matter memo and direct primary authority. Avoid long
quotations and do not present an agent's prediction as a legal determination.
