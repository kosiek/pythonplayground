
from assertpy import assert_that, soft_assertions


def alternatingCharactersNaive(text: str) -> int:
    required_deletions = 0
    previous_char = text[0]
    for char in text[1:]:
        if char == previous_char:
            required_deletions += 1
        previous_char = char
    return required_deletions

alternatingCharacters = alternatingCharactersNaive

def test_alternating_characters():
    with soft_assertions():
        assert_that(alternatingCharacters("AABABAB")).is_equal_to(1)
        assert_that(alternatingCharacters("AAAA")).is_equal_to(3)
        assert_that(alternatingCharacters("ABABAB")).is_equal_to(0)
        assert_that(alternatingCharacters("BABA")).is_equal_to(0)
        assert_that(alternatingCharacters("AAABBB")).is_equal_to(4)
