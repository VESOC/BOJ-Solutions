# 백준 10809 알파벳 찾기 문제
print(*map(input().find, map(chr,range(97, 123))))
#----#
word = input()
for i in range(97, 123):
	i = chr(i)
	print(word.find(i))
#----#
word = input()
alphabet = dict()
for c in map(chr, range(97, 123)):
	alphabet[c] = -1
for i, c in enumerate(word):
	if alphabet[c] == -1:
		alphabet[c] = i
print(*alphabet.values())