n = int(input())
in_place = [0]*n
cnt = 0


def in_way(x):
    for i in range(x):
        if in_place[x] == in_place[i] or abs(in_place[x] - in_place[i]) == x - i:
            return False
    return True


def dfs(x):
    global cnt

    if x == n:
        cnt += 1
    else:
        for i in range(n):
            in_place[x] = i
            if in_way(x):
                dfs(x+1)


dfs(0)
print(cnt)
