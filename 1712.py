# 백준 1712 손익분기점 문제
a, b, c = map(int, input().split())
if c <= b:
	print(-1)
else:
	print(a//(c-b)+1)