def rec_product(a, b):
    if (b == 0):
        return(0)
    if (b < 0):
        return(rec_product(a, (b + 1)) - a)
    return(a + rec_product(a, (b - 1)))


x = rec_product(5, 2)
print(x)

x = rec_product(-5, 2)
print(x)

x = rec_product(5, -2)
print(x)

x = rec_product(-5, -2)
print(x)