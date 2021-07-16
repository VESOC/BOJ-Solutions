# 백준 14470 전자레인지 문제
a, b, c, d, e = list(int(input()) for _ in range(5))
if a < 0:
	print(-a*c + d + b*e)
else:
	print((b-a)*e)