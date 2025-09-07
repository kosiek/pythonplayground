from collections import Counter

from assertpy import assert_that
from pytest import mark


def get_smallest_subarray_size_with_same_degree_brute(array: list[int]) -> int:
    occurences = Counter(array)
    array_degree_data = occurences.most_common(1)[0]
    array_degree_value = array_degree_data[0]
    array_degree = array_degree_data[1]
    # print(f"{array_degree=} for "{array_degree_value=})

    if array_degree == 1:
        return 1
    if array_degree == len(array):
        return len(array)

    result = len(array)
    for maximum_length in range(2, len(array)):
        for start in range(len(array) - maximum_length + 1):
            end = start + maximum_length
            subarray = array[start:end]
            # print(subarray)
            subarray_counter = Counter(subarray)
            subarray_degree = subarray_counter.most_common(1)[0]
            if subarray_degree[1] == array_degree:
                result = len(subarray)
    return result


def get_smallest_subarray_size_with_same_degree_brute2(array: list[int]) -> int:
    frequencies = Counter(array)
    array_degree_data = frequencies.most_common(1)[0]
    array_degree_value = array_degree_data[0]
    array_degree = array_degree_data[1]

    if array_degree == 1:
        return 1
    # if array_degree == len(array):
    #     return len(array)

    smallest_array_len = len(array)
    for window_size in range(2, len(array)):
        frequency_window = Counter(array[0 : window_size - 1])
        # print(f"initial for {window_size=}: {frequency_window=}")
        for window_start in range(0, len(array) - window_size):
            # print(f"=== {window_size=}, {window_start=}")
            first_window_value = array[window_start]
            last_window_value = array[window_start + window_size - 1]
            frequency_window[last_window_value] += 1
            # print(f"{frequency_window=}")
            current_subarray = array[window_start : window_start + window_size]
            # print(f"{current_subarray=}")
            subarray_degree = frequency_window.most_common(1)[0]
            if subarray_degree[1] == array_degree and len(current_subarray) < smallest_array_len:
                # print(f"Update: {smallest_array_len=} > {subarray_degree[1]}")
                smallest_array_len = len(current_subarray)
            frequency_window[first_window_value] -= 1
    return smallest_array_len


my_func = get_smallest_subarray_size_with_same_degree_brute2

tests = [
    [2, [1, 2, 2, 3, 4]],
    [3, [1, 2, 3, 2, 4]],
    [5, [1, 1, 1, 1, 1]],
    [1, [1, 2, 3, 4, 5]],
]


@mark.parametrize(["answer", "array"], tests)
def test_is_valid(answer: int, array: list[int]):
    print(f"{'=' * 3} NEXT TEST {'=' * 3}\n--- expect: {answer} ---\n--- array: {array} ---\n")
    result = my_func(array)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)
