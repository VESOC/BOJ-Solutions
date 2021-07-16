from math import ceil, log2
import sys

input = sys.stdin.readline


def get_min(left, right):
    global size, tree
    res_min = []
    res_max = []
    left += size
    right += size
    while left < right:
        if left % 2:
            res_min += [tree[left][0]]
            res_max += [tree[left][1]]
            left += 1
        if not right % 2:
            res_min += [tree[right][0]]
            res_max += [tree[right][1]]
            right -= 1
        left //= 2
        right //= 2
    if left == right:
        res_min += [tree[left][0]]
        res_max += [tree[left][1]]
    return [min(res_min), max(res_max)]


n, m = map(int, input().split())
numbers = [[int(input())]*2 for _ in range(n)]
size = (1 << ceil(log2(n)))
tree = [[1000000000, 1000000000] for _ in range(size << 1)]
tree[size:size+n] = numbers
for i in range(size-1, 0, -1):
    t = i << 1
    a, b = tree[t], tree[t+1]
    tree[i] = [min(a[0], b[0]), max(a[1], b[1])]
for _ in range(m):
    a, b = map(int, input().split())
    print(*get_min(a-1, b-1))
