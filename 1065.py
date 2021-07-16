# 백준 1065 한수 문제
n = int(input())
if n < 100:
	print(n)
else:
	cnt = 99
	for i in range(100, n+1):
		d = tuple(map(int, str(i)))
		if d[0]-d[1] == d[1]-d[2]:
			cnt += 1
	print(cnt)