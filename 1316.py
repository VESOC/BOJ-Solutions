# 백준 1316 그룹 단어 체커 문제
ans = 0
for _ in range(int(input())):
	word = input()
	new_word = ''
	isTrue = True
	for c in word:
		i, j = word.find(c), word.rfind(c)
		if word.count(c) != j-i+1:
			isTrue = False
			break
	ans += isTrue
print(ans)
#----#
cnt = 0
for _ in range(int(input())):
    word = input()
    cnt += list(word) == sorted(word, key = word.find)
print(cnt)