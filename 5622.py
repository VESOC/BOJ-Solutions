# 백준 5622 다이얼 문제
classify = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
ans = 0
for c in s:
	for idx, dial in enumerate(classify):
		if c in dial:
			ans += 3 + idx
			break
print(ans)