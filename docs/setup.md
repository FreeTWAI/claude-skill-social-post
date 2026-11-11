# Setup

## 1. Install Skill

Clone the repository and copy the `social-post/` directory to one of the following locations:

- **Codex:** `~/.codex/skills/social-post/`
- **Claude Code:** `~/.claude/skills/social-post/`

For Windows PowerShell (Codex):

```powershell
git clone https://github.com/Hao0321/claude-skill-social-post.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse ".\claude-skill-social-post\social-post" "$env:USERPROFILE\.codex\skills\social-post"
```

For macOS/Linux (Bash):
```bash
git clone https://github.com/Hao0321/claude-skill-social-post.git
mkdir -p ~/.claude/skills
cp -r claude-skill-social-post/social-post ~/.claude/skills/social-post
```

## 2. Create Private Work Files

In the installed `social-post/` directory, run:

```bash
cp style_profile.example.md style_profile.md
cp content_plan.example.md content_plan.md
```

*(For Windows PowerShell, use `Copy-Item` instead of `cp`.)*

這兩個檔案與日後建立的 `data/` 都不應提交到公開 fork。

## 3. 初始化語氣與內容計畫

依序告訴 agent：

```text
幫我學 FB 風格
幫我排 14 天社群內容
```

如果要從已登入的社群頁面讀貼文或實際發布，環境還需要可控制瀏覽器的工具。規劃、撰稿與數據分析不需要瀏覽器。

## 4. 發布安全閘

告訴 agent「今天發一篇」後，它會先產出各平台草稿。送出前應該：

1. 顯示完整正文。
2. 核對平台與目前登入帳號。
3. 取得當前對話中的明確確認。

未確認就不發布，也不代為登入、切換隱私或刪除貼文。

## 5. Log Outcome Analytics

From the repository root directory, first copy the example bundle and update it with your own data:

```bash
cp social-post/references/outcome-bundle.example.json my-outcome.json
python social-post/scripts/log_outcome.py my-outcome.json
```

The first script run is a dry-run. Once you confirm the contents, write them:

```bash
python social-post/scripts/log_outcome.py my-outcome.json --write
python social-post/scripts/social_data.py validate
```

When appending snapshots for the same post later, you can omit the `post` block in the bundle and only provide the new `snapshot`; older snapshots won't be overwritten.

## 6. Compare Series and Rules

```bash
python social-post/scripts/social_data.py summary --series your-series-id
python social-post/scripts/build_rule_registry.py --write
python social-post/scripts/self_test.py
```

只比較 maturity 接近的快照。若故事、首幀、文案與發布時間一起改變，必須列為 confound，不能稱為乾淨 A/B。

## Troubleshooting

- `invalid published_at`：時間需使用 ISO 8601 並包含 offset，例如 `2026-08-11T19:49:00+08:00`。
- `unknown post_id`：首次寫入需要 `post`＋`snapshot`；追加快照才可省略 `post`。
- 發到錯帳號風險：發布前截圖或讀取 compose 畫面，讓使用者確認帳號。
- 平台 UI 改版：重新讀取當下 DOM／accessibility state，更新對應平台 reference 或 `references/chrome-comment-adapter.md`；不要把舊 CSS selector 當成長期合約。
- P5 掃描被拒絕：先用 `browser-scan-request` 把當前 session、帳號、貼文與期限寫入本機 ledger，再讓 scan receipt 回綁輸出的 request ID；不可讓 Chrome 自己宣告 scope。
