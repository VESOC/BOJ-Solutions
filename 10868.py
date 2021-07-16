from math import ceil, log2
import sys

input = sys.stdin.readline


def get_min(left, right):
    global size, tree
    results = []
    left += size
    right += size
    while left < right:
        if left % 2:
            results += [tree[left]]
            left += 1
        if not right % 2:
            results += [tree[right]]
            right -= 1
        left //= 2
        right //= 2
    if left == right:
        results += [tree[left]]
    return min(results)


n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
size = (1 << ceil(log2(n)))
tree = [1000000000]*(size << 1)
tree[size:size+n] = numbers
for i in range(size-1, 0, -1):
    t = i << 1
    a, b = tree[t], tree[t+1]
    tree[i] = min(a, b)
for _ in range(m):
    a, b = map(int, input().split())
    print(get_min(a-1, b-1))

# ---- #

input = sys.stdin.readline


def init(node, start, end):
    global tree
    if start == end:
        tree[node] = numbers[start]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2),
                         init(node*2+1, (start+end)//2+1, end))
    return tree[node]


def get_min(node, start, end, left, right):
    if left > end or right < start:
        return 1000000000
    if left <= start and end <= right:
        return tree[node]
    return min(get_min(node*2, start, (start+end)//2, left, right),
               get_min(node*2+1, (start+end)//2+1, end, left, right))


n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
size = (1 << ceil(log2(n))+1)
tree = [1000000000]*size
init(1, 0, n-1)
for _ in range(m):
    a, b = map(int, input().split())
    print(get_min(1, 0, n-1, a-1, b-1))
