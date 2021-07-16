# 백준 4673 셀프넘버 문제
numbers = {i for i in range(1, 10001)}
generated = set()
for i in range(1, 10001):
	i += sum(map(int, str(i)))
	if i > 10000:
		continue
	generated.add(i)
[print(i) for i in sorted(list(numbers-generated))]
