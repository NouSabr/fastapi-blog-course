iter_list = iter(['Item1', 'Item2', 'Item3'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))


def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))