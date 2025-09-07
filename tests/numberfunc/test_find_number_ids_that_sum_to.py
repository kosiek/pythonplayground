# type: ignore
# ruff: noqa

from assertpy import assert_that
from pytest import fixture, raises

from numberfunc.number_generations import (
    InvalidSourceNumbersArrayError,
    InvalidTargetError,
    NoSolutionError,
    find_number_ids_that_sum_to,
)


@fixture
def sample_valid_numbers_and_solutions_set() -> tuple[int, list[int]]:
    # Simplify: just find a hardcoded set
    # would be best to use data driven tests with multiple sets:
    target_number = 42
    source_numbers = [1, 3, 4, 5, 6, 7, 14, 22, 27, 31, 38, 45, 49]
    id_first = 2
    id_second = 10
    return target_number, source_numbers, id_first, id_second


@fixture
def sample_invalid_set_with_zero_or_negative_target_number() -> tuple[int, list[int]]:
    # Simplify: just find a hardcoded set
    # would be best to use data driven tests with multiple sets:
    target_number = -1
    source_numbers = [1, 3, 5, 6, 7, 14, 22, 27, 31, 38, 45, 49]
    id_first = -1
    id_second = -1
    return target_number, source_numbers, id_first, id_second


@fixture
def sample_invalid_set_with_zero_or_negative_in_source_numbers() -> tuple[int, list[int]]:
    # Simplify: just find a hardcoded set
    # would be best to use data driven tests with multiple sets:
    target_number = 12
    source_numbers = [1, 3, 5, 6, 7, 14, 22, 27, -1, 38, 45, 49]
    id_first = -1
    id_second = -1
    return target_number, source_numbers, id_first, id_second


@fixture
def sample_unsolvable_set() -> tuple[int, list[int]]:
    # Simplify: just find a hardcoded set
    # would be best to use data driven tests with multiple sets:
    target_number = 17
    source_numbers = [12, 13, 14, 15, 16, 21, 37]
    id_first = -1
    id_second = -1
    return target_number, source_numbers, id_first, id_second


def test_find_number_ids_that_sum_to(
    sample_valid_numbers_and_solutions_set: tuple[int, list[int], int, int],
) -> None:
    target, source, sol_id_first, sol_id_second = sample_valid_numbers_and_solutions_set
    id_first, id_second = find_number_ids_that_sum_to(
        target_number=target, from_source_array=source
    )
    assert_that(id_first).is_equal_to(sol_id_first)
    assert_that(id_second).is_equal_to(sol_id_second)


def test_find_number_ids_that_sum_to_fails_on_negative_target_number(
    sample_invalid_set_with_zero_or_negative_target_number: tuple[int, list[int], int, int],
) -> None:
    target, source, _, _ = sample_invalid_set_with_zero_or_negative_target_number
    with raises(InvalidTargetError, match=f"{target!r}"):
        find_number_ids_that_sum_to(target_number=target, from_source_array=source)


def test_find_number_ids_that_sum_to_fails_on_any_zero_or_negative_in_source_numbers(
    sample_invalid_set_with_zero_or_negative_in_source_numbers: tuple[int, list[int], int, int],
) -> None:
    target, source, _, _ = sample_invalid_set_with_zero_or_negative_in_source_numbers
    with raises(InvalidSourceNumbersArrayError, match=f"{source!r}"):
        find_number_ids_that_sum_to(target_number=target, from_source_array=source)


def test_find_number_ids_that_sum_to_fails_on_unsolvable_set(
    sample_unsolvable_set: tuple[int, list[int], int, int],
) -> None:
    target, source, _, _ = sample_unsolvable_set
    with raises(NoSolutionError):
        find_number_ids_that_sum_to(target_number=target, from_source_array=source)
