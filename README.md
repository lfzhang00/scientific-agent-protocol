# 科研双智能体协作与反馈控制协议（v2.1）

[English](README.en.md)

本仓库是协议的测试、构建与分享工作区。中文版默认加载 `AGENTS.md`，英文版加载 `AGENTS.en.md`；`references/` 与 `references/en/` 按需读取，`build_full.py` 生成中英两种单文件版。当前发行包：v2.1.1（协议正文 2.1；许可与打包补丁）。

## 文件

| 路径 | 作用 |
| --- | --- |
| `AGENTS.md` | 中文核心协议（v2.1），日常默认加载 |
| `AGENTS.en.md` | 英文核心协议（v2.1） |
| `references/roles.md` | 中文字智能体 A/B 提示词 + 本轮任务包 |
| `references/skill-routing.md` | 中文技能检测、阶段路由表、缺失处理 |
| `references/background.md` | 中文可选研究背景模板 |
| `references/en/roles.md` | 英文字智能体 A/B 提示词 + 本轮任务包 |
| `references/en/skill-routing.md` | 英文技能检测、阶段路由表、缺失处理 |
| `references/en/background.md` | 英文可选研究背景模板 |
| `build_full.py` | 由核心 + references 生成中英单文件版 |
| `AGENTS.full.md` | 中文完整单文件版（生成，不手改） |
| `AGENTS.en.full.md` | 英文完整单文件版（生成，不手改） |
| `README.en.md` | 英文说明 |
| `LICENSE` | 代码 MIT 许可 |
| `LICENSE-docs` | 文档 CC BY 4.0 许可 |
| `THIRD_PARTY.md` | 第三方名称与依赖声明 |
| `CHANGELOG.md` | 版本变更 |
| `scripts/package.sh` | 生成 `dist/` 发布 zip |

## 构建

```bash
python3 build_full.py        # 同时生成中文和英文完整版
python3 build_full.py zh     # 只生成中文
python3 build_full.py en     # 只生成英文
```

检查输出：两版 full 均无 `FULL:` 标记，且无对应语言的 `references/*.md` 指针。当前尺寸：

- 中文核心：5,780 字符 / 14,395 bytes；中文完整版：9,564 字符 / 24,915 bytes。
- 英文核心：18,198 字符 / 18,217 bytes；英文完整版：31,278 字符 / 31,307 bytes。

英文是翻译，字符数与中文不可直接比较；默认仍只加载中文核心，英文版用于英文协作者或英文交付。英文版保留了原项目“默认使用简体中文讨论”的设定；英文团队使用时可自行修改 `AGENTS.en.md` 中该句。

## 依赖

- 构建：Python 3.8+，仅标准库（`re`、`sys`、`pathlib`）；无第三方 Python 包。
- 打包：`git` 与 `git archive`；无额外依赖。
- 路由表提到的 skills 均为可选，不随仓库分发；缺失时按协议使用内置降级流程。

## 打包

- 发布包由 GitHub Releases 提供；本地可运行 `scripts/package.sh v2.1.1` 生成 `dist/scientific-agent-protocol-v2.1.1.zip`。
- 脚本要求对应 tag 已存在；先推送 tag。

## 修改流程

1. 只改 `AGENTS.md`、`AGENTS.en.md` 或对应的 `references/*.md`；两个 `*.full.md` 由脚本生成，不手改。
2. 运行 `python3 build_full.py`。
3. 按上面的检查项验证；需要分享时发送对应的 `*.full.md`。
4. 同步到项目：中文版复制 `AGENTS.md` + `references/`；英文版复制 `AGENTS.en.md` + `references/en/`。完整版只在一次性使用或跨助手分享时使用。

## 许可

- 代码（`build_full.py`、`scripts/package.sh`）：MIT，见 `LICENSE`。
- 文档（`AGENTS*.md`、`README*.md`、`references/**`、`CHANGELOG.md`、`THIRD_PARTY.md`）：CC BY 4.0，见 `LICENSE-docs`。
- 第三方 skill 名称仅用于路由引用；本仓库不打包其内容/代码，见 `THIRD_PARTY.md`。

## 说明

- 核心与 references 的衔接靠 HTML 注释标记 `<!-- FULL:name -->`；改标记名时同步改 `build_full.py`。
- 旧版本已移出工作区；后续版本历史由 git 提交记录保存。
- 本仓库默认分支为 `main`，默认 README 为中文。
