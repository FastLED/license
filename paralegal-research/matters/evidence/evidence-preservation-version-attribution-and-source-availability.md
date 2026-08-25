---
id: PR-0016
title: Evidence preservation, version attribution, and public-source availability
question: "What license-agnostic, lawful evidence record can distinguish public investigation from compelled discovery and support later analysis of a software version, its attribution, and public-source availability?"
short_answer: "A defensible preliminary record preserves what was publicly and lawfully available, identifies the version and capture method, retains the original artifact and working derivatives separately, and documents hashes, provenance, and custody. It can support later factual analysis but does not itself establish authorship, a license trigger, source completeness, or infringement. Public source release is a factual distribution/publication question; protective-order production is confidential litigation discovery and is not public release."
research_status: answered
legal_review: pending
jurisdictions: [US-federal]
licenses: []
actors: [copyright-owner, contributor, distributor, service-operator, recipient, investigator]
conduct: [preserve, reproduce, distribute, provide-network-access, withhold-source]
topics: [evidence, preservation, version-attribution, provenance, public-source-availability]
confidence: medium
last_verified: 2026-08-25
github_issues: [https://github.com/FastLED/license/issues/17]
related_matter_ids: [PR-0017, PR-0018, PR-0019]
supersedes: []
---

# PR-0016: Evidence preservation, version attribution, and public-source availability

> Preliminary research for attorney review. Not legal advice and not a license
> or policy decision.

## Scope and assumptions

This U.S.-federal operational research memo concerns lawfully obtained public
artifacts: shipped media or binaries, publicly accessible repositories,
download pages, notices, package metadata, and communications already received
by the actor. It assumes no account bypass, scraping contrary to applicable
law/terms, device access, interception, or acquisition from a nonpublic system.
It does not decide ownership, copying, derivative-work status, a particular
license's source obligation, or an obligation to preserve triggered by a
specific dispute. The license/version must be separately identified; no term is
assumed from a family label.

## Short answer

Preservation should create a repeatable factual record: retain the original
available artifact, record source URL/location, date/time and timezone,
acquisition method, relevant access context, file size, cryptographic hash,
handler/transfer history, and a description of any later analysis. NISTIR 8387
supports this integrity-oriented practice; Federal Rules of Evidence 901,
902(13)–(14), and 1001–1008 govern a possible federal authentication/best-
evidence foundation, not the substantive proposition.

Public investigation ends at materials lawfully accessible without compelled
process. Discovery begins only in an authorized proceeding and is governed by
rules, court orders, privilege, proportionality, and protective orders. A
production marked confidential or attorneys'-eyes-only can enable litigation
analysis while restricting dissemination; it is not public source availability.
Conversely, a public repository or source archive may be evidence of a release,
but cannot alone prove that it is the complete or correct source for a given
binary, that the releaser was authorized, or that the release met a particular
license term.

## Analysis

### Preserve provenance and integrity, not a conclusion

NIST guidance advises documentation of an artifact's source and acquisition,
secure storage, hashes, and chain of custody. It supports the *method* of
preserving a digital artifact, not the legal conclusion that a hash identifies
an author or proves a matching source tree. Federal Rules 901 and 902 may be
relevant later, but admission depends on the offered item, witness/certificate,
notice, and forum-specific precedent. [AUTH-0112](../../authorities/statutes/us-federal-rules-of-evidence-digital-authentication.md) and [AUTH-0113](../../authorities/statutes/nist-digital-evidence-preservation.md).

A binary/source comparison should therefore preserve: the acquired binary and
source snapshot; tools and versions; build instructions and environment;
commands; outputs; dates; known nondeterminism; and the analyst's distinction
between observed matches and interpretive conclusions. A mismatch can arise
from compiler, toolchain, build flags, dependencies, timestamps, packing, or
missing material; it is not automatically evidence of a missing source
obligation.

### Version attribution requires converging facts

Useful facts can include embedded notices, version strings, package manifests,
SBOMs, signatures, release tags/commit identifiers, distributor labels,
shipping records, and reproducible-build results. Each has limits: a tag can
move, a notice can be stale, a signature can authenticate a key rather than a
license grant, and an SBOM can be incomplete. Preserve any page/archive context
and identify the person or system making each attribution. Ownership and chain
of title remain separate evidence questions.

### Public release and protected discovery are different channels

Public-source availability asks what a recipient or public user could obtain,
when, from whom, under what access conditions, and whether the available
material corresponds to the relevant version. Discovery production asks what a
party/nonparty must provide in a case under Rules 26, 34, or 45. A Rule 26(c)
protective order can limit use or disclosure; it does not convert confidential
production into a public release or resolve a source-availability condition.
[AUTH-0111](../../authorities/statutes/us-federal-discovery-and-protective-orders.md).

## Scenario matrix

| Scenario | Factual record to preserve | Main uncertainty |
|---|---|---|
| Public download or repository | Original response/archive, URL, timestamp, hash, release/ref, notices | Whether it was complete/correct source for a product |
| Device or product lawfully acquired | Photographs, labels, receipt, firmware image method, hash, custody log | Whether supplied software matches a public release |
| Recipient reports no source link | Original package/UI/communication and ordinary access path | Exact license obligation and recipient entitlement |
| Confidential litigation production | Producing party, order/designation, native format, production metadata | Scope of permitted use; it is not public availability |
| Binary/source comparison | Inputs, tools, commands, outputs, environment, analyst notes | Reproducibility and legal significance of differences |

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [AUTH-0112](../../authorities/statutes/us-federal-rules-of-evidence-digital-authentication.md) | Authentication/self-authentication and best-evidence framework | Federal rules; no automatic admission or merits proof |
| [AUTH-0113](../../authorities/statutes/nist-digital-evidence-preservation.md) | Technical integrity and custody documentation | Official guidance, not legal rule |
| [AUTH-0111](../../authorities/statutes/us-federal-discovery-and-protective-orders.md) | Discovery/protective-order distinction | Federal procedure; local practice controls details |
| [NISTIR 8387](https://doi.org/10.6028/NIST.IR.8387) | Separate originals, records, hashes, and custody | Technical source only |

## Research checklist for counsel review

- Identify the actual actor, license text/version, release date, product version,
  and asserted trigger before characterizing an obligation.
- Preserve lawful originals and a read-only/controlled working copy; log hashes,
  source, time/timezone, acquisition method, and every transfer.
- Record access conditions and whether the artifact was public, recipient-only,
  or obtained under court process.
- Preserve binary/source-comparison methods and uncertainty; retain raw output.
- Assess forum-specific preservation duties, privacy, contract, anti-circumvention,
  trade-secret, and evidence rules before expanding collection.

## What would change the answer

- A selected forum, litigation hold, specific license obligation, contested
  authenticity, nonpublic data source, or a proposed forensic method.

## Open questions for counsel

- Whether and when a concrete dispute creates a preservation duty, and its scope.
- Whether the proposed acquisition and automated collection are lawful in all
  relevant jurisdictions.
- What foundation, expert evidence, or protective-order terms a chosen court requires.

## Repository implications

No change to `LICENSE` follows. A project-specific preservation policy or
technical-release procedure would require separate engineering and legal review.

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial research for issue #17 | Agent; attorney review pending |
