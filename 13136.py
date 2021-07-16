# 백준 13136 Do Not Touch Anything 문제
from math import ceil
r, c, n = map(int, input().split())
print(ceil(r/n)*ceil(c/n))