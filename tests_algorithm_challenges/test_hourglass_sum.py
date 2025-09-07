
import sys

from assertpy import assert_that
from pytest import mark


def get_max_hourglass_sum(array: list[list[int]]) -> int:

    result: int = -sys.maxsize

    for row in range(len(array) - 2):
        for column in range(len(array[row]) - 2):
            # An hourglass contains 7 values, named from A to G:
            a = array[row][column]
            b = array[row][column + 1]
            c = array[row][column + 2]
            d = array[row + 1][column + 1]
            e = array[row + 2][column]
            f = array[row + 2][column + 1]
            g = array[row + 2][column + 2]
            hourglass_sum = a + b + c + d + e + f + g
            # print(f"start {row=}, {column=}, {hourglass_sum=}")
            if hourglass_sum > result:
                result = hourglass_sum

    return result

hourglassSum = get_max_hourglass_sum

tests_cond1_positive = [
    [
        19,
        [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ]
    ],
    [
        -6,
        [
            [-1, -1, 0, -9, -2, -2],
            [-2, -1, -6, -8, -2, -5],
            [-1, -1, -1, -2, -3, -4],
            [-1, -9, -2, -4, -4, -5],
            [-7, -3, -3, -2, -9, -9],
            [-1, -3, -1, -2, -4, -5],
        ]
    ]
]

@mark.parametrize(["answer", "array"], tests_cond1_positive)
def test_results(answer: int, array: list[list[int]]):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- text: {array} ---\n"
    )
    result = hourglassSum(array)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)
