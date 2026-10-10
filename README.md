# Codex Game Skills

面向 **OpenAI Codex** 的游戏开发技能库与工作室协作模板，覆盖创意、原型、设计、架构、实现、测试和发布准备。

**74 个技能 · 49 个角色配置 · 13 类代码规则 · 可复现的验证工具。**

[![Codex validation](https://github.com/lazyseacow/codex-game-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/lazyseacow/codex-game-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A project-local game-development skill collection for OpenAI Codex, with workflows, custom roles, design templates and executable validation helpers.

## 快速开始

克隆为新游戏项目，在仓库根目录启动 Codex：

```sh
git clone https://github.com/lazyseacow/codex-game-skills.git my-game
cd my-game
codex
```

也可以在 Codex 桌面应用或 IDE 中打开 `my-game` 文件夹。使用已有的 Codex 账号、模型和权限设置。

向 Codex 发送：

```text
使用 $start 帮我开发一个 Godot 2D 游戏。
```

或者直接执行具体工作流：

```text
使用 $prototype 做一个单文件 HTML 躲避障碍原型，验证移动和碰撞。
使用 $setup-engine 配置我已安装的 Godot 版本。
使用 $dev-story 实现 production/epics/<项目>/story-001.md，并验证。
使用 $smoke-check 检查当前游戏，记录实际运行证据。
```

技能通过 `.agents/skills/` 自动发现，用 `$技能名` 明确调用。如果当前会话没有显示新技能，重新打开会话。

**这是项目级技能包。** 技能依赖 `.codex/` 中的角色、文档、模板和配置工具；不要只把某个 `SKILL.md` 复制到全局技能目录。接入已有游戏项目时，合并 `.agents/skills/`、`.codex/`、`docs/engine-reference/` 和根项目指令，并保留项目已有配置。完整接入说明见 [中文指南](docs/CODEX.md)。

## 开发路线

小型项目的最小正式开发路线：

```text
$start → $setup-engine → $brainstorm → $create-stories
                                      ↓
                          $dev-story → $story-done
                                      ↓
                                $smoke-check
```

`$prototype` 可以独立验证一个玩法或技术问题。`$help` 根据项目状态推荐下一步；已有游戏可用 `$adopt` 做现状检查。复杂项目可通过 `$settings` 提高 rigor，加入系统设计、架构、冲刺和团队评审。

## 技能目录

| 工作流 | 技能 |
| --- | --- |
| 入门与配置 | `$start`、`$help`、`$project-stage-detect`、`$setup-engine`、`$adopt`、`$settings` |
| 游戏设计 | `$brainstorm`、`$map-systems`、`$design-system`、`$quick-design`、`$review-all-gdds`、`$propagate-design-change` |
| 美术与体验 | `$art-bible`、`$asset-spec`、`$asset-audit`、`$ux-design`、`$ux-review` |
| 架构 | `$create-architecture`、`$architecture-decision`、`$architecture-review`、`$create-control-manifest` |
| 开发与计划 | `$create-epics`、`$create-stories`、`$dev-story`、`$story-done`、`$story-readiness`、`$estimate`、`$sprint-plan`、`$sprint-status` |
| 评审与分析 | `$design-review`、`$code-review`、`$balance-check`、`$content-audit`、`$scope-check`、`$perf-profile`、`$tech-debt`、`$gate-check`、`$consistency-check`、`$security-audit` |
| QA 与测试 | `$qa-plan`、`$smoke-check`、`$soak-test`、`$regression-suite`、`$test-setup`、`$test-helpers`、`$test-evidence-review`、`$test-flakiness`、`$skill-test`、`$skill-improve` |
| 生产管理 | `$milestone-review`、`$retrospective`、`$bug-report`、`$bug-triage`、`$reverse-document`、`$playtest-report` |
| 发布准备 | `$release-checklist`、`$launch-checklist`、`$changelog`、`$patch-notes`、`$hotfix`、`$day-one-patch` |
| 原型与内容 | `$prototype`、`$vertical-slice`、`$onboard`、`$localize` |
| 团队协作 | `$team-combat`、`$team-narrative`、`$team-ui`、`$team-release`、`$team-polish`、`$team-audio`、`$team-level`、`$team-live-ops`、`$team-qa` |

完整技能文件见 [`.agents/skills/`](.agents/skills)。

## 引擎与角色

| 开发目标 | 主要角色 | 运行要求 |
| --- | --- | --- |
| Godot 4 | `godot-specialist`，GDScript/C#/Shader/GDExtension 专家 | 安装对应 Godot 版本及测试工具 |
| Unity | `unity-specialist`，DOTS/Shader/Addressables/UI 专家 | 安装对应 Unity 编辑器及构建工具 |
| Unreal Engine 5 | `unreal-specialist`，GAS/Blueprint/Replication/UMG 专家 | 安装对应 Unreal 编辑器及构建工具 |
| HTML 原型 | `prototyper`、`gameplay-programmer`、`qa-tester` | 浏览器；自动化测试按需使用 Node.js |

49 个角色覆盖总监、部门负责人和专项开发人员。原生配置位于 [`.codex/agents/`](.codex/agents)，便携角色说明位于 [`.codex/roles/`](.codex/roles)。所有角色继承当前会话的模型与 reasoning 设置。

子代理调用取决于宿主能力和当前授权；工具不可用时，工作流可以顺序执行角色步骤，并明确说明评审方式。

## Codex 工作方式

- `AGENTS.md` 提供项目指令，技能入口位于 `.agents/skills/`。
- 配置解析、构建、测试和观察使用宿主实际可用的工具，并记录真实结果。
- `.codex/rules/` 是按路径读取的开发规则；执行权限由 Codex 宿主配置控制。
- 已授权的实现请求允许完成必要的本地修改；重大未定设计选择仍由用户决定。
- 团队工作流使用获授权的子代理，或顺序执行角色步骤。

完整约定见 [Codex runtime](.codex/docs/codex-runtime.md)。

## 配置

`project.yaml` 保存团队共享配置；`project.local.yaml` 保存被 Git 忽略的个人偏好。配置解析包含本地覆盖、默认值与 rigor 展开：

```sh
bash .codex/scripts/yaml-helper.sh resolve_config
```

在 Codex 中查看或修改：

```text
$settings
$settings modes.rigor=standard
$settings --local modes.review_mode=solo
```

`minimal` 适合快速原型和小项目，`standard` 增加设计及测试约束，`full` 提供完整追踪和评审。引擎版本及构建/测试命令应与实际安装环境一致。

## 验证

技能库验证需要 **Python 3.11+ 和 Bash**，不需要第三方 Python 库：

```sh
python3 tools/sync_roles.py --check
python3 tools/validate_codex.py
python3 -m unittest discover -s tests/codex -v
git diff --check
```

[GitHub Actions](https://github.com/lazyseacow/codex-game-skills/actions/workflows/validate.yml) 配置了 Linux/macOS 检查。可选的真实 Codex 检查使用当前登录及模型，会消耗账号用量；需要 Node.js：

```sh
python3 tools/verify_codex_live.py --workspace .scratch/live-check
```

2026-10-10 的本地验证结果：

| 检查 | 结果 |
| --- | --- |
| 74 个技能、49 个角色配置、引用及脚本 | 通过 |
| 技能库回归测试 | 11 项通过 |
| 真实 Codex 会话生成 HTML 游戏 | 完成，实际执行配置解析与角色步骤 |
| HTML 游戏逻辑测试 | 14 项通过 |
| Playwright + Chrome 浏览器检查 | 移动、松键、碰撞、计时冻结、重开通过；桌面/手机布局无溢出 |

这些结果验证了技能库和 HTML 原型路线。Godot/Unity/Unreal 的引擎运行、原生角色的子代理调用、触屏玩法和人工趣味评估仍未验证。临时游戏、截图、运行日志及本机配置不随仓库发布。详见 [验证指南](docs/CODEX.md#验证)。

## 项目结构

```text
AGENTS.md                     项目指令
.agents/skills/               技能及分阶段参考
.codex/roles/                 角色说明维护源
.codex/agents/                原生角色 TOML
.codex/docs/                  工作流文档和设计模板
.codex/rules/                 按路径读取的开发规则
.codex/scripts/               配置与项目观察工具
project.yaml                  团队共享配置
tools/                        原生角色同步和验证工具
tests/codex/                  可执行回归测试
tests/skills/                 技能与角色行为评估规范
```

技能、规则、文档和脚本直接维护。角色说明更新后运行 `python3 tools/sync_roles.py` 同步 TOML。升级时合并游戏项目的定制，见 [贡献说明](CONTRIBUTING.md) 和 [升级说明](UPGRADING.md)。

## 来源与许可证

本项目基于 [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) 修改而来，原作者为 **Donchitos**。技能工作流、角色说明、模板及部分工具沿用了原项目内容，并进行了 Codex 运行方式、目录结构、配置解析和验证工具的修改。

保留原作者 `Copyright (c) 2026 Donchitos` 及完整 [MIT License](LICENSE)。详细来源与修改说明见 [NOTICE](NOTICE)。复制或分发相关内容时，须一并保留版权和许可声明。

问题反馈请使用 [本仓库 Issues](https://github.com/lazyseacow/codex-game-skills/issues)。
