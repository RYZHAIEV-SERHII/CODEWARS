# import unittest
#
# from greed import score
#
#
# class GreedTest(unittest.TestCase):
#     def test_greed(self):
#         self.assertEqual(score([5, 1, 3, 4, 1]), 250)
#         self.assertEqual(score([1, 1, 1, 3, 1]), 1100)
#         self.assertEqual(score([2, 3, 4, 6, 2]), 0)
#         self.assertEqual(score([4, 4, 4, 3, 3]), 400)
#         self.assertEqual(score([2, 4, 4, 5, 4]), 450)
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

from greed import score


def test_score():
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
