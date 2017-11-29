def is_isogram(string):
    seen = set()

    for char in string.lower():
        if not char.isalpha():
            continue

        if char in seen:
            return False

        seen.add(char)

    return True
