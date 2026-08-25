---
id: PR-0009
title: Covered work, derivative work, linking, aggregation, and source scope
question: "How do copyright derivative-work boundaries and license-defined covered-work, linking, aggregation, and corresponding-source boundaries interact?"
short_answer: "Copyright's derivative-work inquiry and a license's defined coverage/source boundary are related but not interchangeable. Technical labels such as static linking, dynamic linking, plug-in, IPC, API use, containerization, or aggregation do not yield a universal answer. GPL-family licenses use work-based concepts and specific source/relinking rules; MPL/CDDL are file-oriented; EPL excludes files that only link/bind/subclass from Modified Works; EUPL, OSL, RPL, SSPL, and source-available terms use their own definitions. The reviewed authorities do not decide a general linking rule, so fact-specific analysis remains partial."
research_status: partial
legal_review: pending
jurisdictions: [US-federal, US-Ninth-Circuit, European-Union, Germany]
licenses: [GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, EUPL-1.2, OSL-3.0, RPL-1.5, SSPL-1.0, source-available]
actors: [copyright-owner, contributor, modifier, distributor, service-operator, recipient]
conduct: [modify, prepare-derivative-work, distribute, convey, aggregate, provide-source]
topics: [scope, derivative-work, linking, aggregation, corresponding-source]
confidence: low
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0002, PR-0003, PR-0004, PR-0006, PR-0008, PR-0010]
supersedes: []
---

# PR-0009: Covered work, derivative work, linking, aggregation, and source scope

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

Actor: a contributor/owner, modifier, distributor, or source recipient.
Trigger: combining code, linking, bundling, conveying executables, or providing
source. This memo separates copyright law from contract/license definitions.
It does not render an engineering conclusion for a particular architecture,
dependency graph, build process, jurisdiction, or license exception.

## Short answer

The first question is copyright: does the resulting work embody protected
expression so as to be a derivative work under applicable law? The second is
textual: what does the selected license call a covered work, modification,
combined/larger work, extension, required component, corresponding source, or
service source? A third is factual: what source and installation/relinking
material was conveyed. *Micro Star* confirms that a digital file may be
derivative even without carrying every asset, but expressly cannot answer a
general linking rule. *Hellwig* did not reach GPL linking scope because proof
was insufficient.

## Analysis

### Do not substitute labels for facts

Static/dynamic linking, header inclusion, runtime loading, RPC/IPC, API calls,
packaging, containers, and separate processes are evidence about architecture,
not statutory or license conclusions. Analyze protected expression, code
incorporation, control/data flow, build/relink mechanism, shared address space,
distribution unit, and each license's actual definitions. A lawful copyright
conclusion may still leave a contractual source/relinking obligation; a broad
license definition may still require enforceability analysis.

### Textual comparison

| Family | Coverage/source boundary stated by text | Critical limit |
|---|---|---|
| GPL-2 | Work based on Program / whole work containing portions; complete corresponding source on executable distribution | No authoritative universal linking test |
| GPL-3/AGPL-3 | Covered work, modified version, Corresponding Source; aggregate clause permits separate independent works on same medium | AGPL §13 separately reaches modified Program network interaction |
| LGPL-2.1 | Library versus work using Library; §6 supplies relinking/source routes | Technical compliance and derivative status remain fact-specific |
| LGPL-3 | Application, Combined Work, Minimal Corresponding Source/Corresponding Application Code | Definitions are not a judicial linking holding |
| MPL-2/CDDL-1 | File-level Covered Software/Modifications, permitting Larger Work non-covered files | A new file containing covered code is covered under MPL |
| EPL-2 | Program/Modified Works; excludes files only declaring/interfacing/linking/binding/subclassing | Other changes can alter classification |
| EUPL-1.2 | Derivative Works and source preferred for modification; compatibility list | National copyright law and language control |
| OSL/RPL/SSPL | Derivative Works/Original Work, Required Components, Service Source Code as defined | Broad terms require exact-version and deployment facts |
| Source-available | BUSL/ELv2/Commons Clause/FSL/PolyForm define licensed software, derivatives or use restriction differently; often no reciprocal source duty | Never infer copyleft source scope from source availability |

Official-text cards in PR-0002 support these descriptions. They do not decide
technical scope or remedy.

### Corresponding source is not simply "the repository"

For GPLv3/AGPLv3, identify the Corresponding Source definition and the conveyed
object code/build context. LGPL variants add their own application/relinking
materials. MPL/CDDL/EPL divide covered source from larger work differently.
SSPL §13 can reach Service Source Code; RPL invokes Required Components.
The scope of a source offer must be tested against the particular defined term,
not a generic request for "all source."

### Authority and contrary limits

*Micro Star* concerned game-level files and preliminary injunctive relief, not
software libraries. *Fisher* left GPLv3 covered-work/conveyance facts for a
jury. *Hellwig* supplies a negative limit: failed proof did not establish that
VMware complied or that dynamic linking never makes a covered work. No reviewed
U.S. appellate opinion decides the requested GPL/AGPL/LGPL static-versus-dynamic
linking proposition. Mark it `partial` rather than adopting any steward FAQ or
technical rule as law.

## Scenario matrix

| Scenario | Textual route | Main uncertainty |
|---|---|---|
| Separate proprietary program dynamically uses LGPL library | LGPL §6/§4 source-relinking analysis | Architecture, version, conveyed materials |
| GPL binary bundles independent utility on same image | GPL-3 aggregate clause may matter | Independence/copyright boundary |
| MPL executable includes modified covered file plus new files | Disclose modified covered source | File contents and source-access timing |
| SSPL service uses management/orchestration code | §13 Service Source Code analysis | Whether program functionality is offered as service |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0077](../../authorities/cases/micro-star-v-formgen.md) | Fact-specific derivative-work analysis | Ninth Circuit game facts; PI posture |
| [AUTH-0042](../../authorities/cases/fisher-v-sas-automation-summary-judgment.md) | GPLv3 coverage/conveyance can be fact issues | District court; no final merits result |
| [AUTH-0059](../../authorities/cases/hellwig-v-vmware.md) | Proof failure before linking decision | Germany; no scope holding |
| [GPL/LGPL/MPL/EPL/CDDL/EUPL/OSL/RPL/SSPL cards](../../authorities/licenses/) | Exact defined boundaries | Official text, not judicial construction |

## What would change the answer

- Dependency/source tree, build scripts, binaries, symbols, licenses/notices,
  delivery channel, and selected law.
- An exact-license appellate ruling on linking or Corresponding Source.

## Open questions for counsel

- What precisely is combined, copied, conveyed, and needed to modify/relink?
- Which license version/exceptions govern each component and what forum's
  derivative-work test applies?

## Repository implications

This memo does not classify any FastLED or third-party component and makes no
change to `LICENSE`.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial scope synthesis for issue #17 | Agent; attorney review pending |
