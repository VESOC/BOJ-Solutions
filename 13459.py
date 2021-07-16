# 백준 13459 구슬 탈출 문제
from collections import deque
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
for i in range(n):
  if 'R' in board[i]:
    rx, ry = i, board[i].index('R')
  if 'B' in board[i]:
    bx, by = i, board[i].index('B')
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
ans = 0


def move(x, y, dx, dy):
	cnt = 0
	while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
		x += dx
		y += dy
		cnt += 1
	return x, y, cnt


def bfs():
    global rx, ry, bx, by, visited, ans
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while q:
			rx, ry, bx, by, cnt = q.popleft()
			if cnt > 10:
				break
			for i in range(4):
				n_rx, n_ry, cr = move(rx, ry, direct[i][0], direct[i][1])
				n_bx, n_by, cb = move(bx, by, direct[i][0], direct[i][1])
				if board[n_bx][n_by] == 'O':
					continue
				if board[n_rx][n_ry] == 'O':
					print(1)
					return
				if n_rx == n_bx and n_ry == n_by:
						if cr > cb:
							n_rx -= direct[i][0]
							n_ry -= direct[i][1]
						else:
							n_bx -= direct[i][0]
							n_by -= direct[i][1]
				if visited[n_rx][n_ry][n_bx][n_by]:
					continue
				visited[n_rx][n_ry][n_bx][n_by] = True
				q.append((n_rx, n_ry, n_bx, n_by, cnt+1))
	print(0)

bfs()
