# 백준 4948번 베르트랑 공준 문제
sieve = [1]*246913
sieve[0] = 0
sieve[1] = 0
for i in range(2, 246913):
	if sieve[i]:
		for j in range(i+i, 246913, i):
			sieve[j] = 0
while True:
	n = int(input())
	if n == 0:
		break
	print(sum(sieve[n+1:n*2+1]))