#!/usr/bin/env python3
"""Build full single-file versions from each core and its references."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LANGS = {
    "zh": {
        "core": "AGENTS.md",
        "refs": "references",
        "out": "AGENTS.full.md",
        "form_note": "> 完整单文件版，由 `AGENTS.md` 与 `references/` 自动构建，可直接上传或粘贴。",
        "replacements": [
            ("或 `references/background.md` 的模板", "或文末的背景模板"),
            ("（见 `references/roles.md`）", "（见下文的子智能体角色提示词）"),
            ("按 `references/skill-routing.md` 检查", "按下文的“Skill 检测与调用”检查"),
            ("按 `references/roles.md` 传入", "按上文传入"),
            ("`references/background.md` 的模板", "文末的背景模板"),
            ("`references/skill-routing.md`", "下文的“Skill 检测与调用”"),
            ("`references/roles.md`", "下文的子智能体角色提示词"),
            ("完整角色提示词见 [references/target-research-planner.md](references/target-research-planner.md)", "完整角色提示词为可选角色文件（单文件完整版不内嵌）"),
        ],
        "pointers": (
            "references/roles.md",
            "references/skill-routing.md",
            "references/background.md",
            "references/target-research-planner.md",
        ),
    },
    "en": {
        "core": "AGENTS.en.md",
        "refs": "references/en",
        "out": "AGENTS.en.full.md",
        "form_note": "> Complete single-file version, built automatically from `AGENTS.en.md` and `references/en/`; ready to upload or paste.",
        "replacements": [
            ("or the template in `references/en/background.md`", "or the template at the end of this file"),
            ("(see `references/en/roles.md`)", "(see the subagent role prompts below)"),
            ('check the available skills against `references/en/skill-routing.md`', 'check the available skills against "Skill Detection and Selection" below'),
            ("as described in `references/en/roles.md`", "as described above"),
            ("`references/en/background.md`", "the template at the end of this file"),
            ("`references/en/skill-routing.md`", '"Skill Detection and Selection" below'),
            ("`references/en/roles.md`", "the subagent role prompts below"),
            ("the full role prompt is in [references/en/target-research-planner.md](references/en/target-research-planner.md)", "the full role prompt is an optional role file (not included in this single-file version)"),
        ],
        "pointers": (
            "references/en/roles.md",
            "references/en/skill-routing.md",
            "references/en/background.md",
            "references/en/target-research-planner.md",
        ),
    },
}

INCLUDE_RE = re.compile(r"<!-- FULL:([a-z-]+) -->\n(.*?)<!-- /FULL:\1 -->", re.DOTALL)


def build(lang: str) -> None:
    cfg = LANGS[lang]
    core = ROOT / cfg["core"]
    refs = ROOT / cfg["refs"]
    out = ROOT / cfg["out"]

    text = core.read_text(encoding="utf-8")

    openings = re.findall(r"<!-- FULL:([a-z-]+) -->", text)
    closings = re.findall(r"<!-- /FULL:([a-z-]+) -->", text)
    if openings != closings:
        sys.exit(f"[{lang}] marker mismatch:\n  open:  {openings}\n  close: {closings}")
    if len(openings) != len(set(openings)):
        sys.exit(f"[{lang}] duplicate marker: {openings}")

    replaced: list[str] = []

    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        replaced.append(name)
        if name == "form":
            return cfg["form_note"]
        ref = refs / f"{name}.md"
        if not ref.is_file():
            sys.exit(f"[{lang}] missing reference: {ref}")
        return ref.read_text(encoding="utf-8").strip() + "\n"

    full = INCLUDE_RE.sub(repl, text)
    if replaced != openings:
        sys.exit(f"[{lang}] not all blocks replaced: replaced={replaced} openings={openings}")
    if "FULL:" in full:
        sys.exit(f"[{lang}] unresolved FULL marker remains in output")

    for old, new in cfg["replacements"]:
        full = full.replace(old, new)
    for pointer in cfg["pointers"]:
        if pointer in full:
            sys.exit(f"[{lang}] unresolved reference pointer in full: {pointer}")

    full = re.sub(r"\n{3,}", "\n\n", full).strip() + "\n"
    out.write_text(full, encoding="utf-8")

    print(f"[{lang}] core: {len(text)} chars / {len(text.encode('utf-8'))} bytes")
    print(f"[{lang}] full: {len(full)} chars / {len(full.encode('utf-8'))} bytes")
    print(f"[{lang}] blocks: {', '.join(replaced)}")


def main() -> None:
    args = sys.argv[1:] or ["all"]
    if args == ["all"]:
        langs = ["zh", "en"]
    else:
        langs = args
    unknown = [lang for lang in langs if lang not in LANGS]
    if unknown:
        sys.exit(f"unknown language(s): {', '.join(unknown)}; use zh, en, or all")
    for lang in langs:
        build(lang)


if __name__ == "__main__":
    main()
