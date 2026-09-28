# xiaohongshu-prohibited-words

> **一句话定位**：发布小红书内容前，先过这一道违禁词闸门。它不是泛泛的词库工具，而是一个发布前的硬性风险检查步骤。

> **小红书发布前违禁词闸门（离线）**
> **An offline publish-time safety gate for Xiaohongshu posts.**

---

## What it does

This skill scans Xiaohongshu draft text with a local prohibited-word list and a local Python script. It is designed to answer one release-time question: **can this post be safely published now, or does it still contain hard-risk wording?**

## Why it matters

A post can be limited, rejected, or suppressed even when the copy feels “basically fine.” This skill exists to stop that failure mode earlier. If P0 terms are still present, do not publish.

## Why people install it

- It is a publish-time gate, not just a reference list.
- It works offline when paid APIs are unavailable.
- It provides a clearer PASS / FAIL boundary.
- It can act as the canonical word-risk source inside a larger preflight workflow.

## Demo first

The proof this skill needs is not a pretty screenshot — it is a believable release gate:

- PASS: no hard-blocking terms remain
- FAIL: hard-blocking terms still exist and must be fixed before publish
- Wordlist maintenance: the source of truth stays explicit and auditable

## Quick start

```bash
# 从物料 md 扫描（只提取「## 标题」+「## 正文」两段，跳过审查记录避免误报）
python3 scripts/check_prohibited.py --file 笔记终稿.md

# 或直接传纯发布文案
python3 scripts/check_prohibited.py "标题" "正文" "标签"
```

退出码：`0` = 无 P0 硬词（PASS）；`1` = 有 P0 硬词需改；`2` = 运行错误。

**规则：P0 硬词未清空 = 禁止发布。**

## What makes it different

- **Offline-first:** no paid API dependency required
- **Publish-time framing:** it exists to stop bad releases, not just collect words
- **Single source of truth:** wordlist maintenance is part of the product
- **Workflow-safe:** can serve as the word-risk gate in a larger release flow

## Wordlist maintenance

The word list lives in `references/prohibited-words.md`. It should not be treated as a static dump. It must be maintained:

- add words only with verified trigger evidence
- downgrade or remove words when they become false positives
- prune outdated entries when platform rules shift

## Relationship to other skills

- used by `free-course-share`
- used by `xiaohongshu-content-workflow`
- can be used as the word-risk layer inside broader preflight checks

## License

MIT

