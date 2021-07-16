# 백준 10871 X보다 작은 수 문제
n, x = map(int, input().split())
for data in map(int, input().split()):
	if data < x:
		print(data, end=' ')