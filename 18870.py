n = int(input())
org = tuple(map(int, input().split()))
ans = {k: i for i, k in enumerate(sorted(set(org)))}
[print(ans[k], end=' ') for k in org]
