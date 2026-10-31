# Social Post Skill Documentation

This document covers the skill prompts, supported platforms, parameter schemas, and output examples for the Social Post generation skill.

## Supported Platforms

*   Facebook
*   Instagram
*   Threads
*   YouTube
*   X (Twitter)

## Skill Prompts

### ChatGPT Chat
The ChatGPT Chat version of the skill is triggered by the following phrases:
*   "發文" (Publish)
*   "寫文" (Write post)
*   "文案" (Copywriting)
*   "用我的口氣／格式" (Use my tone/format)
*   "Mode C" (Mode C)
*   "黑底白字" (White text on black background)
*   "分析貼文" (Analyze post)

### Local Environment (Codex / Claude Code)
The local skill uses six modes to handle the social post lifecycle:
*   **P0 Plan:** Content planning and experimentation.
*   **P1 Learn Voice:** Learning local tone from authorized samples.
*   **P2 Draft / Publish:** Drafting content; publishing only after user confirmation in the current turn.
*   **P3 Log Outcome:** Saving posts, snapshots, account overviews, and corrections.
*   **P4 Optimize Patterns:** Cross-post/cross-platform comparisons after aligning maturity.
*   **P5 Comment Ops:** Chrome-controlled scanning, drafting, and approval (live replies require canary unlock).

## Parameter Schemas

The skill relies on JSONL structured data for canonical tracking. The primary schemas are:
*   `data/posts.jsonl`: Posts, captions, and publishing conditions.
*   `data/insight_snapshots.jsonl`: Snapshots of post insights.
*   `data/account_snapshots.jsonl`: Account period overviews (7/30/90 days).
*   `data/experiments.jsonl`: Cross-post hypotheses and confounds.
*   `data/corrections.jsonl`: Factual correction events.

## Output Examples

### Mode C: Long Form / Review (Threads)
(Contradiction/result/stance first. Clear structure: What we did -> What we found -> Why it matters -> Next steps. One action at the end.)

*   做麵包這五年，我才懂的三件事。
*   第一，發酵時間不能急。
*   第二，麵粉的溫度比水溫更重要。
*   第三，客人的回饋是最好的配方。
*   下週我們將推出全新法棍，敬請期待。
