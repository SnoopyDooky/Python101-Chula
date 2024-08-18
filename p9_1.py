import numpy as np

x = [int(e) for e in input().split()]
rentalrates = np.array(x)
sales = np.ndarray((4, 5), int)
for k in range(4):
    sales[k] = [int(e) for e in input().split()]
totalsales = np.sum(sales, axis=0)
d = np.argmax(totalsales)
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
print(days[d], totalsales[d])
salesvalues = rentalrates.dot(sales)
for e in salesvalues:
    print(e, end=" ")
