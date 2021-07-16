# 백준 8958 OX퀴즈 문제
for _ in range(int(input())):
	quiz_answer = input()
	answer = 0
	increment = 1
	for ox in quiz_answer:
		if ox == 'X':
			increment = 1
		else:
			answer += increment
			increment += 1
	print(answer)