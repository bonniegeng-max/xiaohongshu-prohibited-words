## Description:

Checks Xiaohongshu draft titles, body text, and tags against a locally maintained list of prohibited and sensitive terms before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Xiaohongshu creators and their agents use this skill to check Chinese-language drafts for potentially restricted wording and review suggested edits before publishing. They can maintain the local wordlist as platform practices change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outdated platform rules or wordlist entries can produce false positives or miss restricted wording.

Mitigation: Review flagged text and regularly update the wordlist against observed platform outcomes before relying on a publication recommendation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bonniegeng-max/skills/xiaohongshu-prohibited-words)
- [Prohibited-words reference list](references/prohibited-words.md)
- [Wordlist section configuration](references/sections.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text scan report with severity-ranked matches, suggested edits, and publication-check reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A clear result indicates no P0 matches, not guaranteed platform approval; missing wordlist data blocks a clear result.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
