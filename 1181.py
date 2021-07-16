# 백준 1181번 단어 정렬 문제
import sys
def input():
    return sys.stdin.readline().rstrip()
def print(val):
    sys.stdout.write(str(val)+'\n')
data = sorted({input() for _ in range(int(input()))}, key=lambda s: (len(s), s))
[print(i) for i in data]