---
id: PR-0006
title: Copyright conditions versus contract covenants
question: "When does breach of a public-license term exceed copyright permission rather than create only a contract claim?"
short_answer: "There is no universal label-driven answer. In the Ninth Circuit, a restriction must limit the scope of permission and bear the required nexus to an exclusive copyright right to support infringement; an independent covenant ordinarily supports contract relief. Other circuits use their own contract and license-construction rules. GPL-family source/conveyance terms have a closer textual connection to reproduction/distribution than network-only or operational promises, but that is an inference requiring clause-, act-, and forum-specific analysis."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, US-Ninth-Circuit, US-Second-Circuit, European-Union]
licenses: [GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, source-available]
actors: [copyright-owner, contributor, distributor, service-operator, recipient]
conduct: [reproduce, modify, distribute, convey, provide-network-access, omit-notice, withhold-source]
topics: [condition-covenant, copyright-nexus]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0001, PR-0005, PR-0007, PR-0009, PR-0010]
supersedes: []
---

# PR-0006: Copyright conditions versus contract covenants

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: an owner asserting infringement or a contracting party asserting breach.
Trigger: a claimed failure to comply while reproducing, modifying, conveying,
distributing, or providing network access. The central U.S. framework is the
Ninth Circuit's; EU material is limited to the CJEU software-license rule. This
memo does not decide a remedy, termination, or the construction of a particular
release.

## Short answer

*Jacobsen* held that the Artistic License terms before it could be conditions
of copyright permission. *MDY* holds in the Ninth Circuit that a licensee
infringes only by violating a condition that limits the grant's scope and has a
copyright nexus; independent covenants are contractual. *Graham* is contrary
in application only, not a conflicting rule: the Second Circuit treated unpaid
royalties as a covenant on that text, while leaving possible rescission for
remand. The CJEU permits a copyright route for breach of a software-license
limitation concerning a reserved act, leaving classification/remedy to national
law ([AUTH-0050](../../authorities/cases/it-development-v-free-mobile.md)).

**Inference, not holding:** conveyance/distribution source and notice duties
are more readily tied to acts the owner licenses than a free-standing service,
reporting, or operational duty. AGPL §13, OSL external deployment, RPL
deployment, and SSPL §13 need especially careful nexus analysis where there is
no distribution. Explicitly calling MPL §§3.1-3.4 "conditions" is significant
textual evidence, not a universal litigation result.

## Analysis

### The controlling rule is forum and clause specific

The Ninth Circuit requires both a limiting condition and a nexus to the
copyright owner's exclusive rights; [AUTH-0002](../../authorities/cases/mdy-industries-v-blizzard.md).
*Jacobsen* treats the attribution/modification terms in the Artistic License as
conditions in its text and posture, not every open-source promise. Under
*Graham*, a licensee's nonpayment did not automatically terminate a
nonexclusive software license because the payment term was a covenant.

This means a complaint must identify (1) the exact grant, (2) conditional
language/termination machinery, (3) the defendant's act under §106, and (4)
the relation between the breached term and that act. A breach that leaves the
permission in force is ordinarily not infringement merely because it is called
material or because damages are desired.

### License texts identify different candidates; they do not decide the rule

| Family | Textual feature material to classification | Limit |
|---|---|---|
| GPL-2 | Distribution/modification terms; automatic termination §4 | No express cure and no appellate construction of each term |
| GPL-3/AGPL-3/LGPL-3 | "convey" and Corresponding Source obligations; automatic termination/reinstatement §8; AGPL §13 remote interaction | Network-only nexus unresolved in the reviewed U.S. record |
| LGPL-2.1 | Library/work-using-library conditions and distribution mechanics | Linking and technical compliance are factual |
| MPL-2 | §§3.1-3.4 expressly conditions of §2.1 grants | File boundary and state/federal claim still matter |
| EPL/CDDL/EUPL | Distribution/communication obligations plus termination/cure clauses | No exact-text controlling U.S. merits construction located |
| OSL/RPL | Conditions plus external/internal deployment vocabulary | Broad text does not create a known copyright-nexus holding |
| SSPL/source-available | Service restrictions or use restrictions may be part of permission | Exact scope, enforceability, and nexus are unresolved |

### Contrary authority and limits

Do not import *MDY* as nationwide law. *Graham* warns against converting every
license promise into infringement. *Artifex* permitted GPL contract and
copyright theories to proceed but settled before a merits decision. *Fisher*
left GPLv3 coverage, conveyance, and cure for a factfinder rather than deciding
the legal effect in the abstract. In the EU, *IT Development* concerns paid
software and Directives, not an AGPL source remedy.

## Scenario matrix

| Scenario | Likely theory | Main uncertainty |
|---|---|---|
| GPLv3 object-code conveyance without Corresponding Source | Copyright condition plausible | Ownership, covered work, cure, forum |
| AGPL program modified and used only over network | Textual §13 breach; contract/copyright theory depends | §106 nexus and remedy |
| MPL executable distribution without source access | Express condition supports copyright-scope argument | Covered file and jurisdiction |
| ELv2 hosted-service restriction | Contract/license scope argument | Meaning of managed service and nexus |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0001](../../authorities/cases/jacobsen-v-katzer.md) | Some public-license terms can condition permission | Federal Circuit applying Ninth Circuit law; PI appeal |
| [AUTH-0002](../../authorities/cases/mdy-industries-v-blizzard.md) | Ninth Circuit condition/nexus test | Binding only there; not open source |
| [AUTH-0073](../../authorities/cases/graham-v-james.md) | Covenant versus condition distinction | Binding Second Circuit; particular license |
| [AUTH-0050](../../authorities/cases/it-development-v-free-mobile.md) | EU reserved-act limitation route | CJEU interpretation, not public license |
| [AUTH-0070](../../authorities/statutes/us-copyright-subject-matter-and-preemption.md) | §106 baseline | Statute does not classify terms |

## What would change the answer

- Exact clause, grant/termination/cure text, act of copying/conveyance, and
  controlling law.
- A final GPL/AGPL/LGPL/MPL/EPL/CDDL/EUPL/OSL/RPL/SSPL merits decision.

## Open questions for counsel

- Is the intended claim infringement, contract, or both, and what forum's
  construction rule controls?
- Does the claimed breach occur with a presently exclusive act after any cure?

## Repository implications

This memo supplies no conclusion about this repository's license or an
enforcement decision.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial doctrine synthesis for issue #17 | Agent; attorney review pending |
