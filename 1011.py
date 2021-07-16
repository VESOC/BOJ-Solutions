# 백준 1011번 Fly me to Alpha Centauri 문제
from math import sqrt
for _ in range(int(input())):
	x, y = map(int, input().split())
	dif = y-x
	if dif <= 3:
		print(dif)
	else:
		t = int(sqrt(dif))
		if dif == t**2:
			print(2*t-1)
		elif t**2 < dif <= t**2 + t:
			print(2*t)
		elif t**2 + t < dif <= t**2 + 2*t:
			print(2*t+1)