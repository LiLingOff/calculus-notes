// 以 KaTeX 渲染頁面中的 $...$（行內）與 $$...$$（獨立行）公式
renderMathInElement(document.body, {
  delimiters: [
    { left: "$$", right: "$$", display: true },
    { left: "$", right: "$", display: false }
  ],
  throwOnError: false
});

// 列印時展開練習題的折疊詳解，印完再收回原狀
let closedDetails = [];
window.addEventListener("beforeprint", () => {
  closedDetails = [...document.querySelectorAll("details:not([open])")];
  closedDetails.forEach(d => { d.open = true; });
});
window.addEventListener("afterprint", () => {
  closedDetails.forEach(d => { d.open = false; });
  closedDetails = [];
});
