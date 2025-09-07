
from collections import deque

from assertpy import assert_that
from pytest import mark


def rotate_array(array: list[int], rotations: int) -> list[int]:

    mod = deque(array)
    for _ in range(rotations % len(array)):
        value = mod.popleft()
        mod.append(value)
        print(f"rotation #{_ + 1}: {array} -> {mod}")
    return list(mod)

rotLeft = rotate_array

tests_cond1_positive = [
    [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        0,
    ],
    [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        5,
    ],
    [
        [3, 4, 5, 1, 2],
        [1, 2, 3, 4, 5],
        2,
    ],
    [
        [1, 2, 3, 4, 5],
        [3, 4, 5, 1, 2],
        3,
    ],
    [
        [1, 2, 3, 4, 5],
        [5, 1, 2, 3, 4],
        6,
    ],
]

@mark.parametrize(["answer", "array", "rotations"], tests_cond1_positive)
def test_results(answer: int, array: list[int], rotations: int):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {array} ---\n"
    )
    result = rotLeft(array, rotations)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)
