# 백준 10250 ACM 호텔 문제
for _ in range(int(input())):
	h, w, n = map(int, input().split())
	a = n%h
	b = n//h+1
	if a == 0: 
		a = h
		b -= 1
	print(a*100+b)