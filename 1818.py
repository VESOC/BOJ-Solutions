# 백준 1818 책정리 문제 - Longest Increasing Subsquence 알고리즘
input()
data = list(map(int, input().split()))
lis = [data[0]]
cnt = 0
def lower_bound(end, target):
	start, mid = 0, 0
	while end != start:
		mid = (start+end)//2
		if lis[mid] < target:
			start = mid + 1
		else:
			end = mid
	return end
for i in data[1:]:
	if lis[-1] < i:
		lis.append(i)
	else:
		lis[lower_bound(len(lis)-1, i)] = i
		cnt += 1
print(cnt)