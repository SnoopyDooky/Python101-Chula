d = []
t = int(input())
while t >= 0:   # append t >= 0
    d.append(t)
    t = int(input())
d.append(t)   # append t < 0
for e in d[:-1]:
    print(e + d[-1])
