# A note on the self-generating consecutive-sum greedy sequence (OEIS A005243)

This repository contains a short note on the greedy self-generating sequence
defined by
- $a_1=1$, $a_2=2$;
- for $k\ge 3$, $a_k$ is the least integer $>a_{k-1}$ that can be written as a sum
  of at least two consecutive earlier terms.

This is OEIS **A005243** (https://oeis.org/A005243) and also appears as Problem #423 (https://www.erdosproblems.com/423) in Bloom’s Erdős Problems website.

## Main result

Define the “excess” $b_n := a_n - n$. The note proves:

> **Theorem.** The sequence $(b_n)_{n\ge 1}$ is nondecreasing and unbounded.
> In particular, {a_n: n >= 1} omits infinitely many positive integers,
> settling a conjecture recorded in the COMMENTS section of OEIS A005243
> (“Conjecture: there are infinitely many nonmembers.”).

## Files

- `On_Erdős_Problem_423.pdf`.
- LaTeX source.

