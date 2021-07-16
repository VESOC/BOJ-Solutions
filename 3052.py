# 백준 3052 나머지 문제
data = [int(input())%42 for _ in range(10)]
diff = set(data)
print(len(diff))