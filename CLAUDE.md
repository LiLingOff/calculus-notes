# 微積分講義網頁

把使用者給的 AP Calculus I 講義 PDF 轉成「概念講解＋題目＋緊接詳解」的靜態網頁。純閱讀頁，不加側欄、按鈕、摺疊等 UI。

## 結構
- `index.html`：目錄，每週一行 `<li>`
- `template.html`：新講義頁的骨架，含所有可用區塊
- `assets/style.css`：共用樣式（含深色模式、列印）
- `assets/math.js`：KaTeX auto-render 設定，`$...$` 行內、`$$...$$` 獨立
- `tools/svgplot.py`：畫函數圖的工具，輸出 SVG
- `weekNN/index.html`：各週講義；`weekNN/figs.py` 產生該週的 `fig-*.svg`
- `exams/`：考古題與作業詳解，每份一頁（`112-mid.html`、`1101-mid-a.html`、`hw1.html`…）；`exams/figs.py` 產生全部的 `fig-<考卷>-q<題>.svg`
- `source/`：原始 PDF，在 `.gitignore` 裡，不進 repo（repo 是公開的，不能推上去）
  - `lecture-notes/`：課堂講義，檔名 `115 AP_Calculus I Lecture Note N.pdf`（有改版也照這個名字覆蓋）
  - `past-exams/`：歷屆考古題與解答
  - `hw/`：作業相關

## 新增一份講義
講義 PDF 放進 `source/lecture-notes/`。
1. 讀 PDF：`pdftoppm` 沒裝，用 pypdf 抽文字
   `python -I -c "import pypdf,sys;r=pypdf.PdfReader(sys.argv[1]);[print('=====PAGE',i+1,'\n',p.extract_text()) for i,p in enumerate(r.pages)]" "<pdf 路徑>"`
   題目要看圖時（例如從圖形比大小），用 PyMuPDF 把頁面轉成 PNG 再看：
   `python -I -c "import fitz,sys;d=fitz.open(sys.argv[1]);d[int(sys.argv[2])-1].get_pixmap(dpi=150).save(sys.argv[3])" "<pdf>" <頁碼> <輸出.png>`（輸出放 scratchpad）
2. 複製 `template.html` 到 `weekNN/index.html`（NN 兩位數），依講義章節順序寫：
   每節先白話講概念與公式，再列講義中所有 Example / Exercise 為「題 n」，詳解直接接在題目後面。
3. 每題自己驗算，講義給的 Ans 也要核對；講義有筆誤就放進頁首 `.erratum`，題目旁也註明。
4. 需要圖時寫 `weekNN/figs.py`（參考 `week04/figs.py`），執行 `python weekNN/figs.py` 產生 SVG，用 `<img>` 嵌入。
   適合畫圖的：割線切線、不可微點、夾擠、切線法線、面積等幾何直覺。
   每個有節號的 h2/h3 加 `id`，規則是 `s` 加節號、點換成連字號（`<h2 id="s2-2">`、`<h3 id="s5-4-1">`），
   本週必背總整理用 `id="summary"`。首頁主題路線靠這些 id 跳轉。
   每題的 `section.q` 加 `id="qN"`（N 是題號），考古題頁引用講義例題時靠它跳轉。
5. 在 `index.html` 加一行週次目錄，並把新內容併入下方「主題複習路線」：
   延續既有主題的小節補進該段的連結；新主題就照先備關係插入新段，寫出「先讀」段號（插入後其他段的「先讀」號碼要跟著改）。
   講義 (*) 內容與證明加 `<span class="lv">延伸</span>`。
6. 用瀏覽器開頁面檢查：KaTeX 無紅字錯誤、圖正常、手機寬度無水平捲動。
   預覽用 preview_start `calculus`（`.claude/launch.json`，port 8766），
   開 `http://localhost:8766/weekNN/index.html`。不要用 file:// 開，預覽窗格會變成靜態快照、相對路徑載不到。
7. 上線：見下方「上線」。

## 新增一份考古題或作業
PDF 放進 `source/past-exams/` 或 `source/hw/`。
1. 先列出題目清單和每題對應的主題路線段號給使用者確認，再開始寫。
2. 頁面放 `exams/`，骨架照現有的考古題頁：頁首 `.erratum` 列官方解答錯誤（沒有就寫一句「逐題驗算過，沒有發現錯誤」），
   每小題一個 `section.q`，`id` 用 `q1a`、整題用 `q5`；題目下一行 `<p class="topic">` 寫「主題 N 名稱｜§x.y 連結」。
3. 詳解第一段用 `<strong>考點</strong>` 說這題考什麼、用什麼方法；官方跳步要補齊，有更快的做法放 `.tip`。
   證明題標「關鍵一步」，`.remark` 寫官方給分與常見失分。講義沒教的工具（羅必達、積分等）標 `<span class="lv">超出範圍</span>`，
   官方用羅必達但講義範圍內做得到的，改寫成講義做法。
   提到講義例題時寫成連結，例如 `<a href="../week02/index.html#q18">週二題 18</a>`。
4. 在 `index.html` 的「考古題與作業」加一行；再到主題路線對應段的 `<div class="ex">`（練習）的 `<ul>` 裡，
   一份考卷一個 `<li><a class="exam" href="exams/….html">卷名</a><span class="qs"><a href="exams/…#q1a">1(a)</a>…</span></li>`，
   該段還沒有練習區就照其他段新增。
5. 預覽檢查同講義；另外確認所有 `href` 的錨點都存在。

## 題目來源
題目只用講義本身的 Example / Exercise，以及講義寫成定理並附證明的內容（例如 tan 的導數）。
自己補充的內容放在講解或 `.remark`，不要混進題號。

## 上線
- 網站 https://lilingoff.github.io/calculus-notes/ ，GitHub Pages 直接送出 repo `LiLingOff/calculus-notes` 的 `main` 分支根目錄。commit 後 `git push` 就會上線，通常一兩分鐘。
- repo 是公開的，所有進 repo 的檔案都看得到。推之前用 `git status` 確認沒有 PDF 或其他不該公開的檔案。
- `.nojekyll` 讓 GitHub 不經 Jekyll 處理，原樣送出檔案，不要刪。
- 本機 `archive/server` 分支是搬家前的舊歷史，裡面有原始 PDF，永遠不要推送。
- 講義連結全用相對路徑，不要寫 `/` 開頭的絕對路徑（網站掛在 `/calculus-notes/` 底下）。

## Git
- commit 訊息不加 Co-Authored-By。

## 撰寫規則
- 繁體中文；不濫用破折號、不重複同一修辭、不用彎引號與翻譯腔。
- 使用者程度：上過課但基本沒聽，講解要從直覺講起，但不要囉嗦。
- LaTeX 裡的小於、大於用 `\lt`、`\gt`（避免 HTML 解析問題）；分段函數用 `cases`。
- 區塊 class：`.def` 定義、`.thm` 定理、`.remark` 補充、`.tip` 套路、`.erratum` 筆誤、
  `section.q` 包 `.problem` 與 `.solution`，答案用 `.ans`。兩張圖並排用 `figure.pair`。
