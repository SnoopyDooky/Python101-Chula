s = input() + " "
group = 0
for i in range(len(s)-1):
    if s[i] in "aeiou" and s[i+1] not in "aeiou":
        group += 1
print(group)
