st = []

for _ in range(int(input())):
    c = int(input())
    if c == 0 and len(st):
        st.pop()
    elif c != 0:
        st.append(c)
print(sum(st))
