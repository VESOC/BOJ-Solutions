# 백준 7568번 덩치 문제 
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
	cnt = 1
	for j in range(n):
		if i == j:
			continue
		if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
			cnt += 1
	print(cnt, end=' ')