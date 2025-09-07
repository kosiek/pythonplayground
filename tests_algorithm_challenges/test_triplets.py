
from assertpy import assert_that


def countTripletsBasic(arr: list[int], r: int):
    doublets: set[tuple[int, int]] = set()
    triplets: set[tuple[int, int, int]] = set()
    for i in range(len(arr)):
        # print(f"Iterate index {i}: {arr[i]}")
        next_value = arr[i] * r
        for search_index in range(i, len(arr)):
            # print(
            #     f"\t[Searching {next_value}] Search index {search_index}: {arr[search_index]} == {next_value=}?"
            # )
            if not arr[search_index] == next_value:
                continue
            # print("\t\tSUCCESS.")
            doublets.add((i, search_index))
    # print(f"Doublets:\n{doublets}")
    for doublet in doublets:
        first = doublet[0]
        second = doublet[1]
        next_value = arr[second] * r
        for search_index in range(second, len(arr)):
            # print(f"\t[Searching {next_value}] Search index {search_index}: {arr[search_index]}")
            if not arr[search_index] == next_value:
                continue
            triplets.add((first, second, search_index))
    # print(f"Triplets:\n{triplets}")
    return len(triplets)


def countTripletsHash(arr: list[int], r: int):
    total = 0
    occurences: dict[int, list[int]] = {}
    for index in range(len(arr)):
        value = arr[index]
        if value not in occurences:
            occurences[value] = [index]
            continue
        occurences[value].append(index)
    # print(f"Occurences map: {occurences}")
    for i in range(len(arr)):
        base = arr[i]
        second_geometry = base * r
        third_geometry = second_geometry * r
        # print(f"[{base=}] Searching for occurences of {second_geometry=} and {third_geometry=}")
        if second_geometry not in occurences:
            continue
        # print(f"\tsecond geometry found at indices: {occurences[second_geometry]=}")
        if third_geometry not in occurences:
            continue
        # print(f"\tthird geometry found at indices: {occurences[third_geometry]=}")
        total += len(occurences[second_geometry]) * len(occurences[third_geometry])
    return total


from collections import defaultdict


# Complete the countTriplets function below.
def countTripletsDefaultdict(arr: list[int], r: int):
    total = 0
    futures: dict[int, int] = defaultdict(int)
    found_pairs: dict[int, int] = defaultdict(int)
    for number in arr:
        total += found_pairs[number]
        found_pairs[number * r] += futures[number]
        futures[number * r] += 1
    return total


countTriplets = countTripletsDefaultdict


def test_count_triplets():
    assert_that(countTriplets([1, 2, 2, 4], 2)).is_equal_to(2)
    assert_that(countTriplets([1, 3, 9, 9, 27, 81], 3)).is_equal_to(6)
    assert_that(countTriplets([1, 5, 5, 25, 125], 5)).is_equal_to(4)

    assert_that(countTriplets([1, 2, 2, 4, 4], 2)).is_equal_to(4)


def test_count_triplets_100items():
    assert_that(countTriplets([1] * 100, 1)).is_equal_to(161700)
