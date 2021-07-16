# 백준 11650번 좌표 정렬하기 문제
import sys
[print(*x) for x in sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))])]