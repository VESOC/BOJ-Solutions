# 백준 1436번 영화감독 숌 문제
n = int(input())
i = 665
while True:
	i += 1
	if '666' in str(i):
		n -= 1
	if not n:
		print(i)
		break