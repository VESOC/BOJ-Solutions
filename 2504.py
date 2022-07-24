s = input()
ans = i = 0
st, valst = [], [0]
fail = False
vd = {")": 2, "]": 3}
mtd = {"(": ")", "[": "]"}
while i < len(s):
    if st:
        if s[i] in "([":
            if i + 1 >= len(s):
                fail = True
                break
            if s[i + 1] == mtd[s[i]]:
                valst[-1] += vd[mtd[s[i]]]
                i += 2
                continue
            st.append(mtd[s[i]])
            valst.append(0)
            i += 1
            continue
        else:
            valst[-1] *= vd[s[i]]
            if not st:
                fail = True
                break
            if st.pop() != s[i]:
                fail = True
                break
        i += 1
        print(not not valst, valst)
        if st and valst:
            tmp = valst.pop()
            valst[-1] += tmp
        if not st and valst:
            ans += valst.pop()
        continue
    if s[i] in "([":
        if i + 1 >= len(s):
            fail = True
            break
        if s[i + 1] == mtd[s[i]]:
            ans += vd[mtd[s[i]]]
            i += 2
        else:
            st.append(mtd[s[i]])
            valst.append(0)
            i += 1
    else:
        fail = True
        break
if fail:
    print(0)
else:
    print(ans)


# -------- #
bracket = input()
stack = []
answer = 0
tmp = 1
vald = {")": 2, "]": 3}
rev = {")": "[", "]": "("}
mtd = {"(": ")", "[": "]", ")": "(", "]": "["}
for i in range(len(bracket)):
    if bracket[i] in "([":
        stack.append(bracket[i])
        tmp *= vald[mtd[bracket[i]]]
    else:
        if not stack or stack[-1] == rev[bracket[i]]:
            answer = 0
            break
        if bracket[i - 1] == mtd[bracket[i]]:
            answer += tmp
        stack.pop()
        tmp //= vald[bracket[i]]
if stack:
    print(0)
else:
    print(answer)
