def make_int_list(x):
    return [int(e) for e in x.split()]


def is_odd(e):
    return e % 2 == 1


def odd_list(alist):
    return [e for e in alist if is_odd(e)]


def sum_square(alist):
    total = 0
    for e in alist:
        total += e**2
    return total


exec(input().strip())
