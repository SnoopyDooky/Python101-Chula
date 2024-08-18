def sumlist(x):
    sum_of_integer = 0
    for e in x:
        if type(e) == list:
            sum_of_integer += sumlist(e)
        else:
            sum_of_integer += e
    return sum_of_integer


print(eval(input().strip()))
