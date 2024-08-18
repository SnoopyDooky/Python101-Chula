isbn = input()
n1, n2, n3, n4, n5, n6, n7, n8, n9 = [int(e) for e in isbn]
s = 10*n1 + 9*n2 + 8*n3 + 7*n4 + 6*n5 + 5*n6 + 4*n7 + 3*n8 + 2*n9
# (s + n10) % 11 == 0
# s + n10 = 11k, k is integer
# therefore: k = s//11 + 1
# and n10 = 11k - s = 11(s//11 + 1) - s
n10 = 11 * (s//11 + 1) - s
print(isbn + str(n10))
