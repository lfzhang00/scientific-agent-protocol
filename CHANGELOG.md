# Changelog

## 2.2 — 2026-11-28

- 新增可选角色：靶点研究策划专家（`target_research_planner`），中英文提示词作为可选文件分发，不内嵌完整单文件版。
- 工程与交付规范新增“总览唯一入口”：每个课题 `00_总览/` 只保留一个 `index.html`，更新同一入口，不在总览目录并列首页、版本页或备份。
- 核心协议升 2.2；中英核心、完整版、README 同步。

## 2.1.1 — 2026-11-27

打包与许可补丁；协议正文与 2.1 相同。Packaging and licensing patch; protocol text unchanged from 2.1.

- 代码 `build_full.py`、`scripts/package.sh` 使用 MIT；文档使用 CC BY 4.0。
- 新增 `LICENSE`、`LICENSE-docs`、`THIRD_PARTY.md`。
- 中英文 README 增加依赖、许可、打包说明。
- 新增 `scripts/package.sh`；`dist/` 加入 `.gitignore`。

## 2.1 — 2026-11-27

- 新增链接规则：PMID、DOI、数据、文档、项目文件引用必须可点击；生成内容不留裸编号。
- 重建中英文完整版，同步 README 与项目副本。
