d = {}  # ex. {subject_id: set of student_id, ...}
t = input().split()
# add data to d
while int(t[0]) != -1:
    student_id = t[0]
    subject_id = set(t[1:])
    for e in subject_id:
        if e in d:
            d[e].add(student_id)
        else:
            d[e] = {student_id}
    t = input().split()
subject_id_input = input().split()
for e in subject_id_input:  # create empty set if subject_id_input not in dictionary
    if e not in d:
        d[e] = set()
student_in_subject_id1 = d[subject_id_input[0]]
student_in_subject_id2 = d[subject_id_input[1]]
a = len(student_in_subject_id1 & student_in_subject_id2)    # intersect
b = len((student_in_subject_id1 | student_in_subject_id2) - (student_in_subject_id1 & student_in_subject_id2))  # union - intersect
c = len(student_in_subject_id1 | student_in_subject_id2)    # union
print(a, b, c)
