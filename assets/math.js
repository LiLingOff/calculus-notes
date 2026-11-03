// 以 KaTeX 渲染頁面中的 $...$（行內）與 $$...$$（獨立行）公式
renderMathInElement(document.body, {
  delimiters: [
    { left: "$$", right: "$$", display: true },
    { left: "$", right: "$", display: false }
  ],
  throwOnError: false
});
