= Linear Algebra in Complex Vector Spaces

== Preamble <complex-la-preamble>

從實數轉到複數，線性組合的規則並沒有改變；真正需要小心的是：
如何定義長度、內積，以及矩陣的轉置。本節先固定這些基本符號，
後續預設討論有限維空間，向量以 column vector 表示。

=== 複數與共軛

複數可以寫成 $z = a + b i$，其中 $a, b in RR$ 且 $i^2 = -1$。
本筆記以 $z^*$ 表示 scalar 的共軛（complex conjugate），以 $abs(z)$ 表示絕對值：

$ z^* = a - b i, quad abs(z) = sqrt(a^2 + b^2). $

共軛保留實部並反轉虛部的符號，因此

$
  z z^* &= (a + b i)(a - b i) = a^2 + b^2 = abs(z)^2, \\
  (z + w)^* &= z^* + w^*, \\
  (z w)^* &= z^* w^*.
$

特別是 $abs(z)^2$ 永遠是非負實數，且只有在 $z = 0$ 時等於零。
這個性質是複數向量長度的基礎。

=== 複數向量與線性組合

$CC^n$ 表示由 $n$ 個複數分量組成的向量空間。
若 $u, v in CC^n$ 且 $alpha, beta in CC$，則 $alpha u + beta v$ 仍在 $CC^n$ 中。
「複數向量空間」的意思也包含 scalar 可以取複數；只看向量寫了幾個分量還不夠。

例如在 $CC^1$ 中，$i = i dot 1$，所以 $1$ 與 $i$ 在複數 scalars 下線性相依。
但若將同一集合 $CC$ 視為實數向量空間，$a + b i = 0$ 對實數 $a, b$
只可能有 $a = b = 0$，故 $1$ 與 $i$ 在實數 scalars 下線性獨立。
因此 $CC$ 在 $CC$ 上的維度是 $1$，在 $RR$ 上的維度則是 $2$。

=== 轉置與共軛轉置

對矩陣 $A = (a_(j k)) in CC^(m times n)$，本筆記使用以下符號：

- $A^T$：轉置（transpose），交換 row 與 column。
- $A^*$：本筆記用星號表示逐項取共軛，不交換 row 與 column。
- $A^dagger = (A^*)^T$：共軛轉置（conjugate transpose，也稱 adjoint），兩者都做。

因此 $(A^dagger)_(j k) = a_(k j)^*$，而 $A^dagger in CC^(n times m)$。
例如

$
  A = mat(1, i; 2 + i, 3), quad
  A^T = mat(1, 2 + i; i, 3), quad
  A^dagger = mat(1, 2 - i; -i, 3).
$

當矩陣的元素都是實數時，$A^dagger = A^T$；一般複數矩陣則不能混用。另一些教材以 $A^*$ 表示 adjoint；
本筆記固定以 $A^dagger$ 表示 adjoint，星號只表示逐項共軛。
對維度相容的矩陣乘積，共軛轉置會反轉順序：

$ (A B)^dagger = B^dagger A^dagger, quad (A^dagger)^dagger = A. $

順序反轉來自轉置；逐項共軛本身不會反轉乘法順序。

=== 內積與長度：共軛為何不可省略？

對 $u, v in CC^n$，本筆記採用標準內積

$ chevron.l u, v chevron.r = u^dagger v = sum_(j=1)^n u_j^* v_j. $ <complex-inner-product>

這裡採用量子計算常見的慣例：*第一個引數共軛線性，第二個引數線性*。
也就是對 $alpha, beta in CC$，

$
  chevron.l alpha u + beta v, w chevron.r
    &= alpha^* chevron.l u, w chevron.r
      + beta^* chevron.l v, w chevron.r, \\
  chevron.l u, alpha v + beta w chevron.r
    &= alpha chevron.l u, v chevron.r + beta chevron.l u, w chevron.r.
$

有些教材將線性放在第一個引數，閱讀時要先確認慣例。
由 @complex-inner-product 可得共軛對稱性與正定性：

$
  chevron.l v, u chevron.r &= lr(chevron.l u, v chevron.r)^*, \\
  chevron.l u, u chevron.r &= sum_(j=1)^n abs(u_j)^2 >= 0.
$

第二式只有在 $u = 0$ 時等於零，因此可以定義 Euclidean norm：

$ norm(u) = sqrt(lr(chevron.l u, u chevron.r)), quad norm(alpha u) = abs(alpha) norm(u). $

若直接沿用實數的 $u^T v$，非零向量可能得到零「長度平方」。
例如取 $u = vec(1, i)$，則

$ u^T u = 1 + i^2 = 0, quad u^dagger u = 1 + (-i)i = 2. $

所以 $u$ 的正確長度是 $sqrt(2)$。若要歸一化（normalize），需先有 $u != 0$，再令

$ hat(u) = u / norm(u), quad hat(u)^dagger hat(u) = 1. $

兩個向量正交的條件是 $u^dagger v = 0$，不要求它們已歸一化。
例如 $u = vec(1, i)$ 與 $v = vec(i, 1)$ 滿足
$u^dagger v = i - i = 0$，且長度都是 $sqrt(2)$；
分別除以 $sqrt(2)$ 後，才得到一組 orthonormal vectors。

=== 與量子計算符號的對照

在選定 orthonormal basis 後，Dirac notation 中的 ket $lr(| psi chevron.r)$ 對應 column vector $psi$，
bra $lr(chevron.l psi |)$ 對應 row vector $psi^dagger$。因此

$ lr(chevron.l phi | psi chevron.r) = phi^dagger psi. $

同一對向量的乘法順序不同，結果的種類也不同：
$phi^dagger psi$ 是 scalar，而 $psi phi^dagger$ 是矩陣（outer product）。
若 $psi, phi in CC^n$，兩者的維度分別是 $1 times 1$ 與 $n times n$。

例如 $psi = vec(alpha, beta)$ 對應的 bra 是
$psi^dagger = mat(alpha^*, beta^*)$，
而量子純態向量的歸一化條件寫成

$ lr(chevron.l psi | psi chevron.r) = abs(alpha)^2 + abs(beta)^2 = 1. $

這裡的係數可以是複數，但長度平方仍是實數；關鍵正是內積中的共軛。
