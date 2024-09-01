def last_digit(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    else:
        a_last_digit = a % 10
        b_last_digit = b % 4 + 4 if b % 4 == 0 else b % 4
        return pow(a_last_digit, b_last_digit, 10)


print(last_digit(9, 7))
print(last_digit(2**200, 2**300))
print(last_digit(0, 0))
