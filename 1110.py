# 백준 1110 더하기 싸이클 문제
n = k = int(input())
count = 0
while True:
	k = (k%10) * 10 + (k//10 + k%10) % 10
	count += 1
	if k == n:
		print(count)
		break