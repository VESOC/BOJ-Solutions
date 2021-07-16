# 백준 2675 문자열 반복 문제
for _ in range(int(input())):
	n, s = input().split()
	n = int(n)
	print(''.join([c*n for c in s]))
#----#
for _ in range(int(input())):
	n, s = input().split()
	n = int(n)
	for c in s:
		print(c*n, end='')
	print()