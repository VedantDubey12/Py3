def sum_of_digits(n):
    total = 0
    for ch in str(n)[:-1]:
        total += int(ch)
    return total


def is_palindrome(text):
    return text == text[::-1]


def second_largest(numbers):
    numbers.sort()
    return numbers[-1]


print(sum_of_digits(1234))            # expected 10
print(is_palindrome("Madam"))         # expected True
print(second_largest([4, 9, 2, 7]))   # expected 7
