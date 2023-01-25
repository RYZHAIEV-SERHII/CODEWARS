def array_diff(a, b):
    return [num for num in a.copy() if num not in b]


print(array_diff([1, 1, 2], [1]))
print(array_diff([1, 1, 2], []))
