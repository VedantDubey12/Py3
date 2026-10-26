def sum_of_digits(n):
    total = 0
    for ch in str(abs(n)):  # FIX 1: loop over ALL digits (the last one was skipped)
        total += int(ch)
    return total


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()  # FIX 2: ignore case and spaces
    return cleaned == cleaned[::-1]


def second_largest(numbers):
    unique = sorted(set(numbers))  # FIX 3: sort unique values, do not change the input
    if len(unique) < 2:
        raise ValueError("Need at least two different numbers.")
    return unique[-2]  # FIX 3: second from the end, not the last


assert sum_of_digits(1234) == 10
assert is_palindrome("Madam") is True
assert is_palindrome("race car") is True
assert is_palindrome("hello") is False
assert second_largest([4, 9, 2, 7]) == 7
assert second_largest([5, 5, 3]) == 3
print("All checks passed.")
