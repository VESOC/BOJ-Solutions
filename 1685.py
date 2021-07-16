# 백준 1685 숫자놀이 문제 - 실패
input()
data = list(reversed(sorted(map(int, input().split()))))
n = int(input())
for i in range(2, data[0]*n):
	t, m = n, i
	for j in data:
		if j > m:
			continue
		while t > 0 and m > 0:
			m -= j
			t -= 1
		t += 1
		i += j
	if i < 0:
		if i%2:
			print(f'jjaksoon win at {i}')
			break
		else:
			print(f'holsoon win at {i}')
			break