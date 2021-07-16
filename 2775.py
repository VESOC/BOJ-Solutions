# 백준 2775 부녀회장이 될거야 문제
for _ in range(int(input())):
	k, n = int(input()), int(input())
	residents = [i for i in range(1, n+1)]
	for _ in range(k):
		for j in range(1, n):
			residents[j] += residents[j-1]
	print(residents[-1])

for _ in range(int(input())):
	k, n, tmp = int(input()), int(input()), 1
	for i in range(1, k+1):
		tmp += n*i
	print(tmp)