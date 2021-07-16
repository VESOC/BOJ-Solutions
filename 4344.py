# 백준 4344 평균은 넘겠지 문제
for _ in range(int(input())):
	n, *data = list(map(int, input().split()))
	avg = sum(data)/n
	cnt = 0
	for score in data:
		if score > avg:
			cnt += 1
	print('%.3f%%' %(cnt/n*100))