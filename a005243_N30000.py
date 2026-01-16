import math
import heapq
import argparse
import matplotlib.pyplot as plt


def a005243_first_n(n_max: int):
    """
    Generate first n_max terms of OEIS A005243:
      a1=1, a2=2; for k>=3 pick the least integer > a_{k-1}
      representable as a sum of >=2 consecutive earlier terms.
    """
    if n_max <= 0:
        return []
    if n_max == 1:
        return [1]

    terms = [1]
    heap = [2]      # min-heap of representables; ensures a2 = 2
    seen = {2}      # dedup
    cum = [1]       # cumulative sums of reversed terms (initially [1])

    while len(terms) < n_max:
        m = heapq.heappop(heap)
        seen.remove(m)
        terms.append(m)

        # new representables: m + cum
        for s in cum:
            val = m + s
            if val not in seen:
                seen.add(val)
                heapq.heappush(heap, val)

        # update cum
        cum = [m] + [m + s for s in cum]

    return terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=30000, help="number of terms to generate")
    args = parser.parse_args()
    n_max = args.n

    a = a005243_first_n(n_max)
    b = [a[i] - (i + 1) for i in range(n_max)]

    xs = list(range(1, n_max + 1))

    b_over_n15 = [b[i] / (xs[i] ** (1.0 / 5.0)) for i in range(n_max)]
    b_over_n13 = [b[i] / (xs[i] ** (1.0 / 3.0)) for i in range(n_max)]
    b_over_sqrt = [b[i] / math.sqrt(xs[i]) for i in range(n_max)]
    b_over_log = [float("nan")] * n_max
    for i, n in enumerate(xs):
        if n >= 2:
            b_over_log[i] = b[i] / math.log(n)

    # 5 plots: b_n, b_n/n^{1/5}, b_n/n^{1/3}, b_n/n^{1/2}, b_n/log n
    fig, axes = plt.subplots(5, 1, figsize=(9, 18))

    # 1) b_n (log-log)
    axes[0].loglog(xs, [max(1e-12, v) for v in b])
    axes[0].set_xlabel("n")
    axes[0].set_ylabel("b_n = a_n - n")
    axes[0].set_title(f"A005243: b_n (first {n_max} terms)")
    axes[0].grid(True, which="both")

    # 2) b_n / n^{1/5}
    axes[1].plot(xs, b_over_n15)
    axes[1].set_xlabel("n")
    axes[1].set_ylabel(r"$b_n / n^{1/5}$")
    axes[1].set_title(r"$b_n / n^{1/5}$")
    axes[1].grid(True)

    # 3) b_n / n^{1/3}
    axes[2].plot(xs, b_over_n13)
    axes[2].set_xlabel("n")
    axes[2].set_ylabel(r"$b_n / n^{1/3}$")
    axes[2].set_title(r"$b_n / n^{1/3}$")
    axes[2].grid(True)

    # 4) b_n / n^{1/2}
    axes[3].plot(xs, b_over_sqrt)
    axes[3].set_xlabel("n")
    axes[3].set_ylabel(r"$b_n / n^{1/2}$")
    axes[3].set_title(r"$b_n / n^{1/2}$")
    axes[3].grid(True)

    # 5) b_n / log n  (start from n=2)
    axes[4].plot(xs[1:], b_over_log[1:])
    axes[4].set_xlabel("n")
    axes[4].set_ylabel(r"$b_n / \log n$")
    axes[4].set_title(r"$b_n / \log n$")
    axes[4].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
