# Changelog

All notable changes to this skill will be documented in this file.

## [1.0.0] - 2026-09-13

### Added

- 首版发布：小红书违禁词离线检测 skill
- `references/prohibited-words.md`：7 大类违禁词库（实测硬词 / 外部平台名 / 极限词 / 价格诱导 / 导流话术 / 账号禁区词 / 强制标注项），含入库/出库维护机制
- `scripts/check_prohibited.py`：纯离线扫描脚本（零依赖），只扫「标题+正文」段避免误报，退出码 0=PASS / 1=有硬词 / 2=错误
- 违禁词来源：2026-09-12/13 实测限流（白嫖/0元/¥0/免费×≥2/官方连用/答案PDF+主页群/LinkedIn 等）+ 小红书社区规范通用违禁词
