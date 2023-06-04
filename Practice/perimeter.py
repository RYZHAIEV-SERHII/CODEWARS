def perimeter(n):
    # Calculate the Fibonacci sequence up to n+1 terms
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    # Calculate the perimeter of each square and add them up
    perimeter = sum(4 * fib[i] for i in range(n + 1))

    return perimeter
