for _ in range(int(input())):
    n = int(input())
    pos = 0
    while n > 1:
        if n % 2:
            print(pos, end=" ")
        pos += 1
        n //= 2
    print(pos)
