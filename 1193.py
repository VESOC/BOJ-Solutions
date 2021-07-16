# 백준 1193 분수 찾기 문제
n = int(input())
i = 1
while True:
	n -= i
	if n <= 0:
		n += i
		break
if i%2:
	print((n-i), '/', i, sep='')
else:
	print(i, '/', (n-i), sep='')