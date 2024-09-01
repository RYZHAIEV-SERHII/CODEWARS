class Adder:
    def __init__(self, value=0):
        self.value = value

    def __call__(self, x):
        return Adder(self.value + x)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return self.value + other

    def __int__(self):
        return self.value


# # Usage examples:
# result1 = Adder(1)
# print(result1)  # Output: 1
#
# result2 = Adder(1)(2)
# print(result2)  # Output: 3
#
# result3 = Adder(1)(2)(3)
# print(result3)  # Output: 6
#
# result4 = Adder(1)(2)(3)(4)
# print(result4)  # Output: 10
#
# result5 = Adder(1)(2)(3)(4)(5)
# print(result5)  # Output: 15
#
# # Storing and reusing returned values
# addTwo = Adder(2)
# print(addTwo)  # Output: 2
# print(addTwo + 5)  # Output: 7
# print(addTwo(3))  # Output: 5
# print(addTwo(3)(5))  # Output: 10
