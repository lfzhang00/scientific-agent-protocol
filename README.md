# 科研多专家协作协议

[English](README.en.md)

这套提示词帮助 AI 助手分工审查科研问题。BioInfo、BioLab 和 BioStats 默认参与实质性科研任务；BioTarget 按需处理靶点研究策划。适合研究前期调研、数据解释、实验设计和方案修订。

| 角色 | 负责什么 |
| --- | --- |
| BioInfo | 数据来源、计算分析与生物学解释 |
| BioLab | 实验模型、干预设计与机制验证 |
| BioStats | 独立审查生信和湿实验两侧的设计、统计与推断 |
| BioTarget | BioInfo 的可选专项：靶点证据、表达定位、疾病切口与研究方案 |

## 开始使用

按使用场景选择一种方式。

### 用于一个项目

1. 将 [AGENTS.md](AGENTS.md) 和 `references/` 复制到项目根目录。已有 `AGENTS.md` 时合并规则，保留原有约定。
2. 英文团队可用 [AGENTS.en.md](AGENTS.en.md) 及 `references/en/`；若助手默认读取 `AGENTS.md`，将选用的英文核心另存为该文件名。
3. 新建聊天，或在已有聊天中要求助手重新读取项目规则，然后提供问题与材料。例如：

   > 请按项目协议评估 [研究问题]。已有材料是 [文件或证据]，本轮只完成 [范围]，交付 [成果]。时间和资源限制为 [条件]。

背景模板可选，不必先填完整表格。协议中的角色名是分工约定，能否实际调用子智能体取决于助手及其工具。无法委派时，助手应说明限制，按三个专业视角依次审查。

### 一次性使用或分享给其他助手

发送 [中文完整单文件版](AGENTS.full.md) 或 [English single-file edition](AGENTS.en.full.md)。两版均包含 BioInfo、BioLab、BioStats 和 BioTarget 的完整指令，无需附带 `references/`。第三方 skills 需由使用者所在环境提供。

## 默认流程与交付

协调者统一背景和证据，三个专家先独立评估，再交叉审查。BioStats 从设计阶段参与，在实验、主要分析和结论定稿前审查相关材料。遇到新证据或分歧时，更新受影响部分；文件操作、普通查询和提示词配置直接处理。

实际研究成果按章节生成 HTML。`00_总览/index.html` 是项目内唯一总览入口；`12_分享/<课题名>_研究摘要.html` 是可单独发送、离线打开的精简分享版，目标不超过 5 MB。完整数据、脚本和长表保留在项目内。仅使用或修改本协议不会自动生成研究报告。

BioTarget 保留 GTEx、CELLxGENE、Tabula Sapiens、HPA、UniProt，以及 GWAS Catalog、OMIM 等数据库的使用范围、证据来源和去重要求；按问题选择资源，不要求每次遍历全部数据库。

## 维护提示词

源文件与生成文件分开维护。

| 文件 | 用途 |
| --- | --- |
| `AGENTS.md`、`AGENTS.en.md` | 中英文核心协议 |
| `references/`、`references/en/` | 对应语言的角色、技能路由和背景模板 |
| `AGENTS.full.md`、`AGENTS.en.full.md` | 自动生成的完整单文件版，请勿直接编辑 |
| [build_full.py](build_full.py) | 展开核心、引用资料和两个专项角色提示词 |
| [scripts/package.sh](scripts/package.sh) | 从本地 Git 标签导出 ZIP |
| [CHANGELOG.md](CHANGELOG.md) | 版本记录 |

修改源文件后，用 Python 3.8 或更高版本重新生成：

```bash
python3 build_full.py       # 中英两版
python3 build_full.py zh    # 仅中文
python3 build_full.py en    # 仅英文
python3 build_full.py --check  # 检查已提交的完整版是否与源文件一致
```

构建只使用 Python 标准库。脚本检查引用资料、角色全文和内部链接；缺失时报告错误。中文版与英文版应同步修改，英文按自然表达改写，保留相同的角色关系、证据要求和执行范围。

交付前运行 `git diff --check`，检查生成文件，并搜索“不是……而是……”式对比、套话、过度强调、重复收尾和破折号等文风问题。搜索结果逐处判断，必要的科学限定和技术符号保留。

## 导出发布包

```bash
bash scripts/package.sh v3.2
```

标签须已在本地存在。脚本导出该标签对应的提交，输出到 `dist/`；未提交的修改不会进入包，也无需先推送标签。创建标签、提交或对外发布由维护者另行决定。

## 技能与许可

助手应先检查当前环境提供的 skills，读取匹配的 `SKILL.md`，再按阶段使用。协议不自动安装技能，也不固定安装目录；缺失时说明限制，采用适用的替代流程。

构建和打包代码采用 [MIT](LICENSE)；提示词与文档采用 [CC BY 4.0](LICENSE-docs)。第三方 skills 的内容和代码不随仓库分发，见[第三方说明](THIRD_PARTY.md)。
