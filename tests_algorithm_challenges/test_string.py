
from collections import Counter

from assertpy import assert_that, soft_assertions


def get_anagram_pairs_count_o_n3(text: str) -> int:
    anagrams = 0
    for window_size in range(1, len(text)):
        print(f"\tAnagrams of length {window_size}")
        for text_start in range(len(text) - window_size + 1):
            text_end = text_start + window_size
            substring = text[text_start:text_end]
            substring_counter = Counter(substring)
            print(f"\t\tSubstring of size {window_size}: {substring}")
            for match_start in range(text_start + 1, len(text) - window_size + 1):
                match_end = match_start + window_size
                match = text[match_start:match_end]
                match_counter = Counter(match)
                print(f"\t\t\tCompare {substring} vs {match}")
                if substring_counter == match_counter:
                    print(f"\t\t\t\tAnagram pair:  {substring} & {match}")
                    anagrams += 1
    print(f"TOTAL: {anagrams}")
    return anagrams


anagrams = get_anagram_pairs_count_o_n3


def test_anagrams():
    with soft_assertions():
        print("===\nCASE: 'mom' (expect: 2)\n---")
        assert_that(anagrams("mom")).is_equal_to(2)

        print("===\nCASE: 'kkkk' (expect: 10)\n---")
        assert_that(anagrams("kkkk")).is_equal_to(10)

        print("===\nCASE: 'abba' (expect: 4)\n---")
        assert_that(anagrams("abba")).is_equal_to(4)

        # assert_that(anagrams("caca")).is_equal_to(3)

        print("===\nCASE: 'abcd' (expect: 0)\n---")
        assert_that(anagrams("abcd")).is_equal_to(0)

        print("===\nCASE: 'ifailuhkqq' (expect: 3)\n---")
        assert_that(anagrams("ifailuhkqq")).is_equal_to(3)
