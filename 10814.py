# 백준 10814번 나이순 정렬 문제
data = []
for _ in range(int(input())):
    x, y = input().split()
    data.append((int(x), y))
data.sort(key=lambda x: x[0])
[print(*i) for i in data]