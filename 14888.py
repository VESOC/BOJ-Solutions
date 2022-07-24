n = int(input())
num = list(map(int, input().split()))
ops = list(map(int, input().split()))
ma, mi = -1000000001, 1000000001


def backtrack(val, opct, p, m, t, d):
    global ma, mi
    if opct == n - 1:
        ma = max(ma, val)
        mi = min(mi, val)
        return
    if p:
        backtrack(val + num[opct + 1], opct + 1, p - 1, m, t, d)
    if m:
        backtrack(val - num[opct + 1], opct + 1, p, m - 1, t, d)
    if t:
        backtrack(val * num[opct + 1], opct + 1, p, m, t - 1, d)
    if d:
        if val < 0:
            backtrack(-(-val // num[opct + 1]), opct + 1, p, m, t, d - 1)
        else:
            backtrack(val // num[opct + 1], opct + 1, p, m, t, d - 1)


backtrack(num[0], 0, *ops)
print(ma)
print(mi)
