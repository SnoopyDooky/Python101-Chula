d = []  # list of integer
t = int(input())
while t != -1:
    d.append(t)
    t = int(input())
for e in d:
    if d.count(e) > len(d)/2:
        print(e)
        break
else:
    print("Not Found")
