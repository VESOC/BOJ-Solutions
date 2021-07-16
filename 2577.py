# 백준 2577 숫자의 개수 문제
from collections import Counter
data = input()+input()+input()
count = Counter(data)
for i in range(10):
	print(0 if str(i) not in count else count[str(i)])
#------#
data = input()+input()+input()
count = [0]*10
for i in data:
	count[int(i)] += 1
[print(i) for i in count]