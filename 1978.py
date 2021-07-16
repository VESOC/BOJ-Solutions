# 백준 1978번 소수 찾기 문제
def isPrime(n):
	if n <= 1:
		return False
	i = 2
	while i*i <= n:
		if n%i == 0:
			return False
		i += 1
	return True
input()
ans = 0
for n in map(int, input().split()):
	if isPrime(n):
		ans += 1
print(ans)

#Sieve of Erathosthenes/에라토스테네스의 체
sieve = [True]*1001
sieve[0], sieve[1] = [False]*2
i = 2
while i <= 1000:
	if sieve[i]:
		for t in range(i+i, 1001, i):
			if sieve[t]:
				sieve[t] = False
	i += 1
input()
ans = 0
for n in map(int, input().split()):
	if sieve[n]:
		ans += 1
print(ans)