import numpy as np


def fib(n, k):  # Fn (mod k)
    I = np.identity(2, int)
    A = np.array([[0, 1], [1, 1]])

    def a(n):  # A^n (mod k) = (A (mod k))^n
        if n == 0: return I
        B = a(n // 2)  # recursion
        if n % 2 == 0: return B.dot(B) % k
        return A.dot(B.dot(B)) % k

    return a(n)[0, 1]


n, k = [int(e) for e in input().split()]
print(fib(n, k))
