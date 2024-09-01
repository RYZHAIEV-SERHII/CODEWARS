def score(dice: list[int]) -> int:
    """
    Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
    is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

     Three 1's => 1000 points
     Three 6's =>  600 points
     Three 5's =>  500 points
     Three 4's =>  400 points
     Three 3's =>  300 points
     Three 2's =>  200 points
     One   1   =>  100 points
     One   5   =>   50 point

    A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
    (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

    Example scoring

     Throw       Score
     ---------   ------------------
     5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
     1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
     2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

    :param dice: list of dice values
    :return: int
    """

    from collections import Counter

    dice_values = {
        1: {1: 100, 3: 1000},
        2: {3: 200},
        3: {3: 300},
        4: {3: 400},
        5: {1: 50, 3: 500},
        6: {3: 600},
    }

    total_score = 0
    count = Counter(dice)

    for value, quantity in count.items():
        if value == 1:
            if quantity >= 3:
                total_score += (
                    dice_values[value][3] + (quantity - 3) * dice_values[value][1]
                )
            else:
                total_score += quantity * dice_values[value][1]
        elif value == 5:
            if quantity >= 3:
                total_score += (
                    dice_values[value][3] + (quantity - 3) * dice_values[value][1]
                )
            else:
                total_score += quantity * dice_values[value][1]
        else:
            if quantity >= 3:
                total_score += dice_values[value][3]

    return total_score


# print(score([1, 1, 1, 3, 1]))  # 1100
