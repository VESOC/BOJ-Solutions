# 백준 10870번 피보나치 수 5 문제
def fibo(n):
	if n < 2:
		return n
	else:
		return fibo(n-1) + fibo(n-2)
print(fibo(int(input())))

# 다이나믹 프로그래밍/동적계획법
dp = [0, 1]
def dp_fibo(n):
	if n < len(dp):
		return dp[n]
	else:
		tmp = dp_fibo(n-1) + dp_fibo(n-2)
		dp.append(tmp)
		return tmp
print(dp_fibo(int(input())))

# 메모리 절약
cur, next = 0, 1
for _ in range(int(input())):
	cur, next = next, next + cur
print(cur)

# 일반항
from math import sqrt
def fibo(n): 
    phi = (1 + sqrt(5)) / 2
    return round(pow(phi, n) / sqrt(5)) 
print(fibo(int(input())))