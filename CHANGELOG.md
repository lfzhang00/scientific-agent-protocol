# Changelog

## 3.1 — 2026-11-28

- 新增 `12_分享/` 与“单文件分享版”规范：阶段性/最终 HTML 成果同步生成 `<课题名>_研究摘要.html`，单文件离线可读；补充内容取舍、表格精简、资源内嵌、来源链接、5 MB 体积目标、职责一致性、入口维护与交付验证。
- 工程与交付规范目录加入 `12_分享/`；核心升 3.1。
- `target-research-planner.md` / `statistical-design-inference.md` 升 2.1：靶点提示词加入分享版交付，统计提示词加入分享版统计口径核对；中英同步。
- 中英核心、完整版、README、CHANGELOG、打包脚本同步 3.1。

## 3.0 — 2026-11-28

- 角色体系升级为三专家：BioInfo、BioLab、BioStats 常设平级；BioStats 默认独立把关生信与湿实验的统计设计、推断与报告，不以用户点名或技能命中为前提。
- 新增 `references/statistical-design-inference.md`（中英）统计设计与推断角色提示词；`target-research-planner.md` 升级 v2.0，BioTarget 明确为 BioInfo 可选专项。
- 核心标题、角色表、协作流程、最终输出同步为三专家；中英核心升 3.0，完整版与 README 重建。
- 不打包旧 `prompts/bioinfo-wetlab.md` 与 `share/` 安装器。

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
