from typing import List

# Given an array of numbers and a target number, return the indices of two numbers in the array that
# add up to the target number:

# Example:
# numbers = [2, 7, 11, 15]
# target_number = 18
# The function should return a tuple of the indices of the numbers [1, 2], because (7 + 11 = 18)
#
# Validation:
# -> forbid any zero or lower target_number
# -> forbid any zero or negatives in array of numbers.

# Performance:
# -> slice out any numbers that exceed target - they will never be considered anyway

# Logic:
# -> loop in a loop
# -> start with first := array[0] and second := array[-1]
# -> step to next iteration if first + second exceeds target
# -> return on match


class InvalidTargetError(Exception):
    """This class represents an error when the target number is invalid, e.g. zero or lower."""

    def __init__(self, target_number: List[int]):
        super().__init__(f"The target number {target_number!r} must be non-zero and non-negative!")


class InvalidSourceNumbersArrayError(Exception):
    """This class represents an error when the source numbers are at least partially invalid, e.g.
    zero, or negative."""

    def __init__(self, source_numbers: List[int]):
        super().__init__(f"Numbers in the source array {source_numbers!r} contain invalid elements")


class NoSolutionError(Exception):
    """This class represents an error when the set of input and output numbers do not have a
    solution."""

    def __init__(self, target_number: int, source_numbers: List[int]):
        message = (
            f"There are no numbers in the soruce array {source_numbers!r} that equal to"
            f" {target_number}"
        )
        super().__init__(message)


def find_number_ids_that_sum_to(
    *, target_number: int, from_source_array: List[int]
) -> tuple[int, int]:
    if target_number < 1:
        raise InvalidTargetError(target_number)
    if any(filter(lambda i: i < 1, from_source_array)):
        raise InvalidSourceNumbersArrayError(from_source_array)

    source_array = list(filter(lambda num: num < target_number, from_source_array))
    source_array.sort()

    for first in source_array[::-1]:
        for second in source_array:
            print(f"{first=}, {second=}")
            if first + second > target_number:
                continue
            if first + second == target_number:
                # we're going from the end to start, so invert the order:
                return source_array.index(second), source_array.index(first)

    raise NoSolutionError(target_number=target_number, source_numbers=from_source_array)

def find_pairs_that_differ_by(amount: int, arr: List[int]):
    if amount == 0:
        raise ValueError("k = 0 is not allowed!")
    number_pairs = 0
    elements = set(arr)
    for i in arr:
        if (i + amount) in elements:
            print(f"{i=} + {amount=} in the set." )
            number_pairs += 1
        if (i - amount) in elements:
            print(f"{i=} + {amount=} in the set." )
            number_pairs += 1
    return number_pairs / 2


def find_longest_sequence(*, in_array: List[int]) -> tuple[int, int]:
    # number_map = {e: 0 for e in in_array}
    number_map = set(in_array)
    max_left_boundary = in_array[0]
    max_right_boundary = in_array[0]
    for i in in_array:
        sequence_length = 1
        left_boundary = i
        right_boundary = i
        is_left_bound_calculating = True
        is_right_bound_calculating = True
        while is_left_bound_calculating or is_right_bound_calculating:
            if left_boundary - 1 in number_map:
                sequence_length += 1
                left_boundary -= 1
            else:
                is_left_bound_calculating = False
            if right_boundary + 1 in number_map:
                sequence_length += 1
                right_boundary += 1
            else:
                is_right_bound_calculating = False
        if right_boundary - left_boundary > max_right_boundary - max_left_boundary:
            max_left_boundary = left_boundary
            max_right_boundary = right_boundary
    return max_left_boundary, max_right_boundary
