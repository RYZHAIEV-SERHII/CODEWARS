def pig_it(text):
    result = text.split()
    for word in result:
        if word[0].isalpha():
            new_word = f"{word[1:] + word[0] + 'ay'}"
            result.insert(result.index(word), new_word)
            result.remove(word)
        else:
            continue
    return " ".join(result)


print(pig_it("Pig latin is cool"))
print(pig_it("Hello world !"))


# alternative version
# import re
# def pig_it(text):
#     return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)
