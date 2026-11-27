# Scientific Three-Expert Collaboration and Feedback Control Protocol (v3.0)

[Chinese](README.md) · Chinese is the default README.

This repository is the test, build, and sharing workspace for the protocol. The Chinese version is the default (`AGENTS.md`); the English version is `AGENTS.en.md`. `references/` and `references/en/` are read on demand; `build_full.py` produces both single-file versions. Current release: v3.0 (protocol text 3.0, 2026-11-28).

## Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Chinese core protocol (v3.0), loaded by default |
| `AGENTS.en.md` | English core protocol (v3.0) |
| `references/roles.md` | Chinese three-expert (BioInfo/BioLab/BioStats) prompts + this round's task package |
| `references/skill-routing.md` | Chinese skill detection, stage routing, and missing-handling rules |
| `references/background.md` | Chinese optional research background template |
| `references/en/roles.md` | English three-expert (BioInfo/BioLab/BioStats) prompts + this round's task package |
| `references/en/skill-routing.md` | English skill detection, stage routing, and missing-handling rules |
| `references/en/background.md` | English optional research background template |
| `references/target-research-planner.md` | Chinese optional role: BioTarget Target Research Planner prompt |
| `references/en/target-research-planner.md` | English optional role: BioTarget Target Research Planner prompt |
| `references/statistical-design-inference.md` | Chinese standing role: BioStats statistical design and inference prompt |
| `references/en/statistical-design-inference.md` | English standing role: BioStats statistical design and inference prompt |
| `build_full.py` | Builds both single-file versions from each core + references |
| `AGENTS.full.md` | Chinese full single-file version (generated; do not edit by hand) |
| `AGENTS.en.full.md` | English full single-file version (generated; do not edit by hand) |
| `README.md` | Chinese README (default) |
| `LICENSE` | MIT license for code |
| `LICENSE-docs` | CC BY 4.0 license for documentation |
| `THIRD_PARTY.md` | Third-party names and dependency notice |
| `CHANGELOG.md` | Version history |
| `scripts/package.sh` | Builds the release zip in `dist/` |

## Build

```bash
python3 build_full.py        # build both Chinese and English full versions
python3 build_full.py zh     # build Chinese only
python3 build_full.py en     # build English only
```

Check the output: neither full version contains a `FULL:` marker or a language-matching `references/*.md` pointer. Current sizes:

- Chinese core: 11,087 chars / 26,774 bytes; Chinese full: 16,015 chars / 40,736 bytes.
- English core: 34,252 chars / 34,279 bytes; English full: 52,377 chars / 52,414 bytes.

The English version is a translation, so its character count is not directly comparable with the Chinese one. The default load remains the Chinese core; the English version is for English collaborators or English deliverables. The English version preserves the original project's "discuss in Simplified Chinese by default" setting; an English-speaking team can edit that line in `AGENTS.en.md`.

## Dependencies

- Build: Python 3.8+ with the standard library only (`re`, `sys`, `pathlib`); no third-party Python packages.
- Packaging: `git` and `git archive`; no extra dependencies.
- Skills named in the routing table are optional and are not distributed with this repository; if missing, use the protocol's built-in fallback.

## Packaging

- Release packages are published on GitHub Releases; run `scripts/package.sh v3.0` locally to create `dist/scientific-agent-protocol-v3.0.zip`.
- The script requires the tag to exist; push it first.

## Editing

1. Edit only `AGENTS.md`, `AGENTS.en.md`, or the matching files under `references/`; both `*.full.md` files are generated and must not be edited by hand.
2. Run `python3 build_full.py`.
3. Verify using the checks above; share the matching `*.full.md` when needed.
4. To use the protocol in a project: copy `AGENTS.md` + `references/` for Chinese, or `AGENTS.en.md` + `references/en/` for English. Use the full version only for one-off use or cross-assistant sharing.

## License

- Code (`build_full.py`, `scripts/package.sh`): MIT; see `LICENSE`.
- Documentation (`AGENTS*.md`, `README*.md`, `references/**`, `CHANGELOG.md`, `THIRD_PARTY.md`): CC BY 4.0; see `LICENSE-docs`.
- Third-party skill names are referenced for routing only; no content or code is bundled; see `THIRD_PARTY.md`.

## Notes

- The core and references are joined by HTML comment markers `<!-- FULL:name -->`; update `build_full.py` if you rename a marker.
- The optional `target_research_planner` and `statistical_design_inference` role prompts are not embedded in `*.full.md`; when sharing, include the matching `references/target-research-planner.md` and `references/statistical-design-inference.md`.
- Older versions have been moved out of the workspace; future version history is kept in git commits.
- The default branch is `main`, and the default README is Chinese.
