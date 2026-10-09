# AI Jarvis Assistant CodeX — owner licensing review

Prepared October 9, 2026 for the October 14 review, 10:00–10:30 a.m. Pacific.
**Decision status: OPEN. This brief is planning analysis, not legal advice or an adopted license.**

## Verified baseline and limits

Reviewed main at [c5354bf](https://github.com/lippytm/Claude-with-AI-Jarvis-Assistant-CodeX-/commit/c5354bf3e14d257462f5837085fd7d7d98903f02).
Its complete tree contains seven scaffold files: .gitignore, README.md, LICENSE,
LICENSING.md, and the three LICENSE-*.md drafts. No implemented developer tools,
AI Clone Engines, educational library, or character assets appear in that main tree.
Open PRs and external/private assets are not part of this file-by-file baseline.

[LICENSE](../LICENSE) has been present since
[the initial commit](https://github.com/lippytm/Claude-with-AI-Jarvis-Assistant-CodeX-/commit/7697a49abb455b58782aa9b7526afdbc17ff8f62),
September 20, 2026 at 03:12 UTC (September 19, 8:12 p.m. Pacific).
The [structure draft](https://github.com/lippytm/Claude-with-AI-Jarvis-Assistant-CodeX-/commit/fd2bc5078b55d52fdcbaee3e4c2f2c654bea7d45)
was added September 20 at 23:22 UTC (4:22 p.m. Pacific); the three license drafts
were added later that same day. LICENSE's inspected history shows no subsequent change.

The [September 22 fix plan](https://docs.google.com/document/d/1_vGZ7FKqEI-1w4D1HXzlPeS_4QwzwbL5rIkXYpk4rfk/edit)
reserves licensing selection for the owner. Its suggestion to remove open terms for
proprietary licensing needs a historical-permissions qualification; its one-word
choice does not establish asset scope, rights ownership, or a release boundary.
Its reconnect status was historical, not a current connectivity finding.

## Compare the four approaches

| Approach | Reuse and commercial products | Obligations and tradeoffs | Fit for the intended project |
|---|---|---|---|
| CC0 1.0 | Broad copying, modification, redistribution and sale within covered rights | No required credit; no patent grant; dedication/fallback cannot simply be withdrawn | Suitable if unrestricted reuse is the goal; poor fit for reserving character exclusivity |
| MIT | Reuse, derivatives, redistribution, sublicensing and sale, including closed products | Preserve copyright and permission notice in copies or substantial portions; no express patent clause | Simple choice for reusable tools and example code; does not prevent competing products |
| Apache-2.0 | Permissive reuse, including commercial and closed products | License/notice preservation, changed-file notices, applicable NOTICE attribution; limited contributor patent grant with litigation termination; no general trademark grant | Strong candidate for reusable engines and integration tools when patent clarity matters |
| Proprietary | Permissions depend on the specific agreement; public visibility alone does not supply a general reuse grant | Custom permissions, support and redistribution rules require drafting; statutory exceptions and existing grants still matter | Candidate for separately controlled new modules and premium creative assets; reduces outside adoption |

Sources: [CC0 legal code](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en),
[MIT text](https://opensource.org/license/mit),
[Apache-2.0 text, sections 2–6](https://www.apache.org/licenses/LICENSE-2.0),
and [GitHub's no-license explanation](https://choosealicense.com/no-permission/).
None of these options guarantees that every included dependency, dataset, or asset is
cleared for the intended use. MIT and Apache-2.0 are permissive, not source-sharing
requirements; attribution is mainly notice preservation, not mandatory advertising
or a guarantee of prominent personal credit.

## Apply the comparison by intended use

- **Reusable developer tools:** MIT favors minimal notice administration. Apache-2.0
  adds explicit contributor patent terms. CC0 favors the least copyright friction
  but omits that grant. Proprietary terms impede the intended reuse.
- **AI Clone Engines:** Separate engine code from model weights, training data,
  memory records, voice/likeness assets, and persona text. MIT or Apache-2.0 can cover
  the engine without granting all those other rights. CC0 offers no clone-specific
  safeguard; proprietary engine terms can reserve new code but do not establish
  consent to imitate a person. Review provider terms and each input's provenance.
- **Educational material:** License executable examples with the reusable code.
  Identify tutorial prose separately. CC0 enables unrestricted teaching and remixing;
  MIT/Apache can cover documentation, though content-specific licenses may communicate
  the goal better. Proprietary or ND terms complicate translation and classroom adaptation.
- **Creative characters:** CC0 is inconsistent with retaining exclusive control over
  covered expression. MIT/Apache likewise allow extensive reuse when applied to assets.
  For new, protectable assets, proprietary permissions or a deliberate content license
  can set different sharing rules. Names, ideas, expression, and trademark rights need
  separate analysis; no policy can guarantee ownership of an entire character concept.
- **Commercial offerings:** All three permissive approaches support monetization.
  Charge for hosting, support, integration, approved new assets, or proprietary add-ons.
  A paid product is a distribution/business category, not automatically a separate
  copyright category. Avoid a universal approval fee for use already permitted.

The [Creative Commons FAQ](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software)
distinguishes software licensing from documentation/art licenses and recognizes CC0
as acceptable for software. For AI-generated assets, the
[U.S. Copyright Office's copyrightability report](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)
makes human authorship central: do not assume that a generated output supports the
same exclusive rights as human-authored expression.

## What can change for future releases

An owner with the necessary rights may select terms for genuinely new protectable
contributions. Preserve the old permissions for inherited material; identify the
new contribution and its license separately. Other contributors' rights and third-party
licenses can limit what the owner can offer.

Example: a future engine incorporates a legacy CC0 utility and adds a new scheduling
module. Approved terms may cover the new module; users retain the legacy utility's
permissions. Republishing the utility under another label does not force users to
abandon those permissions. New protection in a derivative work concerns new authorship,
not the underlying work. [Copyright Office Circular 14](https://www.copyright.gov/circs/circ14.pdf).

Likewise, removing a file, making a repository private, or changing its version number
does not undo a valid earlier grant. Maintain an inventory of commits, file hashes,
notices, releases, and any contemporaneous exclusions. Scope and authority to dedicate
specific materials remain legal-review questions, especially for material first added
alongside conflicting drafts.

## Specific corrections needed

| Existing text | Problem | Documentation correction now / legal decision later |
|---|---|---|
| LICENSING.md: material “is split” into three categories “instead of one blanket license” | Presents a proposed regime as operative while CC0 remains | Describe the actual files and pending proposal; do not announce supersession |
| LICENSE-CODE.md: both proprietary and MIT-style alternatives | Contradictory choices; condensed grant is not standard MIT | Preserve draft; owner later chooses exact text and covered paths |
| LICENSE-CONTENT.md: “No modified/derivative versions” | Inaccurate summary of the referenced CC pattern | Explain that actual BY-NC-ND permits noncommercial production/reproduction of adaptations, but not sharing them |
| LICENSE-COMMERCIAL.md: any product requires written commercial terms | Blanket restriction conflicts with permissive reuse | Limit any later product contract to its identified assets/services and lawful rights |
| Draft LLC holder/marks claims | Formation language is not proof of title or trademark clearance | Verify entity, assignment and marks before changing legal notices |
| September 22 plan: remove LICENSE to become proprietary | Omits prior grants and new/legacy distinction | Keep original plan; treat this brief as a qualification for the upcoming review |

The [actual BY-NC-ND 4.0 terms](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.en),
section 2(a)(1), matter more than a “style” summary. An NC/ND choice also limits
commercial reuse and public remixes; it is unsuitable for broadly reusable engines
and can frustrate educational adaptations. No such choice is adopted here.

## Recommended structure for owner consideration

My recommendation is a reusable software layer plus separately identified creative
assets and commercial agreements. I favor **Apache-2.0 for future reusable software**
if the owner wants adoption and contributor patent clarity. **MIT** is a coherent
alternative if simplicity is the priority. This recommendation is not a selection.

Illustrative organization, to be implemented only after approval:

| Layer | Proposed boundary | Owner decision still required |
|---|---|---|
| Legacy material | Historical commit/file inventory with original notices | Confirm CC0 scope; preserve valid permissions |
| Reusable software | src/, tools/, executable examples and generic engine code | Apache-2.0, MIT, continued CC0, or another approved choice |
| Educational prose | docs/tutorials/ separate from executable snippets | CC0, attribution-oriented content terms, or reserved permissions |
| Creative assets | content/characters/, stories, artwork, persona expression | Reserve new assets or choose an exact content license with defined scope |
| Proprietary additions | Separate package/repository for new premium modules | Exact terms, entitlement, redistribution and compatibility |
| Offerings and brand | Service agreements and separate trademark policy | Price/support/privacy terms, brand clearance and authorized uses |

These paths are examples, not an inventory or new exclusions from today's LICENSE.
Prefer keeping controlled new creative assets in a separate repository until their
terms are approved, to avoid exposing them under an ambiguous repository-wide default.

Do not use “commercial” as a blanket exception to an open code license. Separate code
permissions from service access, premium content delivery, and use of branding.
Optional paid agreements must not misrepresent existing public permissions.
Dual licensing may be possible for rights the owner controls, but an additional paid
offer cannot erase the public alternative; contributor permission may be needed.

## Owner decision record — all fields pending

Before approving any license migration, record:

1. Desired software reuse: broad commercial reuse, or controlled distribution?
2. Exact software license and standard text; selected paths and excluded third-party items.
3. Educational prose policy, including attribution, translation and commercial teaching.
4. New creative-asset policy: sharing, adaptation, commercial use and AI/persona use.
5. Paid offerings: what is actually being sold, and which assets/rights require permission?
6. Verified rights holder and authority for each category, including contributors.
7. First affected release/commit and a legacy/new-material map.
8. Counsel review reference, explicit owner approval, and approval date.

**No response, draft PR approval, or merge of documentation clarification counts as
approval of a future license.** No option is preselected in this decision record.

Counsel should review historical CC0 scope/authority, jurisdictional effects, asset
copyrightability, personality/privacy consent, dependency compatibility, and the
commercial/trademark documents. Company formation alone is not an IP transfer; U.S.
copyright transfers generally require a signed writing under
[17 U.S.C. §204](https://www.copyright.gov/title17/92chap2.html#204).
Do not assert that the pending LLC owns all work, that a mark is registered or cleared,
or that a content restriction can reclaim rights already validly released.

## Review package and acceptance

The accompanying documentation proposal changes README.md and LICENSING.md and adds
this brief. It preserves LICENSE and all three LICENSE-*.md drafts byte-for-byte.
No terms are finalized, no branch is merged, and no agreement is executed.

At the scheduled review: confirm the legacy inventory, discuss software reuse goals,
choose content/product boundaries, and assign legal review. Implement exact approved
licenses in a separate change only after that review and explicit owner authorization.
