import heapq

def generate_a005243(n_terms: int):
    """
    Generate the first n_terms of A005243:
    a1=1, a2=2, and for k>=3, a_k is the least integer > a_{k-1}
    representable as a sum of at least two consecutive earlier terms.
    Implementation: maintain a min-heap of representable sums.
    """
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [1]
    if n_terms == 2:
        return [1, 2]

    a = [1, 2]

    # Heap of candidate representable sums (as integers).
    # We will allow duplicates in heap; we'll skip used values and <= last.
    heap = []

    # Initialize with sums of >=2 consecutive terms from [1,2] -> only 1+2=3
    heapq.heappush(heap, 1 + 2)

    last = a[-1]

    while len(a) < n_terms:
        # Pop until we find the smallest candidate strictly greater than last
        x = heapq.heappop(heap)
        while x <= last:
            x = heapq.heappop(heap)

        # x becomes the next term
        a.append(x)
        last = x

        # Update heap with all sums of >=2 consecutive terms that END at new term.
        # That is: a[j] + a[j+1] + ... + a[new_index] for j <= new_index-1.
        # We build these by summing backwards, ensuring length >= 2.
        s = 0
        # iterate backwards over previous terms INCLUDING new term
        # We'll accumulate s = a[i] + ... + a[new]
        for i in range(len(a) - 1, -1, -1):
            s += a[i]
            # Need at least 2 terms: i must be <= new_index-1
            if i <= len(a) - 2:
                heapq.heappush(heap, s)

    return a

def main():
    n_terms = 30000
    out_path = "A005243_first30000.txt"

    a = generate_a005243(n_terms)

    with open(out_path, "w", encoding="utf-8") as f:
        for idx, val in enumerate(a, start=1):
            f.write(f"{idx}\t{val}\n")

    print(f"Wrote {n_terms} terms to {out_path}")

if __name__ == "__main__":
    main()
