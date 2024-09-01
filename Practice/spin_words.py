def spin_words(sentence):
    new_sentence = sentence.split()
    for word in new_sentence:
        if len(word) > 4:
            new_sentence.insert(new_sentence.index(word), word[::-1])
            new_sentence.remove(word)
    return " ".join(new_sentence)


print(spin_words("Hey fellow warriors"))


# alternative solution
# def spin_words(sentence):
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
