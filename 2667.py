# 백준 2667 단지번호붙이기 문제
def dfs(x, y):
	global graph, ans
	if 0 > x or x > n-1 or 0 > y or y > n-1:
		return False
	if graph[x][y] == 1:
		graph[x][y] = 0
		ans[cnt] += 1
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		return True
	return False


ans = [[0]*25]
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt = 0
for i in range(n):
	for j in range(n):
		if dfs(i, j):
			cnt += 1
print(cnt)
[print(i) for i in sorted(ans[:cnt])]