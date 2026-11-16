= 開始寫筆記 <getting-started>

這是可刪除的示範章節，用來確認中文、公式、證明與引用的 HTML 顯示。
它不是作者已完成的學習紀錄。你可以直接將這個檔案換成自己的筆記。

== 正交投影 <orthogonal-projection>

在複數向量空間中，令 $u^dagger u = 1$，定義

$ P = u u^dagger. $ <projection-operator>

其中 $dagger$ 表示共軛轉置。@projection-operator 所定義的算符滿足

$
  P^2 &= u (u^dagger u) u^dagger = u u^dagger = P, \\
  P^dagger &= (u u^dagger)^dagger = u u^dagger = P.
$

因此 $P$ 是投影到 $u$ 所張成子空間的正交投影算符。
條件 $u^dagger u = 1$ 在第一行推導中不可省略。

== 一個量子計算的連結 <quantum-connection>

取 $u = vec(1, 0)$，則

$ P = mat(1, 0; 0, 0). $

若量子態 $psi = vec(alpha, beta)$ 已歸一化，則
$abs(alpha)^2 + abs(beta)^2 = 1$。
測量對應於 $P$ 的結果，其機率為

$ p = psi^dagger P psi = abs(alpha)^2. $

當 $p > 0$ 時，該結果發生後的態為 $P psi / sqrt(p)$。
這把 @orthogonal-projection 的線性代數概念連到了量子測量。

== 我的下一個問題

在此用自己的話寫下理解或問題，也可以留下 Typst 註解。
需要協作時，在 Agent 對話中指定本檔案與章節，呼叫 Agent View & Extend。
