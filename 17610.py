# 백준 17610 양팔저울 문제
input()
weights = list(map(int, input().split()))

def get_outcome(weights):
	if len(weights) <= 1:
		return weights
	before = get_outcome(weights[:-1])
	added = [outcome + weights[-1] for outcome in before]
	subtracted = [abs(outcome - weights[-1]) for outcome in before]
	total = list(set(before + added + subtracted + [weights[-1]]))
	if 0 in total:
		total.remove(0)
	return total

print(sum(weights) - len(get_outcome(weights)))