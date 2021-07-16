# 백준 11651번 좌표 정렬하기 2 문제
import sys
def input():
    return sys.stdin.readline()
def print(a, b):
    sys.stdout.write(f'{a} {b}\n')
[print(*i) for i in sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0]))]