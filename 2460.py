peo = [0] * 11
for i in range(1, 11):
    off, on = map(int, input().split())
    if i == 1:
        peo[1] = on
    else:
        peo[i] = peo[i - 1] - off + on
print(max(peo))
