# Three-Expert Research Collaboration Protocol

[中文](README.md)

These prompts organize an AI assistant's work across bioinformatics, experimental biology, and statistics. BioInfo, BioLab, and BioStats participate by default in substantive research tasks. BioTarget adds target research planning when needed. Use the protocol for early research, data interpretation, experimental design, and study planning.

| Role | Responsibility |
| --- | --- |
| BioInfo | Data sources, computational analysis, and biological interpretation |
| BioLab | Experimental models, interventions, and mechanistic validation |
| BioStats | Independent review of design, statistics, and inference in both areas |
| BioTarget | An optional BioInfo workflow for target evidence, expression and localization, disease questions, and study plans |

## Get started

Choose the setup that fits your work.

### Use in a project

1. Copy [AGENTS.md](AGENTS.md) and `references/` into the project root for the Chinese edition. Merge any existing `AGENTS.md` rules and preserve project-specific instructions.
2. For English, use [AGENTS.en.md](AGENTS.en.md) and `references/en/`. If the assistant reads `AGENTS.md` by default, save the selected English core under that name.
3. Start a new chat, or ask the assistant to reread the project rules in an existing chat, then provide your question and materials. For example:

   > Follow the project protocol to assess [research question]. Available materials: [files or evidence]. This round covers only [scope] and should produce [deliverable]. Constraints: [time and resources].

The background template is optional. Role names define assignments; actual delegation depends on the assistant and its tools. If independent agents are unavailable, the assistant should disclose the limitation and review the three perspectives in sequence.

### One-off use or sharing with another assistant

Send the [English single-file edition](AGENTS.en.full.md) or the [Chinese single-file edition](AGENTS.full.md). Both include the full instructions for BioInfo, BioLab, BioStats, and BioTarget; no `references/` directory is needed. Third-party skills must be available in the recipient's environment.

## Workflow and outputs

The coordinator supplies a shared background and evidence version. The three experts assess the material independently, then cross-review their reports. BioStats participates from the design stage and reviews relevant materials before experiments, main analyses, and final conclusions. New evidence or disagreements prompt targeted revisions. File operations, ordinary lookups, and prompt configuration are handled directly.

Research outputs use chapter HTML pages. `00_Overview/index.html` is the sole project overview. `12_Share/<study>_research_summary.html` is a compact file that recipients can open offline, with a target size of no more than 5 MB. Full data, scripts, and long tables stay in the project. Using or editing this protocol alone does not generate a research report. Preserve an existing project's directory names when they differ from these defaults.

BioTarget covers resources such as GTEx, CELLxGENE, Tabula Sapiens, HPA, UniProt, GWAS Catalog, and OMIM, with guidance on provenance and overlapping evidence. Select resources for the question; querying every database is unnecessary.

## Maintain the prompts

Edit source files and regenerate the single-file editions.

| File | Purpose |
| --- | --- |
| `AGENTS.md`, `AGENTS.en.md` | Chinese and English core instructions |
| `references/`, `references/en/` | Role prompts, skill routing, and background templates in each language |
| `AGENTS.full.md`, `AGENTS.en.full.md` | Generated single-file editions; do not edit directly |
| [build_full.py](build_full.py) | Expands the core, supporting files, and both specialist role prompts |
| [scripts/package.sh](scripts/package.sh) | Exports a ZIP from a local Git tag |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

After changing sources, rebuild with Python 3.8 or later:

```bash
python3 build_full.py       # both languages
python3 build_full.py zh    # Chinese only
python3 build_full.py en    # English only
python3 build_full.py --check  # check that generated editions match their sources
```

The build uses only the Python standard library. It checks supporting files, complete role prompts, and internal links, and reports missing content. Keep the editions aligned in role structure, evidence standards, and scope, while writing natural prose in each language.

Before delivery, run `git diff --check`, inspect generated files, and search for formulaic contrasts, stock transitions, unsupported emphasis, repetitive conclusions, and decorative em dashes. Review each match in context; retain scientific qualifications and technical notation.

## Export a release archive

```bash
bash scripts/package.sh v3.2
```

The tag must exist locally. The script exports the tagged commit to `dist/`; it excludes uncommitted changes and does not require the tag to be pushed. Creating tags, committing changes, and publishing releases remain separate maintainer decisions.

## Skills and licensing

The assistant checks the skills available in its environment, reads the relevant `SKILL.md`, and selects skills for each stage. The protocol does not install skills or assume a fixed installation directory. Missing skills require a stated limitation and a suitable fallback.

Build and packaging code use the [MIT license](LICENSE). Prompts and documentation use [CC BY 4.0](LICENSE-docs). Third-party skill content and code are not distributed here; see [Third-party notices](THIRD_PARTY.md).
