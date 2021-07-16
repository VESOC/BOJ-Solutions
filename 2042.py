from math import ceil, log2
import sys

# input = sys.stdin.readline


# def init(node, start, end):
#     global tree
#     if start == end:
#         tree[node] = numbers[start]
#     else:
#         tree[node] = init(node*2, start, (start+end)//2) + \
#             init(node*2+1, (start+end)//2+1, end)
#     return tree[node]


# def update(node, start, end, index, diff):
#     global tree
#     if index < start or index > end:
#         return
#     tree[node] += diff
#     if start != end:
#         update(node*2, start, (start+end)//2, index, diff)
#         update(node*2+1, (start+end)//2+1, end, index, diff)


# def sum(node, start, end, left, right):
#     if left > end or right < start:
#         return 0
#     if left <= start and end <= right:
#         return tree[node]
#     return sum(node*2, start, (start+end)//2, left, right) + sum(node*2+1, (start+end)//2+1, end, left, right)


# n, m, k = map(int, input().split())
# numbers = [int(input()) for _ in range(n)]
# size = (1 << ceil(log2(n))+1)
# tree = [0]*size
# init(1, 0, n-1)
# for _ in range(m+k):
#     mode, b, c = map(int, input().split())
#     if mode == 1:
#         diff = c - numbers[b-1]
#         numbers[b-1] = c
#         update(1, 0, n-1, b-1, diff)
#     else:
#         print(sum(1, 0, n-1, b-1, c-1))

# ---- # Fenwick Tree Method
input = sys.stdin.readline


def sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= i & -i
    return ans


def update(i, diff):
    global tree
    while i < n+1:
        tree[i] += diff
        i += i & -i


n, m, k = map(int, input().split())
tree = [0]*(n+1)
numbers = [0]*(n+1)
for i in range(1, n+1):
    numbers[i] = int(input())
    update(i, numbers[i])
for _ in range(m+k):
    mode, b, c = map(int, input().split())
    if mode == 1:
        diff = c - numbers[b]
        numbers[b] = c
        update(b, diff)
    else:
        print(sum(c) - sum(b-1))
