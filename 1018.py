# 백준 1018번 체스판 다시 칠하기 문제
n, m = map(int, input().split())
data = [input() for _ in range(n)]
ans = 65
for x in range(n-7):
	for y in range(m-7):
		b = 0 # 검은색으로 시작
		w = 0 # 흰색으로 시작
		# 의미상 인덱스의 합이 짝수일때를 시작으로 봄
		for s in range(x, x+8):
			for e in range(y, y+8):
				if (s+e)%2: # 홀수
					if data[s][e] != 'B': # 흰색 시작이면 홀수일때 검은색이어야 하는데 아니므로 w추가
						w += 1
					else: # 검은색 시작이면 홀수일때 흰색이어야 하는데 아니므로 b추가
						b += 1
				else: # 짝수
					if data[s][e] != 'W': # 흰색 시작 - 흰 색이 아니므로 w추가
						w += 1
					else: # 검은색 시작 - 검은 색이 아니므로 b추가
						b += 1
		ans = min(ans, b, w)
print(ans)