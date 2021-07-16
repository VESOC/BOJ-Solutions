# 백준 13985 Equality 문제
equation = input()
isValid = eval(equation[:6] + '=' + equation[6:])
print('YES' if isValid else 'NO')