from typing import Any, Sequence


def unique_in_order(sequence: Sequence[Any]) -> list:
    """
    Function takes as argument a sequence and returns a list of items
    without any elements with the same value next to each other
    and preserving the original order of elements.

    For example:

    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
        :param sequence: Any type of sequence (str., list, etc.)
    """
    result = []
    if len(sequence) != 0:
        result.append(sequence[0])
        for ind, element in enumerate(sequence):
            if sequence[ind] == result[-1]:
                continue
            else:
                result.append(element)
    return result


print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order("ABBCcAD"))
print(unique_in_order(""))
