# Learning Notes

以 Typst 撰寫線性代數、量子計算及相關主題的筆記，以 HTML 閱讀。
Human writing first；需要協作時呼叫 **Agent View & Extend**。

## 編輯與預覽

需要 Typst **0.15.1** 與 Python **3.9+**，不需額外 Python 套件。

```sh
python3 scripts/preview.py
```

開啟 <http://127.0.0.1:8000>。用 VS Code、Vim 等編輯 `notes/*.typ`，
儲存後會重新編譯；刷新瀏覽器即可閱讀。Ctrl-C 結束預覽。
`notes/getting-started.typ` 是可刪除的顯示範例，不是你的學習紀錄。

新增章節：建立 `.typ` 檔案，再於 `index.typ` 加入 `#include`。
標題、公式、label 與引用都使用正常 Typst 語法。

只建置與檢查：

```sh
python3 scripts/build.py
python3 scripts/check_site.py
```

輸出為 `_site/index.html`，CSS 使用相對路徑，適用 GitHub Pages 的專案網址。
Typst HTML 仍是實驗功能；本專案固定版本並以實際公式確認輸出。
建置檢查不能證明數學正確，也不能取代瀏覽器的視覺檢查。

## 與 Agent 協作

在這個工作目錄啟動 Agent，並說：

> Agent View & Extend：讀 notes/getting-started.typ 的「正交投影」，幫我補足說明。

Agent 依 `AGENTS.md` 載入 [skill](skills/agent-view-extend/SKILL.md)。
意圖清楚就直接補寫；有影響數學意義的歧義才對話。
skill 的執行不會自動 commit 或發布，也沒有已實作的 GUI 按鈕。

此環境禁止寫入 `.agents/`，所以 skill 目前放在 `skills/`，由
`AGENTS.md` 路由；尚未安裝為原生 skill 選單項目。

## GitHub Actions 與 Pages

初次設定，在此目錄的 terminal 執行：

```sh
python3 scripts/setup_github.py
```

腳本先建置與檢查，再以目前 gh 帳號建立公開的 `learning-notes-typst`，
初始化 Git、提交專案、推送 `main`、啟用 Actions-based Pages 並觸發部署。
需要 gh 已登入、Git 已設定姓名／email，以及 repository 建立與 workflow 權限。
若同名 repository 已存在且本地未連接它，腳本停止，不會覆寫它。
第一次推送後會設定 Pages，再明確觸發一次 workflow，避免首次設定的競態。
失敗後可重跑；完成與否仍以 Actions 結果為準。

也可手動建立公開 repository 並推送，再於 **Settings → Pages →
Build and deployment → Source** 選 **GitHub Actions**。

之後照常使用：

```sh
git add notes/ index.typ
git commit -m "Update learning notes"
git push
```

`main` 的 push 會編譯、檢查並部署 Pages；PR 只建置與檢查。
失敗的 build 不會覆蓋前次成功部署。也可在 Actions 手動執行 workflow。
不需額外儲存 GitHub token，workflow 使用內建 `GITHUB_TOKEN`。

本機尚未連接遠端時，不能把這些設定視為已上線；請以 Actions 成功結果
與實際 Pages 網址為準。
