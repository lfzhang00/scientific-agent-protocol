# Scientific Dual-Agent Collaboration and Feedback Control Protocol (v2.1)

[Chinese](README.md) · Chinese is the default README.

This repository is the test, build, and sharing workspace for the protocol. The Chinese version is the default (`AGENTS.md`); the English version is `AGENTS.en.md`. `references/` and `references/en/` are read on demand; `build_full.py` produces both single-file versions.

## Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Chinese core protocol (v2.1), loaded by default |
| `AGENTS.en.md` | English core protocol (v2.1) |
| `references/roles.md` | Chinese subagent A/B prompts + this round's task package |
| `references/skill-routing.md` | Chinese skill detection, stage routing, and missing-handling rules |
| `references/background.md` | Chinese optional research background template |
| `references/en/roles.md` | English subagent A/B prompts + this round's task package |
| `references/en/skill-routing.md` | English skill detection, stage routing, and missing-handling rules |
| `references/en/background.md` | English optional research background template |
| `build_full.py` | Builds both single-file versions from each core + references |
| `AGENTS.full.md` | Chinese full single-file version (generated; do not edit by hand) |
| `AGENTS.en.full.md` | English full single-file version (generated; do not edit by hand) |
| `README.md` | Chinese README (default) |

## Build

```bash
python3 build_full.py        # build both Chinese and English full versions
python3 build_full.py zh     # build Chinese only
python3 build_full.py en     # build English only
```

Check the output: neither full version contains a `FULL:` marker or a language-matching `references/*.md` pointer. Current sizes:

- Chinese core: 5,780 chars / 14,395 bytes; Chinese full: 9,564 chars / 24,915 bytes.
- English core: 18,198 chars / 18,217 bytes; English full: 31,278 chars / 31,307 bytes.

The English version is a translation, so its character count is not directly comparable with the Chinese one. The default load remains the Chinese core; the English version is for English collaborators or English deliverables. The English version preserves the original project's "discuss in Simplified Chinese by default" setting; an English-speaking team can edit that line in `AGENTS.en.md`.

## Editing

1. Edit only `AGENTS.md`, `AGENTS.en.md`, or the matching files under `references/`; both `*.full.md` files are generated and must not be edited by hand.
2. Run `python3 build_full.py`.
3. Verify using the checks above; share the matching `*.full.md` when needed.
4. To use the protocol in a project: copy `AGENTS.md` + `references/` for Chinese, or `AGENTS.en.md` + `references/en/` for English. Use the full version only for one-off use or cross-assistant sharing.

## Notes

- The core and references are joined by HTML comment markers `<!-- FULL:name -->`; update `build_full.py` if you rename a marker.
- Older versions have been moved out of the workspace; future version history is kept in git commits.
- The default branch is `main`, and the default README is Chinese.
