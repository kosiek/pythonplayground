from numberfunc.number_generations import find_longest_sequence
from pytest import fixture
from pytest import mark
from assertpy import assert_that, soft_assertions

from typing import List, Tuple
import random

@fixture
def sample_valid_numbers_and_solutions_set() -> tuple[List[int], int, int]:
    source_numbers = [1, 3, 4, 5, 6, 7, 14, 22, 23, 24, 25, 26, 27, 30]
    return source_numbers, 22, 27

test_iterations: tuple[List[int], int, int] = [
        ([1, 3, 4, 5, 6, 7, 14, 22, 23, 24, 25, 26, 27, 30], 22, 27),
        ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41], 2, 3),
        ([10, 12, 13, 14, 15, 20, 21, 22, 23, 24], 20, 24),
        ([1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19], 6, 12),
        ([5, 6, 9, 10, 11, 12, 13, 14, 18, 19, 20, 21, 22], 9, 14),
        ([3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 8, 20),
        ([100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], 102, 113),
        ([33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 33, 50),
        ([55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], 55, 70),
        ([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], 75, 95)
    ]

def test_basic_find_longest_sequence(
    sample_valid_numbers_and_solutions_set: tuple[List[int], Tuple[int, int]],
) -> None:
    (
        source_numbers,
        expect_start_number,
        expect_end_number
    ) = sample_valid_numbers_and_solutions_set
    id_first, id_second = find_longest_sequence(
        in_array=source_numbers
    )
    with soft_assertions():
        assert_that(id_first).is_equal_to(expect_start_number)
        assert_that(id_second).is_equal_to(expect_end_number)


@mark.parametrize("numbers, expected_start, expected_end", test_iterations)
def test_find_longest_sequence_ddt(numbers, expected_start, expected_end):
    random.shuffle(numbers)
    start, end = find_longest_sequence(in_array=numbers)
    with soft_assertions():
        assert_that(start).described_as(
            f"Expected start of sequence: {expected_start}, but got: {start}"
        ).is_equal_to(expected_start)
        assert_that(end).described_as(
            f"Expected end of sequence: {expected_end}, but got: {end}"
        ).is_equal_to(expected_end)