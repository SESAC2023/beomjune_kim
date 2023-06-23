h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
else:
    if h >= 1:
        print(h-1, 15 + m)
    elif h < 1:
        print(23, 15 + m)
