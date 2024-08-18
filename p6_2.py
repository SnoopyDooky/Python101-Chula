d = []  # [[-score, id], ...]
t = input().split()
while len(t) > 1:
    d.append([-float(t[1]), int(t[0])])
    t = input().split()
student_id = int(t[0])  # student ID that needs to find rank
d.sort()
for i in range(len(d)):
    if student_id == d[i][1]:   # found student ID
        print(i + 1)    # rank
        break
else:
    print("Not Found")
