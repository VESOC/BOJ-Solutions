# 백준 2231번 분해합 문제
def func():
	n = int(input())
	m = max(n - 9*len(str(n)),0)
	for i in range(m, n):
		if n == sum(map(int, str(i)))+i:
			return i
	return 0
print(func())