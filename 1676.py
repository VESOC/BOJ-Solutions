def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)


f = str(fac(int(input())))[::-1]
for i in range(len(f)):
    if f[i] != '0':
        print(i)
        break
