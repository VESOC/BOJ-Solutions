# PyPy3
from fractions import Fraction

N, K = map(int, input().split())
A = list(map(int, input().split()))

cards = [[] for _ in range(4)]
for _ in range(N):
    t, r = input().split()
    cards[ord(t[0]) - 65].append(int(r))

for a in cards:
    a.sort(reverse=True)

ratios = []
for i, c in enumerate(cards):
    s = A[i]
    for x in c:
        ratios.append((Fraction(x, s), (chr(i + 65), x)))
        s += x

ratios.sort(reverse=True)
[print(*row[1]) for row in ratios[:K]]
