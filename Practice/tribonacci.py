def tribonacci(signature: list, n: int) -> list:
    """
    Well met with Fibonacci bigger brother, AKA Tribonacci.
    As the name may already reveal, it works basically like a Fibonacci,
    but summing the last 3 (instead of 2) numbers of the sequence to generate the next.

        :param signature: list of 3 started numbers
        :param n: quantity of generated numbers in sequence
        :return: list with generated sequence
    """
    result = signature.copy()
    while len(result) < n:
        result.append(sum(result[-3:]))

    return result[:n]


print(tribonacci([300, 200, 100], 0))
print(tribonacci([3, 2, 1], 10))
