---
id: PR-0018
title: Downstream recipients, manufacturers, resellers, and secondary liability
question: "How do downstream-recipient, manufacturer, reseller, and secondary-liability questions differ in a license-agnostic software supply chain?"
short_answer: "The actor that directly reproduces, modifies, distributes, imports, or deploys software must be identified before applying a license condition or copyright claim. A customer, reseller, or contract manufacturer does not become directly or secondarily liable merely by appearing in a supply chain. Secondary liability requires the governing doctrine's own elements, including a direct infringement predicate where required; inducement under Grokster requires purposeful promotion, not mere product handling. Recipient source rights and direct copyright claims are separate questions."
research_status: answered
legal_review: pending
jurisdictions: [US-federal, US-state]
licenses: []
actors: [copyright-owner, contributor, distributor, manufacturer, reseller, recipient, customer, service-operator]
conduct: [reproduce, modify, distribute, import, deploy, provide-network-access]
topics: [supply-chain, direct-infringement, secondary-liability, recipients, manufacturers, resellers]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0016, PR-0017, PR-0019]
supersedes: []
---

# PR-0018: Downstream recipients, manufacturers, resellers, and secondary liability

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

This U.S.-focused memo addresses actor mapping in a mixed hardware/software
supply chain. It assumes an exact license and version will be supplied later;
it does not assume the license treats all transfers, making, hosted access,
resale, or recipient rights identically. It does not decide agency,
indemnification, exhaustion, product-liability, import, contract, or foreign
law issues. "Manufacturer" can mean an entity assembling to instruction,
designing a product, flashing firmware, or selling under its own mark—facts
that must not be collapsed.

## Short answer

Start with a transaction-and-copy map. Direct copyright analysis asks who
performed an exclusive-right act under 17 U.S.C. § 106 and without applicable
permission; license analysis separately asks which actor received permission,
accepted conditions, and took the conduct named in the exact text. A reseller
that merely transfers a finished product, a contract manufacturer that makes or
flashes copies, and a customer that uses a product can occupy materially
different positions.

Secondary liability is not a shortcut around missing direct facts. Under
*Grokster*, inducement requires distribution with an object of promoting
infringement, shown by clear expression or affirmative steps; the case is not
a rule that every reseller/manufacturer is liable for a downstream breach.
Recipient claims to source or notice may rest on the particular license and,
where asserted, contract/beneficiary theory; they are not automatically the
copyright owner's direct claim.

## Analysis

### Map copies, control, and contractual roles

For every relevant version, identify: source provider; party that compiled,
flashed, or embedded it; party that imported or distributed each product; party
that advertised/provided any source; recipient; and any service operator.
Record dates, jurisdictions, transfer documents, instructions, and which party
controlled the relevant act. Do not infer that an OEM brand owns source code or
that a retailer made the embedded copy without evidence.

Section 106 identifies exclusive rights; [AUTH-0006](../../authorities/statutes/us-copyright-remedies.md)
addresses remedies once a claim exists. The condition/covenant analysis in
[AUTH-0001](../../authorities/cases/jacobsen-v-katzer.md) and
[AUTH-0002](../../authorities/cases/mdy-industries-v-blizzard.md) underscores
why exact language and copyright nexus matter. Those cases do not decide a
particular physical supply chain.

### Separate direct from secondary claims

Direct liability asks whether the defendant itself committed a legally relevant
act. Inducement, contributory, vicarious, agency, and joint-liability theories
have distinct elements that vary by doctrine and circuit. *Grokster* supplies
one binding inducement rule, but it involved peer-to-peer software distribution
and users' alleged infringement, not license compliance in a product channel.
[AUTH-0114](../../authorities/cases/mgm-v-grokster-secondary-liability.md).

The required predicate direct infringement, knowledge, material contribution,
control/financial benefit, intent, causal connection, and defenses should be
kept in separate columns. Contractual responsibility, indemnity, and a product
specification may be relevant facts, but they do not automatically establish a
copyright secondary-liability theory.

### Recipients are not interchangeable with owners

A recipient can be evidence source, licensee, customer, or asserted contract
beneficiary. Its ability to obtain or demand source depends on the text,
assent/beneficiary law, and remedy. In *SFC v. Vizio*, the public record
illustrates a third-party-beneficiary/specific-performance theory but not an
adjudicated general recipient right. [AUTH-0005](../../authorities/cases/sfc-v-vizio.md).

## Scenario matrix

| Actor/fact pattern | Direct question | Secondary/recipient question | Main uncertainty |
|---|---|---|---|
| Contract manufacturer flashes firmware | Did it reproduce/modify/distribute and under whose permission? | Agency/contract allocation may matter | Actual instructions and control |
| Brand owner sells product | Did it distribute relevant copies or direct others? | Knowledge/control and product chain | Identity/version of embedded code |
| Retail reseller transfers sealed goods | Did it make a copy or accept an obligation? | Mere resale is not inducement by itself | License text and role facts |
| End user receives device | Did it exercise an exclusive right? | May have recipient/contract theory | Text and governing state law |
| Platform/service provider | What acts did it itself perform? | Inducement/contributory/vicarious elements | Specific conduct and control |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0114](../../authorities/cases/mgm-v-grokster-secondary-liability.md) | Supreme Court inducement standard | Not a reseller or GPL case |
| [AUTH-0001](../../authorities/cases/jacobsen-v-katzer.md) | License conditions can be copyright-relevant | Exact wording and law matter |
| [AUTH-0002](../../authorities/cases/mdy-industries-v-blizzard.md) | Ninth Circuit condition/copyright-nexus framework | Circuit-specific framework |
| [AUTH-0005](../../authorities/cases/sfc-v-vizio.md) | Recipient contract theory pleaded | Pending; no final remedy |
| [AUTH-0055](../../authorities/cases/welte-v-d-link.md) | Foreign device-distribution enforcement record | Source/posture limits stated in card |

## Research checklist for counsel review

- Build a per-version map of code provenance, copies, transfers, control,
  contractual roles, locations, and recipients.
- Identify exact rights holder(s), license(s), assenting party/parties, and the
  condition/covenant language before assigning responsibility.
- Test direct infringement first; list each secondary theory and all its
  governing-jurisdiction elements separately.
- Treat recipient entitlement, warranty/indemnity, agency, exhaustion, and
  supplier contract claims as distinct analyses.
- Preserve lawful sales, packaging, notices, build/flash records, and public
  source-access evidence without treating them as conclusive attribution.

## What would change the answer

- Exact license terms, selected jurisdiction, copy/transfer map, agreements,
  technical control, intent evidence, or foreign distribution facts.

## Open questions for counsel

- Which actors own or control the relevant copyrights and which actually made
  each relevant copy or transfer?
- Whether a target jurisdiction recognizes the asserted secondary or recipient theory.
- Whether manufacturing/resale agreements alter agency, indemnity, or other claims.

## Repository implications

No license carve-out or enforcement policy follows from this general analysis.
Any project-specific manufacturer/reseller terms require separate review.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial research for issue #17 | Agent; attorney review pending |
