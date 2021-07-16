# 백준 2750번 수 정렬하기 문제

# 버블 정렬
data = [int(input()) for _ in range(int(input()))]
for i in range(len(data)):
	for j in range(len(data)-i-1):
		if data[j] > data[j+1]:
			data[j], data[j+1] = data[j+1], data[j]
[print(v) for v in data]
# 선택 정렬
data = [int(input()) for _ in range(int(input()))]
for i in range(len(data)-1):
	min_index = i
	for j in range(i+1, len(data)):
		if data[j] < data[min_index]:
			min_index = j
	data[i], data[min_index] = data[min_index], data[i]
[print(v) for v in data]
# 삽입 정렬
data = [int(input()) for _ in range(int(input()))]
for end in range(1, len(data)):
	i = end
	while i > 0 and data[i - 1] > data[i]:
		data[i - 1], data[i] = data[i], data[i - 1]
		i -= 1
[print(v) for v in data]
# 내장 함수
[print(v) for v in sorted([int(input()) for _ in range(int(input()))])]