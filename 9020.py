# 백준 9020번 골드바흐의 추측 문제
sieve = list(range(2, 10001))
for i in range(2, 10001):
  if sieve[i]:
    for t in range(i+i, 10001, i):
      if sieve[t]:
        sieve[t] = 0
sieve = [i for i in sieve if i]
for _ in range(int(input())):
	tmin, tmax = -1e9, 1e9
	n = int(input())
	for i in range(2, n//2+1):
		if i in sieve:
			if n-i in sieve:
				if tmax-tmin > n-i - i:
					tmax, tmin = n-i, i
	print(tmin, tmax)