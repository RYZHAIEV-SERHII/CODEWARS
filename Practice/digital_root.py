def digital_root(n):
    result = sum(int(num) for num in str(n))
    if len(str(result)) > 1:
        result = digital_root(result)
    return result


print(digital_root(493193))