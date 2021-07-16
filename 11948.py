# 백준 11948 과목 선택 문제
science = [int(input()) for _ in range(4)]
humanities = [int(input()) for _ in range(2)]
science.remove(min(science))
print(sum(science) + max(humanities))