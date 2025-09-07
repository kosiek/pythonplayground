
from collections import Counter

from assertpy import assert_that, soft_assertions


def makeAnagram1(a: str, b: str):
    counts_a = Counter(a)
    counts_b = Counter(b)
    all_chars = set(counts_a.keys()) | set(counts_b.keys())
    deletions = 0
    for char in all_chars:
        deletions += abs(counts_a[char] - counts_b[char])
    return deletions


makeAnagram = makeAnagram1


def test_make_anagram():
    with soft_assertions():
        assert_that(makeAnagram("cde", "abc")).is_equal_to(4)
        # assert_that(makeAnagram("iamlordstupidvoldemord", "tombadmarvoloriddle")).is_equal_to(9)
        assert_that(
            makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")
        ).is_equal_to(30)
