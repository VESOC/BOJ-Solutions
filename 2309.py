from bisect import bisect

arr = []
for _ in range(9):
    arr.append(int(input()))
su = sum(arr)
diff = su - 100
arr.sort()
for i in range(9):
    t = bisect(arr, diff - arr[i]) - 1
    if arr[t] == diff - arr[i]:
        a, b = arr[t], arr[i]
        arr.remove(a)
        arr.remove(b)
        print(*arr, sep="\n")
        break
