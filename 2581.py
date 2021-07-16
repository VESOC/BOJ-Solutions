# 백준 2581번 소수 문제
def isPrime(n):
	if n <= 1:
		return False
	i = 2
	while i*i <= n:
		if n%i == 0:
			return False
		i += 1
	return True
sum, min = 0, 0
for n in range(int(input()), int(input())+1):
	if isPrime(n):
		if min == 0:
			min = n
		sum += n
if sum == 0:
	print(-1)
else:
	print(sum)
	print(min)

#Sieve of Eratosthenes/에라토스테네스의 체
sieve = [True]*10001
sieve[0], sieve[1] = [False]*2
i = 2
while i <= 10000:
	if sieve[i]:
		for t in range(i+i, 10001, i):
			if sieve[t]:
				sieve[t] = False
	i += 1
sum, min = 0, 0
for n in range(int(input()), int(input())+1):
	if sieve[n]:
		if min == 0:
			min = n
		sum += n
if sum == 0:
	print(-1)
else:
	print(sum)
	print(min)