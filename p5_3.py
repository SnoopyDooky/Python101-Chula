filename = input()
# [[number of first char, first char], ...]  ex. [[0, 'a'], [0, 'b'], [0, 'f']]
count = [[0, input()] for i in range(3)]  # 3 inputs
fin = open(filename, "r")
for line in fin:
    for e in line.strip():
        for i in range(3):
            if e == count[i][1]:
                count[i][0] += 1
fin.close()
count.sort(reverse=True)    # ex. [[4, 'a'], [3, 'f'], [1, 'b']]
print(count[0][1] + count[1][1] + count[2][1])
