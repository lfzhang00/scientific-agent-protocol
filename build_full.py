#!/usr/bin/env python3
"""Build or check complete research prompts using only the standard library."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGS = {
    "zh": {
        "core": "AGENTS.md",
        "refs": "references",
        "out": "AGENTS.full.md",
        "note": "> 完整单文件版，包含四个角色的指令和引用资料，由源文件自动生成。",
        "role_marker": "## 完整角色提示词",
        "role_titles": ("BioStats 完整提示词", "BioTarget 完整提示词"),
    },
    "en": {
        "core": "AGENTS.en.md",
        "refs": "references/en",
        "out": "AGENTS.en.full.md",
        "note": "> Generated single-file edition with all four role prompts and supporting material.",
        "role_marker": "## Full Role Prompt",
        "role_titles": ("Full BioStats prompt", "Full BioTarget prompt"),
    },
}
SECTIONS = ("roles", "skill-routing", "background")
ROLES = (("statistical-design-inference", "bio-stats"), ("target-research-planner", "bio-target"))
INCLUDE_RE = re.compile(r"<!-- FULL:([a-z-]+) -->\n(.*?)<!-- /FULL:\1 -->", re.DOTALL)
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)")


def build(lang: str) -> str:
    cfg = LANGS[lang]
    core, refs = ROOT / cfg["core"], ROOT / cfg["refs"]
    text = core.read_text(encoding="utf-8")
    openings = re.findall(r"<!-- FULL:([a-z-]+) -->", text)
    closings = re.findall(r"<!-- /FULL:([a-z-]+) -->", text)
    expected = ["form", *SECTIONS]
    if openings != expected or closings != expected:
        raise ValueError(f"{core.name}: expected matching blocks {expected}; got {openings} / {closings}")

    anchors = {core.resolve(): "protocol"}
    anchors.update({(refs / f"{name}.md").resolve(): name for name in SECTIONS})
    anchors.update({(refs / f"{name}.md").resolve(): anchor for name, anchor in ROLES})

    def rewrite_links(content: str, source: Path) -> str:
        def replace(match: re.Match[str]) -> str:
            label, target = match.groups()
            if target.startswith("#") or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                return match.group(0)
            resolved = (source.parent / target).resolve()
            if resolved not in anchors:
                raise ValueError(f"{source}: unsupported local link {target}")
            return f"[{label}](#{anchors[resolved]})"
        return LINK_RE.sub(replace, content)

    def include(match: re.Match[str]) -> str:
        name = match.group(1)
        if name == "form":
            return cfg["note"]
        source = refs / f"{name}.md"
        content = rewrite_links(source.read_text(encoding="utf-8").strip(), source)
        return f'<a id="{name}"></a>\n\n{content}\n'

    full = rewrite_links(text, core)
    full = INCLUDE_RE.sub(include, full)
    for (name, anchor), title in zip(ROLES, cfg["role_titles"]):
        source = refs / f"{name}.md"
        content = source.read_text(encoding="utf-8")
        marker = cfg["role_marker"] + "\n"
        if content.count(marker) != 1 or not content.split(marker, 1)[1].strip():
            raise ValueError(f"{source}: expected one nonempty full-role section")
        body = rewrite_links(content.split(marker, 1)[1].strip(), source)
        full += f'\n<a id="{anchor}"></a>\n\n## {title}\n\n{body}\n'
    full = '<a id="protocol"></a>\n\n' + full
    if "FULL:" in full:
        raise ValueError(f"{core.name}: unresolved include marker")
    present = re.findall(r'<a id="([^"]+)"></a>', full)
    if len(present) != len(set(present)):
        raise ValueError(f"{core.name}: duplicate internal anchor")
    for _, target in LINK_RE.findall(full):
        if target.startswith("#") and target[1:] not in present:
            raise ValueError(f"{core.name}: missing anchor {target}")
    return re.sub(r"\n{3,}", "\n\n", full).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("languages", nargs="*", metavar="LANG", help="zh, en, or all (default: all)")
    parser.add_argument("--check", action="store_true", help="check generated files without changing them")
    args = parser.parse_args()
    languages = args.languages or ["all"]
    if any(lang not in (*LANGS, "all") for lang in languages):
        parser.error("languages must be zh, en, or all")
    if "all" in languages and len(languages) > 1:
        parser.error("use 'all' alone, or select zh and/or en")
    languages = list(LANGS) if languages == ["all"] else list(dict.fromkeys(languages))
    try:
        # Validate every selected language before changing any output.
        outputs = [(ROOT / LANGS[lang]["out"], build(lang)) for lang in languages]
        if args.check:
            stale = [path.name for path, content in outputs
                     if not path.is_file() or path.read_text(encoding="utf-8") != content]
            if stale:
                parser.exit(1, "Rebuild required: " + ", ".join(stale) + "\n")
        else:
            for path, content in outputs:
                path.write_text(content, encoding="utf-8")
        for path, content in outputs:
            print(f"{path.name}: {'current' if args.check else 'built'}, {len(content):,} characters, {len(content.encode('utf-8')):,} bytes")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
