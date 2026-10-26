# Bug Fixing Using Cursor AI

A buggy Python program that was diagnosed and corrected with the help of Cursor AI.

## Files

- `buggy_original.py`: the program with three bugs
- `fixed.py`: the corrected program, with `# FIX` comments and `assert` checks

## The bugs and the fixes

| # | Function | Bug | Result before | Fix |
|---|---|---|---|---|
| 1 | `sum_of_digits` | `str(n)[:-1]` skipped the last digit | `6` instead of `10` | Loop over every digit |
| 2 | `is_palindrome` | Compared the text as-is, so `"Madam"` failed | `False` instead of `True` | Lowercase the text and remove spaces first |
| 3 | `second_largest` | Returned the last item after sorting, which is the largest | `9` instead of `7` | Sort the unique values and return the second from the end |

## How the bugs were found

1. Ran `buggy_original.py` and compared each printed value with the expected value in the comments.
2. Asked Cursor AI to explain why each result was wrong.
3. Applied each fix, then added `assert` checks in `fixed.py` to prove they work.

## How to run

```bash
python buggy_original.py   # wrong output: 6, False, 9
python fixed.py            # All checks passed.
```

## Technologies

Python 3, Cursor AI, Git
