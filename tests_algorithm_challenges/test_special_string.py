

from assertpy import assert_that
from pytest import mark


def how_many_special_substrings_o_n2(textlen: int, text: str) -> int:
    """
    Determine how many special substrings a given string contains.

    A string is special if:
    - All characters are the same, e.g. 'aaaaaa'
    - All characters except the middle one are the same, e.g. 'aadaa'
    """
    result = 0

    for max_len in range(1, len(text) + 1):
        for start in range(len(text) - max_len + 1):
            end = start + max_len - 1
            substring = text[start:end + 1]
            # print(f"{max_len=}, substring: @{start=}, @{end=}, {substring=}")
            def test_same(i: str) -> bool:
                return i == substring[0]
            # print(f"\tresult total: {list(filter(test_same, substring))}")
            if len(list(filter(test_same, substring))) == len(substring):
                # print("\tyes, all characters are the same.")
                result += 1
                continue
            # replace middle character if string is odd:
            if len(substring) % 2 != 0:
                mid_idx = int(len(substring) / 2)
                modified = substring[:mid_idx] + substring[0] + substring[mid_idx + 1:]
                # print(f"\tThe string is odd, modified middle character: {modified}")
                if len(list(filter(test_same, modified))) == len(modified):
                    # print("\tyes, all characters (except the middle one) are the same.")
                    result += 1

    return result

from dataclasses import dataclass


def how_many_special_substrings(textlen: int, text: str) -> int:
    """
    Determine how many special substrings a given string contains.

    A string is special if:
    - All characters are the same, e.g. 'aaaaaa'
    - All characters except the middle one are the same, e.g. 'aadaa'
    """

    @dataclass
    class CharacterChain:
        char: str
        count: int

        def __repr__(self):
            return f"< char={self.char}, number={self.count} >"

    result: int = 0
    chain_sequence: list[CharacterChain] = []
    current_chain = CharacterChain(text[0], 1)

    for char in text[1:]:
        if char == current_chain.char:
            current_chain.count += 1
            continue
        # Chain broken:
        result += int((current_chain.count + current_chain.count ** 2) / 2)
        chain_sequence.append(current_chain)
        current_chain = CharacterChain(char, 1)

    chain_sequence.append(current_chain)
    for chain_a, chain_b, chain_c in zip(chain_sequence, chain_sequence[1:], chain_sequence[2:], strict=False):
        # print("=")
        # print(f"{chain_a=}")
        # print(f"{chain_b=}")
        # print(f"{chain_c=}")
        if chain_a.char == chain_c.char and chain_b.count == 1:
            result += min(chain_a.count, chain_c.count)

    result += int((current_chain.count + current_chain.count ** 2) / 2)
    return result

substrCount = how_many_special_substrings

tests_cond1_positive = [
    [7, 5, "asasd"],
    [10, 7, "abcbaba"],
    [12, 7, "aabaacc"],
    [10, 4, "aaaa"],
]

@mark.parametrize(["answer", "text_len", "text"], tests_cond1_positive)
def test_is_valid_cond1_positive(answer: int, text_len: int, text: str):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {text} ---\n"
    )
    result = substrCount(text_len, text)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)
