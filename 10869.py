# 백준 10869 사칙연산 문제
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
#------#
numbers = input().split()
for operator in ['+', '-', '*', '//', '%']:
	print(eval(operator.join(numbers)))