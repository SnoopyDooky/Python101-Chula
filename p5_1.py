f = open("data.txt", "r")
section = input()
Sum = 0; n = 0
for line in f:  # id:name:section:score
    line = line.strip()
    # find index of first, second, and third colon
    i_first = line.find(":")
    i_second = line.find(":", i_first+1)
    i_third = line.find(":", i_second+1)
    sec = line[i_second+1:i_third]
    if section == sec:
        score = float(line[i_third+1:])
        n += 1
        Sum += score
f.close()
if n > 0:
    print(Sum / n)  # average score
else:
    print("Not Found")
