def sum_of_squares(x,y):

    total = 0
    for i in range(x,y):
        total = total + i*i
    return total


def square_of_sums(x,y):

    total = 0
    for i in range(x,y):
        total += i

    total *= total
    return total


print(square_of_sums(1,101) - sum_of_squares(1,101))

