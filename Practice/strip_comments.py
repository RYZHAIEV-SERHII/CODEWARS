def strip_comments(strng: str, markers: list[str]):
    """
    Function to clear text from a specific symbols.
    :param strng: Given text to be cleared
    :param markers: Specified symbols to be removed from given text.
    :return: Cleared text.
    """
    lines = strng.split("\n")
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index].rstrip()
        lines[i] = line.rstrip()

    return "\n".join(lines)
