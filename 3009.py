# 백준 3009번 네 번째 점 문제
x, y = [], []
for _ in range(3):
	n, m = map(int, input().split())
	x.append(n)
	y.append(m)
for i in x:
	if x.count(i) == 1:
		print(i, end=' ')
		break
for i in y:
	if y.count(i) == 1:
		print(i)
		break