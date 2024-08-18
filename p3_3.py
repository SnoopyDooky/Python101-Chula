l = int(input())  # perimeter
max_c = -1
# a+b+c = l and 0 < a < b < c < l
# Thus: b < c => b < l-a-b => b < l-a
for a in range(1, l-1):  # 1 <= a <= l-2
    for b in range(a+1, l-a):  # a < b < l-a
        c = l - a - b
        if c**2 == a**2 + b**2 and c > max_c:
            max_c = c
print(max_c)
