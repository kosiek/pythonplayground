
from assertpy import soft_assertions


def twoStrings(s1: str, s2: str):
    print(f"Comparing '{s1}' and '{s2}' to check whether one string is a substring of the other.")
    longer_string = s1 if len(s1) > len(s2) else s2
    shorter_string = s2 if len(s1) > len(s2) else s1
    for window_size in range(1, len(longer_string) + 1):
        if window_size > len(shorter_string):
            break
        print(f"\tChecking substrings of size {window_size}")
        for start in range(len(longer_string) + 1):
            end = start + window_size
            if end > len(longer_string):
                break
            test_substring = longer_string[start:end]
            if len(test_substring) > len(longer_string):
                break
            print(f"\t\tChecking if '{test_substring}' is in '{shorter_string}'")
            if test_substring in shorter_string:
                print("\t\tSUCCESS!")
                return "YES"
    return "NO"


def test_two_strings():
    with soft_assertions():
        assert twoStrings("hello", "world") == "YES"
        assert twoStrings("hi", "world") == "NO"
        assert twoStrings("abc", "def") == "NO"
        assert twoStrings("abc", "cde") == "YES"
        assert twoStrings("abcdefg", "xyz") == "NO"
        assert twoStrings("abcdefg", "fg") == "YES"
