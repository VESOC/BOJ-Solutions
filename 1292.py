arr = [0]
for i in range(1, 51):
    arr += [i] * i
a, b = map(int, input().split())
print(sum(arr[a : b + 1]))
