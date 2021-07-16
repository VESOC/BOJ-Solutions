# 백준 2798번 블랙잭 문제
n, t = map(int, input().split())
data = tuple(map(int, input().split()))
def blackjack():
	ans = 0
	for i in data[:-2]:
		for j in data[1:-1]:
			if i == j:
				continue
			for k in data[2:]:
				if j == k or i == k or i+j+k > t:
					continue
				if i+j+k == t:
					return t
				else:
					ans = max(ans, i+j+k)
	return ans
print(blackjack())

#--#
from itertools import combinations
n, m = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
for order in combinations(data, 3):
  s = sum(order)
  if s == m:
    ans = s
    break
  elif ans < s < m:
    ans = s
print(ans)