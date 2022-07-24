from itertools import combinations

n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {"a", "n", "t", "i", "c"}
    input_chars = []
    alpha = {
        k: v
        for v, k in enumerate(
            (set(map(chr, range(ord("a"), ord("z") + 1))) - nece_chars)
        )
    }
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input()) - nece_chars:
            tmp |= 1 << alpha[c]
        input_chars.append(tmp)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb)

        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)

# -------- #
from itertools import combinations
from sys import exit

n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    learned = {"a", "n", "t", "i", "c"}
    words = []
    all_char = set()
    ans = 0
    for _ in range(n):
        words.append(set(input()) - learned)
        all_char |= words[-1]
    if len(all_char) < k - 5:
        print(n)
        exit(0)
    for comb in combinations(all_char, k - 5):
        comb = set(comb)
        tmp = 0
        for word in words:
            if word | comb == comb:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
