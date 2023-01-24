def is_pangram(s):
    from string import ascii_lowercase
    letters = ''
    for char in s:
        if char.isalpha():
            letters += char.lower()
    return True if ''.join(sorted(set(letters))) == ascii_lowercase else False


s = 'The quick brown fox jumps over the lazy dog'
print(is_pangram(s))