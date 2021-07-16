# 백준 1929번 소수 구하기 문제
def isPrime(n):
	if n <= 1:
		return False
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True
m, n = map(int, input().split())
for i in range(m, n+1):
	if isPrime(i):
		print(i)

#Sieve of Eratosthenes/에라토스테네스의 체
sieve = [True]*1000001
sieve[0], sieve[1] = [False]*2
i = 2
while i <= 1000000:
  if sieve[i]:
    for t in range(i+i, 1000001, i):
      if sieve[t]:
        sieve[t] = False
  i += 1
m, n = map(int, input().split())
for i in range(m, n+1):
	if sieve[i]:
		print(i)
