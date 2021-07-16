# 백준 17611 직각다각형 문제
points = [list(map(int, input().split())) for _ in range(int(input()))]
points.append(points[0])
x_cnt, y_cnt = dict(), dict()
for p in range(1, len(points)):
	pre_x, pre_y = points[p-1]
	x, y = points[p]

	if x == pre_x:
		start = min(y, pre_y)
		end = max(y, pre_y)
		if start in y_cnt.keys():
				y_cnt[start] += 1
		else:
				y_cnt[start] = 1
		if end in y_cnt.keys():
				y_cnt[end] -= 1
		else:
				y_cnt[end] = -1

	if y == pre_y:
		start = min(x, pre_x)
		end = max(x, pre_x)
		if start in x_cnt.keys():
				x_cnt[start] += 1
		else:
				x_cnt[start] = 1
		if end in x_cnt.keys():
				x_cnt[end] -= 1
		else:
				x_cnt[end] = -1

x_cnt = sorted(x_cnt.items(), key=(lambda x:x[0]))
y_cnt = sorted(y_cnt.items(), key=(lambda x:x[0]))

max_x = 0
temp_x = 0
for v in x_cnt.values():
    temp_x += v
    max_x = max(max_x, temp_x)

max_y = 0
temp_y = 0
for v in y_cnt.values():
    temp_y += v
    max_y = max(max_y, temp_y)

print(max(max_x, max_y))