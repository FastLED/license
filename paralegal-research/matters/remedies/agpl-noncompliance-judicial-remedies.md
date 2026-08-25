---
id: PR-0001
title: Judicial remedies for AGPL-style source noncompliance
question: "For an infringer that has not complied with an AGPL code base, what can a U.S. court ordinarily order, and can the remedy be source disclosure or acquisition of a commercial license?"
short_answer: "A court can ordinarily stop continued unlicensed copying, distribution, or other acts within the copyright owner's exclusive rights and may award authorized monetary and ancillary relief. Source disclosure or performance of a source obligation may be requested under a contract theory, but it is not an automatic or well-established final remedy in U.S. AGPL litigation. A judge generally cannot force parties into a new commercial license; a license can be voluntarily obtained, and its value may sometimes inform damages."
research_status: answered
legal_review: pending
jurisdictions:
  - US-federal
  - California
licenses:
  - GNU Affero General Public License version 3
actors:
  - copyright-owner
  - exclusive-licensee
  - service-operator
  - distributor
  - recipient
conduct:
  - distribute
  - provide-network-access
  - withhold-source
  - continue-after-termination
topics:
  - AGPL
  - remedies
  - injunction
  - source-disclosure
  - commercial-license
confidence: medium
last_verified: 2026-08-25
github_issues:
  - https://github.com/FastLED/license/issues/15
  - https://github.com/FastLED/license/issues/17
related_matter_ids: []
supersedes: []
---

# PR-0001: Judicial remedies for AGPL-style source noncompliance

> Preliminary research for attorney review. Not legal advice and not a decision
> to adopt the AGPL, GPL, or any other license.

## Scope and assumptions

This memo answers a hypothetical enforcement question under U.S. federal
copyright law, with California contract principles relevant to the principal
reported GPL cases. It assumes the claimant owns or exclusively controls the
copyrights needed to sue and can prove that the defendant engaged in conduct
requiring permission. It does not decide whether FastLED should adopt AGPL or
whether the current [draft license](../../../LICENSE) produces the same claims.

The key distinction is between:

- an injunction that says **stop conduct unless it is licensed**;
- an affirmative order to **perform the source-disclosure promise**; and
- an order that purports to **create a new paid license** between unwilling
  parties.

Those are not interchangeable remedies.

## Short answer

The conventional copyright remedy is an injunction against continued
unlicensed exercise of copyright rights, supported where proven by impoundment
or destruction, actual damages and infringer's profits, or statutory damages
and attorney's fees when registration and other statutory requirements are met.
A compliant license path may make the injunction read functionally as “stop
unless you comply or obtain separate permission,” but the court is prohibiting
unlicensed conduct rather than choosing a business model for the defendant.

An order requiring publication or delivery of corresponding source is legally
plausible under a contract/specific-performance theory and has appeared in
requests and settlements. The reviewed U.S. authorities do not establish a
routine final AGPL judgment compelling public release. That relief depends on
standing, the governing law, the exact promise, adequacy of damages, and normal
equitable limits.

A court generally cannot impose a commercial license that the copyright owner
never agreed to grant. The parties can settle on a commercial license or enter
a consent judgment. In a damages case, evidence of the owner's commercial
license price may be relevant, but it is a valuation theory—not compelled
acceptance of that license.

## Remedy matrix

| Remedy | What a judge could do | Important limit |
|---|---|---|
| Prohibitory injunction | Stop unlicensed copying, modification, distribution, or other proven acts; condition future conduct on having valid permission | Requires ownership/standing, infringement, and equitable factors; network operation alone must implicate the applicable right or claim |
| Source-code performance | Order a defendant to deliver or publish source if a valid contract claim and specific-performance requirements are established | U.S. AGPL precedent reviewed here does not show this as an automatic or routine final award |
| Actual damages and profits | Compensate proven loss and recover qualifying profits not already included | Causation, apportionment, and non-duplication matter; a commercial fee is evidence, not an imposed contract |
| Statutory damages and fees | Award the relief authorized by 17 U.S.C. §§504–505 | Registration timing under §412 can bar statutory damages and fees for some infringements |
| Impoundment or destruction | Control infringing copies and relevant articles under 17 U.S.C. §503 | Scope and proportionality depend on the articles and proven infringement |
| Declaratory relief | Declare rights, termination, breach, or noncompliance where a justiciable controversy exists | A declaration does not by itself publish source or create a license |
| Contempt/enforcement | Enforce an injunction or consent decree after entry | Applies only to the actual terms and persons bound by the order |

## Role-play scenarios

### 1. Copyright owner proves unlicensed distribution

The owner asks the court to enjoin further distribution. A conventional order
would bar distribution unless the defendant has permission. The defendant can
then stop, comply with an available license path if the license permits cure and
reinstatement, or negotiate a commercial license. The order need not force the
owner to offer commercial terms.

### 2. Service operator violates AGPL §13 but distributes no copy

The claimant asks for a source offer to remote users. The factual and doctrinal
questions become sharper: the claimant must identify an enforceable claim and
show why affirmative performance is available. The language of AGPL §13 is
clear as a license obligation, but this research did not identify a final U.S.
AGPL merits judgment establishing the precise remedy for network-only
noncompliance.

### 3. Claimant asks for “publish the code or buy a license”

That can be a settlement proposal. It can also describe the defendant's
practical choices after an injunction against unlicensed conduct. It should not
be pleaded or described as though a judge can compel an unaccepted commercial
contract. *Artifex v. Hancom* supports potential use of commercial-license value
as a damages measure while expressly resisting the idea that the license was
automatically imposed.

### 4. Downstream user seeks source rather than the copyright owner suing

The theory may be third-party-beneficiary contract enforcement and specific
performance, as in the pending *SFC v. Vizio* litigation, rather than copyright
infringement. Standing, state contract law, federal preemption, and the requested
form of performance all require separate analysis. The existence of that case
does not yet establish a final right to compelled source production.

### 5. Defendant cures after notice

AGPL §8 contains termination and reinstatement rules, including specified cure
mechanisms. Reinstatement of permission going forward does not necessarily
erase claims or remedies for earlier unlicensed acts. The text, notice history,
whether this is a first violation, and the timing of cure must be mapped before
stating the result.

## Analysis

### Copyright remedies focus on stopping infringement and compensating harm

Sections 502–505 of the Copyright Act authorize injunctions, impoundment and
disposition, damages and profits or statutory damages, costs, and discretionary
attorney's fees. Section 412 makes registration timing important to statutory
damages and fee recovery. These provisions do not create a general power to
write a new commercial license for the parties.

### License conditions can support copyright claims, but wording matters

*Jacobsen v. Katzer* recognizes that open-source restrictions tied to the scope
of permission can be copyright conditions rather than only contractual
promises. *MDY Industries v. Blizzard* supplies the Ninth Circuit framework:
breach of a condition that limits the license's scope and has a copyright nexus
can sound in copyright, while breach of an independent covenant generally
sounds in contract. Application to a particular AGPL obligation still depends
on the text and conduct.

### Reported GPL disputes do not establish an automatic forced-license remedy

In *Artifex v. Hancom*, a federal trial court allowed contract and copyright
theories concerning GPL-licensed Ghostscript to proceed. It treated the value
of Artifex's commercial license as a possible damages measure but did not deem
Hancom to have accepted or been forced into that commercial license. The case
later settled, so it did not yield a final merits judgment ordering public
source disclosure.

The BusyBox/Westinghouse default judgment demonstrates that a federal court can
permanently enjoin future distribution after GPL noncompliance and award
monetary and ancillary relief. Because it was a default judgment involving
distribution, its precedential and factual reach is limited.

Settlements such as BusyBox/Monsoon have required source publication,
recipient notice, compliance controls, payment, and conditional reinstatement.
Those terms show practical negotiated remedies, not what every judge must order.

*SFC v. Vizio* tests a beneficiary's state-contract claim for source code and
specific performance. Its procedural survival is important, but no final
merits decision identified as of the verification date establishes that the
requested source remedy will be awarded.

## Authorities

| Authority | Proposition supported | Posture and limits |
|---|---|---|
| [17 U.S.C. remedies](../../authorities/statutes/us-copyright-remedies.md) | Statutory menu of copyright relief and registration constraints | Does not decide contract remedies or AGPL-specific liability |
| [GNU AGPLv3](../../authorities/licenses/gnu-agpl-v3.md) | §13 network source offer; §8 termination, cure, and reinstatement | License text, not a judicial ruling |
| [*Jacobsen v. Katzer*](../../authorities/cases/jacobsen-v-katzer.md) | Open-source terms may be enforceable copyright conditions | Preliminary-injunction appeal; no final source-disclosure remedy |
| [*MDY Industries v. Blizzard*](../../authorities/cases/mdy-industries-v-blizzard.md) | Ninth Circuit condition/covenant and copyright-nexus framework | Not an open-source case |
| [*Artifex v. Hancom*](../../authorities/cases/artifex-v-hancom.md) | GPL contract/copyright claims; commercial-license damages theory | Trial-level pretrial ruling; later settlement |
| [BusyBox / Westinghouse](../../authorities/cases/busybox-westinghouse.md) | Permanent injunction after GPL distribution noncompliance | Default judgment; limited precedential value |
| [BusyBox / Monsoon](../../authorities/cases/busybox-monsoon-settlement.md) | Publication, notice, controls, payment, and conditional reinstatement | Private settlement; not an adjudicated remedy rule |
| [*SFC v. Vizio*](../../authorities/cases/sfc-v-vizio.md) | Beneficiary contract/specific-performance theory can proceed procedurally | Pending; no final merits/source-production award identified |

## What would change the answer

- The forum and governing state contract law.
- Whether the defendant distributed copies or only provided network access.
- The claimant's copyright ownership, exclusive rights, or beneficiary status.
- Exact AGPL version and source-obligation facts.
- Registration and infringement dates.
- Evidence that money is inadequate and affirmative relief is feasible.
- A later final decision in *SFC v. Vizio* or another AGPL merits case.

## Open questions for counsel

- Under the anticipated forum's law, should source publication be pleaded as
  specific performance, injunctive relief, or both?
- For network-only AGPL §13 conduct, what exclusive copyright right and what
  contract formation facts support each claimant's theory?
- What ownership and registration record exists for each relevant release?
- Would a commercial-license price be admissible and sufficiently comparable
  to prove actual damages on the assumed facts?
- How should requested relief preserve an option to negotiate without implying
  that the court may compel either party to license?

## Repository implications

This research does not support changing the repository to AGPL and does not
resolve the remedy language appropriate for the FastLED Reciprocal License. A
separate, counsel-reviewed matter should analyze the current draft's §11.3
commercial-transfer obligation in likely enforcement forums. That scenario is
listed in the [backlog](../../BACKLOG.md).

Discussion and follow-up are tracked in [GitHub issue #15](https://github.com/FastLED/license/issues/15).

## History

| Date | Change | Author/reviewer |
|---|---|---|
| 2026-08-25 | Initial research captured from issue #15 | Agent; attorney review pending |
