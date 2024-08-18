score = float(input())
if 80 <= score <= 100:
    print("A")
elif 75 <= score < 80:
    print("B+")
elif 70 <= score < 75:
    print("B")
elif 65 <= score < 70:
    print("C+")
elif 60 <= score < 65:
    print("C")
elif 55 <= score < 60:
    print("D+")
elif 50 <= score < 55:
    print("D")
elif 0 <= score < 50:
    print("F")
else:
    print("ERROR")
