# 백준 1157 단어 공부 문제
from collections import Counter
words = input().upper()
word_list = list(set(words))
word_count = [words.count(c) for c in word_list]
if(word_count.count(max(word_count)) > 1):
    print('?')
else:
    print(word_list[(word_count.index(max(word_count)))])
# ---- #
word = input().upper()
word_count = Counter(input())
if list(word_count.values()).count(max(word_count.values())) > 1:
    print('?')
else:
    for k, v in word_count.items():
        if v == max(word_count.values()):
            print(k)
            break
