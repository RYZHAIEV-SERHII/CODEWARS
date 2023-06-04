def first_non_repeating_letter(s):
    # Для збереження кількості входжень кожного символу у рядок,
    # ми використовуємо словник.
    counts = {}
    # Проходимось по рядку та заповнюємо словник з відповідними літерами та їх кількістю.
    for char in s:
        char_lower = char.lower()
        counts[char_lower] = counts.get(char_lower, 0) + 1
    # Проходимось по рядку ще раз, та знаходимо перший символ,
    # кількість входжень якого дорівнює 1.
    for char in s:
        char_lower = char.lower()
        if counts[char_lower] == 1:
            return char
    # Якщо жоден символ не входить лише один раз,
    # повертаємо пустий рядок або None.
    return ""
