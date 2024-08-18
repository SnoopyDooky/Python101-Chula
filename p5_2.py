fin = open("score.txt", "r")
sid = input().strip()
for line in fin:
    student_id, grade = line.strip().split()
    if sid == student_id:
        print(grade)
        break
else:
    print("Not Found")
fin.close()
