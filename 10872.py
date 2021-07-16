# 백준 10872번 팩토리얼 문제
def factorial(n):
	if n < 2:
		return 1
	return n * factorial(n-1)
print(factorial(int(input())))