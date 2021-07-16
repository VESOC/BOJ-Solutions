# 백준 13458 시험 감독 문제
from math import ceil
input()
cnt = 0
classes = list(map(int, input().split()))
primary, secondary = map(int, input().split())
for students in classes:
	cnt += 1
	students -= primary
	if students <= 0:
		continue
	cnt += ceil(students/secondary)
print(cnt)