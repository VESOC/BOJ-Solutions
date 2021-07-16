# 백준 13866 팀 나누기 문제
levels = list(map(int, input().split()))
print(abs(sum(levels)-2*(max(levels)+min(levels))))