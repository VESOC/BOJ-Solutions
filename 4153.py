# 백준 4153번 직각삼각형 문제
while True:
	data = list(map(int, input().split()))
	if data[0] == 0:
		break
	a = max(data)
	data.remove(a)
	if a**2 == data[0]**2 + data[1]**2:
		print('right')
	else:
		print('wrong')