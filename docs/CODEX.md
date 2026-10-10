# Codex Game Skills — 游戏开发指南

本项目是面向 OpenAI Codex 的项目级游戏开发技能集合。

## 开始使用

```sh
git clone https://github.com/lazyseacow/codex-game-skills.git my-game
cd my-game
codex
```

也可以在 Codex 桌面或 IDE 中打开项目根目录。技能位于 `.agents/skills/`，
通过 `$技能名` 调用。新增技能未出现在当前会话时，重新打开会话。

```text
使用 $start 帮我开发一个 Godot 2D 游戏。
使用 $prototype 做一个 HTML 躲避障碍原型，验证移动与碰撞。
使用 $dev-story 实现 production/epics/<项目>/story-001.md 并验证。
```

## 接入已有项目

在独立目录克隆技能库后，将以下内容合并到游戏项目：

- `.agents/skills/`：技能及参考文件，同名技能须合并。
- `.codex/`：角色、规则、共享文档、设计模板及脚本。
- `docs/engine-reference/`：所选引擎的版本参考，核对实际安装版本。
- `AGENTS.md`：将工作流约定合并到现有项目指令。
- `project.yaml`：保留项目现有配置，补充所需字段。
- `tools/` 和 `tests/`：需要维护技能或执行集合验证时一并保留。
- `LICENSE` 和 `NOTICE`：保留版权、许可全文及来源说明。已有项目采用其他
  许可证时，将这两份文件保存到第三方许可目录（如
  `third_party/licenses/codex-game-skills/`），保留项目原有许可证。

相对路径以游戏项目根目录为基准。保留游戏设计、代码和生产状态。
Godot、Unity、Unreal 需要实际安装对应引擎及构建工具；HTML 原型可独立运行。

## 工作流与角色

最小正式开发路线为 `$setup-engine` → `$brainstorm` → `$create-stories` →
逐个运行 `$dev-story`、`$story-done`，再运行 `$smoke-check`。
`$prototype` 验证单个机制或技术问题，`$help` 根据当前文件推荐下一步。

74 个技能覆盖设计、架构、实现、QA 与发布。49 个角色的维护源在
`.codex/roles/`，原生 TOML 在 `.codex/agents/`。角色继承会话模型和推理设置。
宿主支持且授权时使用子代理，否则顺序执行角色步骤。

读取 `.codex/docs/codex-runtime.md` 了解授权、配置和验证约定。
项目规则是明确读取的指令，执行权限由宿主决定。工作流不会自行授权发布。

## 配置

`project.yaml` 保存共享配置，`project.local.yaml` 保存个人偏好并被 Git 忽略。

```sh
bash .codex/scripts/yaml-helper.sh resolve_config
```

使用 `$settings modes.rigor=standard` 设置流程深度。`minimal` 适合快速原型，
`standard` 增加设计与测试约束，`full` 提供完整追踪和评审。

## 验证

Python 3.11+ 与 Bash 即可执行集合验证，无第三方 Python 依赖：

```sh
python3 tools/sync_roles.py --check
python3 tools/validate_codex.py
python3 -m unittest discover -s tests/codex -v
git diff --check
```

检查技能 frontmatter、分阶段引用、角色 TOML 与维护源一致性、行为评估规范
目录和 Bash 语法。回归测试验证配置优先级、嵌套项目、非法枚举、故事排序、
真实文件扫描以及损坏的参考和角色文件识别。

可选的真实 Codex 检查使用当前账号与模型，会消耗其用量：

```sh
python3 tools/verify_codex_live.py --workspace .scratch/live-check
```

要求 `codex` 与 `node`，目标目录必须为空。它在隔离工作区真实执行 `$prototype`，
检查游戏、测试、配置执行证据和 checkpoint，然后独立重跑 Node 测试。
浏览器操作与人工趣味评估仍需另行验证。

HTML 原型路线已执行真实 Codex 会话、14 项游戏逻辑测试及浏览器移动、碰撞、
计时冻结、重开和布局验证。Godot/Unity/Unreal 引擎运行、49 个角色的原生
子代理调用、触屏玩法与人工趣味评估尚未验证。静态通过不能替代引擎运行。

## 维护

直接编辑技能、文档、规则和脚本。角色变更后运行 `python3 tools/sync_roles.py`，
再执行上述验证。升级时先合并 `AGENTS.md`、角色及配置的项目定制，
不要覆盖游戏资产或生产文件。详见根目录 `CONTRIBUTING.md` 和 `UPGRADING.md`。

## 来源与许可

本项目基于 [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) 修改，保留 Donchitos 的版权声明及 MIT 许可全文。来源版本和修改范围见根目录 `NOTICE`。分发相关文件时一并保留这些声明。
