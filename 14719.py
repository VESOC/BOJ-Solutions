h, w = map(int, input().split())
arr = [[0] * w for _ in range(h)]
for i, b in enumerate(map(int, input().split())):
    for k in range(h - 1, h - b - 1, -1):
        arr[k][i] = 1
ans = 0
for i in range(h):
    begin = False
    bi = ei = 0
    for j in range(w):
        if arr[i][j] == 1:
            if not begin:
                begin = True
                bi = j + 1
                continue
            elif begin:
                ans += j - bi
                bi = j + 1
print(ans)

# -------- #
h, w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, w - 1):
    left, right = max(arr[:i]), max(arr[i + 1 :])
    cmp = min(left, right)
    if arr[i] < cmp:
        ans += cmp - arr[i]
print(ans)
