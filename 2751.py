# 백준 2751번 수 정렬하기 2 문제

# 파이썬 내장 함수
import sys
[sys.stdout.write(str(v)+'\n') for v in sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])]

# 병합 정렬
import sys
def input():
	return int(sys.stdin.readline())
def print(v):
	sys.stdout.write(str(v)+'\n')
def mergeSort(x):
	if len(x) > 1:
		mid = len(x)//2
		lx, rx = x[:mid], x[mid:]
		mergeSort(lx)
		mergeSort(rx)
		li, ri, i = 0, 0, 0
		while li < len(lx) and ri < len(rx):
			if lx[li] < rx[ri]:
				x[i] = lx[li]
				li += 1
			else:
				x[i] = rx[ri]
				ri += 1
			i += 1
		x[i:] = lx[li:] if li != len(lx) else rx[ri:]
data = [input() for _ in range(input())]
mergeSort(data)
[print(v) for v in data]

# 힙 정렬
import heapq
import sys
def input():
	return int(sys.stdin.readline())
def print(v):
	sys.stdout.write(str(v)+'\n')
data = [input() for _ in range(input())]
heapq.heapify(data)
[print(heapq.heappop(data)) for _ in range(len(data))]