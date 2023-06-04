def alphanumeric(password):
    import re

    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, password))


print(alphanumeric('Hello world'))
print(alphanumeric('PassWord'))
print(alphanumeric('        '))
