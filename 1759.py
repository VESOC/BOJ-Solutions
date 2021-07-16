# 백준 1759번 암호 만들기
from itertools import combinations

l, c = map(int, input().split())
letters = list(set(input())-set(' '))
words = set(combinations(letters, l))
remove_words = set()
for word in words:
    vowel_cnt = consonant_cnt = 0
    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            vowel_cnt += 1
        else:
            consonant_cnt += 1
    if not (vowel_cnt >= 1 and consonant_cnt >= 2):
        remove_words.add(word)
possibles = list(words - remove_words)
for i in range(len(possibles)):
    possibles[i] = ''.join(sorted(possibles[i]))
[print(word) for word in sorted(possibles)]
