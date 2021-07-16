# 백준 11466 Alex Origami Squares 문제
h, w = map(int, input().split())
h, w = max(h, w), min(h, w)
print(max(min(w, h/3), min(w/2, h/2)))