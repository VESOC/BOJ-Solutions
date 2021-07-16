# 백준 14502 연구소 문제
from copy import deepcopy
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus_pos = []
safe_area = 0
for r in range(n):
	for c in range(m):
		if lab[r][c] == 2:
			virus_pos.append((r, c))

def build_wall(start, cnt):
	global lab, safe_area
	if cnt == 3:
		test_lab = deepcopy(lab)
		for virus in virus_pos:
			spread_virus(virus[0], virus[1], test_lab)
		cnt = sum(row.count(0) for row in test_lab)
		safe_area = max(cnt, safe_area)
	else:
		for rc in range(start, n*m):
			x, y = rc//m, rc%m
			if lab[x][y] == 0:
				lab[x][y] = 1
				build_wall(rc, cnt+1)
				lab[x][y] = 0


def spread_virus(x, y, test_lab):
	if test_lab[x][y] == 2:
		dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
		for i in range(4):
			cx, cy = x + dx[i], y + dy[i]
			if 0 <= cx < n and 0 <= cy < m:
				if test_lab[cx][cy] == 0:
					test_lab[cx][cy] = 2
					spread_virus(cx, cy, test_lab)
					

build_wall(0, 0)
print(safe_area)