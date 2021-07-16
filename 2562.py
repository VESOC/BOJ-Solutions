# 백준 2562 최댓값 문제
m, i = 0, 0
for j in range(9):
	n = int(input())
	if n > m:
		m, i = n, j+1
print(m)
print(i)
#--------#
data = [int(input()) for _ in range(9)]
print(max(data))
print(data.index(max(data))+1)