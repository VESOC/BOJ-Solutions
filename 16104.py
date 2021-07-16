# 백준 16104 Extending Rock-Paper-Scissors 문제
n = int(input())
for i in range(n):
	for j in range(1, (n-1)//2+1):
		print(i+1, (i+j)%n)