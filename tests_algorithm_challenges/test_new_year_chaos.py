
from assertpy import assert_that
from pytest import mark


def get_minimum_queue_bribes(final_order: list[int]) -> str:
    bribes = 0
    for idx in range(len(final_order)):
        person = final_order[idx]
        place = idx + 1
        # print(f"{person=} on {place=}")
        if person - place > 2:
            return "Too chaotic"
        for lower_person in final_order[place:]:
            if person > lower_person:
                bribes += 1
    return str(bribes)


def get_minimum_queue_bribes_perf(final_order: list[int]) -> str:
    bribes = 0
    order = [i - 1 for i in final_order]
    for place in range(len(order)):
        person = final_order[place]
        if person - place - 1 > 2:
            return "Too chaotic"
        for lower_person_id in range(place, len(order)):
            if person > final_order[lower_person_id]:
                bribes += 1
    return str(bribes)

minimumBribes = get_minimum_queue_bribes_perf

tests_cond1_positive = [
    [
        "0",
        [1, 2, 3, 4, 5],
    ],
    [
        "3",
        [2, 1, 5, 3, 4],
    ],
    [
        "Too chaotic",
        [2, 5, 1, 3, 4],
    ],
    [
        "7",
        [1, 2, 5, 3, 7, 8, 6, 4],
    ],
]

@mark.parametrize(["answer", "chaotic_order"], tests_cond1_positive)
def test_results(answer: int, chaotic_order: list[int]):
    print(
        f"{'=' * 3} NEXT TEST {'=' * 3}\n"
        f"--- expect: {answer} ---\n"
        f"--- end order: {chaotic_order} ---\n"
    )
    result = minimumBribes(chaotic_order)
    print(f"--- result {result} ---")
    assert_that(result).is_equal_to(answer)
