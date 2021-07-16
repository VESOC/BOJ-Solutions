# 백준 2941 크로아티아 알파벳 문제
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for c_alphabet in croatian_alphabets:
    word = word.replace(c_alphabet, ' ')
print(len(word))