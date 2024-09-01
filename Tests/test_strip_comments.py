from Practice.strip_comments import strip_comments


def test_strip_comments():
    result = strip_comments(
        "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
    )
    assert result == "apples, pears\ngrapes\nbananas"
