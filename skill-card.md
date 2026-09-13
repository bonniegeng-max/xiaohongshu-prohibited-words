## Description:

xiaohongshu-prohibited-words is an offline prohibited-word detector for Xiaohongshu posts. It provides a local word list and a zero-dependency Python scanner that flags hard-blocked words before publishing, with an in/out maintenance mechanism to keep the list current without over-blocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Creators and agent users run this skill before publishing Xiaohongshu notes to catch prohibited or sensitive words that could trigger shadow-limiting, takedown, or rejection. It is the single source of truth for the prohibited-word list, shared by free-course-share and xiaohongshu-content-workflow.

### Deployment Geography for Use:

China (Xiaohongshu platform)

## Known Risks and Mitigations:

Risk: A prohibited-word list is never complete, and platform rules change over time.

Mitigation: The word list has an explicit in/out maintenance mechanism (add on verified triggers, downgrade/remove on false positives, prune on rule changes). Re-check before each publish.

Risk: Over-blocking legitimate words reduces normal expression space.

Mitigation: The list is graded P0/P1/P2, and only P0 blocks publishing; P1/P2 are advisory. Words are added only with a verified trigger, date, and reproducible scenario.

Risk: The scanner only checks text fields (title/body/tags), not cover image OCR.

Mitigation: Cover images must be checked separately for OCR-sensitive words; the word list documents which words are especially sensitive in cover OCR.

## Reference(s):

- [Prohibited word list](references/prohibited-words.md)
- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/xiaohongshu-prohibited-words)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Files]

**Output Format:** [Markdown and text guidance with inline shell commands, plus a scan report from the local script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 only; the scanner uses the standard library with zero third-party dependencies.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
