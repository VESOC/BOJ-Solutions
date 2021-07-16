# 백준 5014번 스타트링크

f, s, g, u, d = map(int, input().split())
goal = g-s
cnt = 0
if goal > 0:
    if u == 0:
        print("use the stairs")
    else:
        cnt += goal // u
        goal %= u
        a = u - d
        if goal % a == 0:
            cnt += 2 * (goal // a)
            print(cnt)
        else:
            print("use the stairs")
elif goal < 0:
    if d == 0:
        print("use the stairs")
    else:
        cnt += -goal // -d
        goal -= cnt * d
        a = d - u
        if -goal % -a == 0:
            cnt += 2 * (-goal // -a)
            print(cnt)
        else:
            print("use the stairs")
else:
    print(0)
