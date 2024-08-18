x = float(input())
total = 0; n = 0
while x != -1:
    total += x
    n += 1
    x = float(input())
if n == 0:
    print("No Data")
else:
    print(total / n)
