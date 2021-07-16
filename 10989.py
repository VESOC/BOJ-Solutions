# 백준 10989번 수 정렬하기 3 문제
import sys
def input():
	return int(sys.stdin.readline())
def print(v):
	sys.stdout.write(str(v)+'\n')
data = [0]*10001
for _ in range(input()):
	data[input()] += 1
for i in range(1, 10001):
	if data[i]:
		for _ in range(data[i]):
			print(i)