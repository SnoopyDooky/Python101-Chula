n = int(input())
s = set([int(e) for e in input().split()])
s_union = set(s)
s_intersect = set(s)
for _ in range(n-1):
    t = set([int(e) for e in input().split()])
    s_union = s_union | t
    s_intersect = s_intersect & t
print(len(s_union))
print(len(s_intersect))
