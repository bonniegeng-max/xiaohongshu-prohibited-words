## Description:

xiaohongshu-prohibited-words is an offline publish-time safety gate for Xiaohongshu posts. It uses a local word list and a zero-dependency Python scanner to catch hard-blocking wording before release, making it easier to stop risky posts before they are published.

Core value:
- Offline word-risk scan
- Clear PASS / FAIL boundary for publishing
- Canonical word-risk source for larger Xiaohongshu workflows

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Creators and agent users run this skill before publishing Xiaohongshu notes to catch prohibited or sensitive words that could trigger shadow-limiting, takedown, or rejection. It works both as a standalone checker and as the canonical word-risk layer inside larger Xiaohongshu workflows.

### Deployment Geography for Use:

China (Xiaohongshu platform)

## Known Risks and Mitigations:

Risk: A prohibited-word list is never complete, and platform rules change over time.

Mitigation: The word list has an explicit in/out maintenance mechanism. Re-check before each publish and update the list with verified trigger evidence.

Risk: Over-blocking legitimate words reduces normal expression space.

Mitigation: The list is graded P0/P1/P2, and only P0 blocks publishing; P1/P2 are advisory.

Risk: The scanner checks text fields only, not every possible media surface such as image OCR.

Mitigation: Use this as the text-risk gate, and pair it with broader preflight review when image or workflow-level checks are required.

## Reference(s):

- [Prohibited word list](references/prohibited-words.md)
- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/xiaohongshu-prohibited-words)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Files]

**Output Format:** [Markdown and text guidance with inline shell commands, plus a scan report from the local script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 only; the scanner uses the standard library with zero third-party dependencies.]

## Skill Version(s):

1.0.0

## Ethical Considerations:

Users should review both the scan result and the release context before publishing, and apply their own safety, compliance, and content-governance requirements.

