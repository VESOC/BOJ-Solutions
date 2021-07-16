# 백준 1002번 터렛 문제
for _ in range(int(input())):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	d = (x1-x2)**2 + (y1-y2)**2
	rad_sum = (r1 + r2)**2
	rad_dif = (r1 - r2)**2
	if d == 0:
		if r1 == r2:
			print(-1)
		else:
			print(0)
	else:
		if d in [rad_sum, rad_dif]:
			print(1)
		elif rad_dif < d < rad_sum:
			print(2)
		else:
			print(0)