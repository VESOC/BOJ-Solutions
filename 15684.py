# 백준 15684 사다리 조작 문제
m, h, n = map(int, input().split())
ladder = [[0]*(m+2) for _ in range(n)]
ans = 4
for _ in range(h):
	h, v = map(int, input().split())
	ladder[h-1][v] = 1

def set_horizontal_ladder(start, cnt):
	global ans
	if check():
		ans = min(ans, cnt)
		return
	elif cnt == 3 or ans <= cnt:
		return
	for i in range(start, m+1):
		for j in range(n):
			if ladder[j][i] + ladder[j][i-1] + ladder[j][i+1] == 0:
				ladder[j][i] = 1
				set_horizontal_ladder(i, cnt+1)
				ladder[j][i] = 0

def check():
	for i in range(1, m+1):
		cur = i
		for j in range(n):
			if ladder[j][cur-1] == 1:
				cur -= 1
			elif ladder[j][cur] == 1:
				cur += 1
		if cur != i:
			return False
	return True

set_horizontal_ladder(1, 0)
print(ans if ans < 4 else -1)