def order(sentence):
    new_sentence = ""
    nums = []
    for word in sentence.split():
        for x in word:
            if x.isdigit():
                nums.append(x)
    result = dict(zip(nums, sentence.split()))
    new_sentence = " ".join(result.get(k) for k in sorted(result))
    return new_sentence


print(order("is2 Thi1s T4est 3a"))
