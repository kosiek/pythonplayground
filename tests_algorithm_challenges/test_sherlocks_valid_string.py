
from collections import Counter

from assertpy import assert_that
from pytest import mark


def is_valid(text: str) -> str:
    occurences = Counter(text)
    occurences_frequencies = Counter(occurences.values())
    # print(f"occurences: {occurences}")
    # print(f"occurences_spread: {occurences_frequencies}")
    # print(f"occurences_spread values: {occurences_frequencies.values()}")
    # Sherlock's string conditions:
    # Cond. 1: has same character frequencies:
    if len(occurences_frequencies.values()) == 1:
        return "YES"

    num_frequencies = len(occurences_frequencies.values())
    least_frequency = min(occurences_frequencies.keys())
    least_frequent_pair = list(filter(lambda i: i[0] == least_frequency, occurences_frequencies.items()))[0]
    most_frequency = max(occurences_frequencies.keys())
    most_frequent_pair = list(filter(lambda i: i[0] == most_frequency, occurences_frequencies.items()))[0]
    # print(f"least frequency pair: freq={least_frequent_pair[0]}, amount={least_frequent_pair[1]}")
    # print(f"most frequency pair: freq={most_frequent_pair[0]}, amount={most_frequent_pair[1]}")
    # Cond. 2.2: (least frequent character):
    # can be brought to the same frequency count by removing one occurence:
    if (
        num_frequencies == 2
        and least_frequent_pair[1] == 1 and least_frequent_pair[0] * least_frequent_pair[1] == 1
    ):
        return "YES"

    # Cond. 2.1: most frequent character:
    # can be brought to the same frequency count by removing one occurence - most frequent character
    if (
        num_frequencies == 2
        and most_frequent_pair[0] - least_frequent_pair[0] == 1 and most_frequent_pair[1] == 1
    ):
        return "YES"

    return "NO"

isValid = is_valid

tests_cond1_positive = [
    ["YES", "a"],
    ["YES", "ab"],
    ["YES", "aabbcc"],
]


@mark.parametrize(["answer", "test"], tests_cond1_positive)
def test_is_valid_cond1_positive(answer: str, test: str):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {test} ---\n"
    )
    result = isValid(test)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)

tests_cond1_negative = [
    ["NO", "badama"],
    ["NO", "aabbccddeefghi"],
]

@mark.parametrize(["answer", "test"], tests_cond1_negative)
def test_is_valid_cond1_negative(answer: str, test: str):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {test} ---\n"
    )
    result = isValid(test)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)

tests_cond2_1_positive = [
    # Yes: 'c' occurs 1 time more than 'a' and 'b'
    ["YES", "abcc"],
    # Yes: 'a' occurs 1 more time than 'b' and 'd'
    ["YES", "bada"],
]


@mark.parametrize(["answer", "test"], tests_cond2_1_positive)
def test_is_valid_cond2_1_positive(answer: str, test: str):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {test} ---\n"
    )
    result = isValid(test)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)

tests_cond2_2_positive = [
    # Yes: we can remove 'c' and all characters have occurence of '2':
    ["YES", "aabbc"],
    # Yes: we can remove one occurence of 'e' and then all letters have occurence of '2':
    ["YES", "abcdefghhgfedecba"],
    # Yes: all characters except 'n' occur 111 times, 'n' 1 time. Remove 'n' and it passes:
    ["YES", "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"],
]


@mark.parametrize(["answer", "test"], tests_cond2_2_positive)
def test_is_valid_cond2_2_positive(answer: str, test: str):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {test} ---\n"
    )
    result = isValid(test)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)


tests_cond2_2_negative = [
    # No: 'a' and 'b' occur 2 times, 'c' and 'd' as well, cannot bring to all x 2:
    ["NO", "aabbcd"],
]


@mark.parametrize(["answer", "test"], tests_cond2_2_negative)
def test_is_valid_cond2_2_negative(answer: str, test: str):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {test} ---\n"
    )
    result = isValid(test)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)
