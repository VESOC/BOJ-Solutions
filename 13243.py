# 백준 13243 Non-decreasing Subsegment
import sys
def input():
	return sys.stdin.readline().rstrip()
input()
data = list(map(int, input().split()))
count, tmp_count = 0, 1
cur_max = tmp = data[0]
for i in range(1, len(data)):
	if data[i] < data[i-1]:
		if tmp_count > count:
			count = tmp_count
			cur_max = tmp
		tmp = 0
		tmp_count = 0
	tmp_count += 1
	tmp += data[i]
if tmp_count > count:
	count = tmp_count
	cur_max = tmp
print(count, cur_max)