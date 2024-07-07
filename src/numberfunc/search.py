from enum import IntEnum
from typing import List

class QueryType(IntEnum):
    INSERT_ONE = 1
    DELETE_ONE = 2
    CHECK_INTEGER_FREQUENCY = 3

OperationsList = List[List[int]]

# Complete the freqQuery function below.
def query_for_information(queries: OperationsList) -> List[int]:
    data: dict[int, int] = {}

    def insert_one(data: dict[int, int], value) -> int | None:
        if value in data:
            data[value] += 1
            return
        data[value] = 1
        
    def delete_one(data: dict[int, int], value) -> int | None:
        if value not in data:
            return
        if data[value] > 1:
            data[value] -= 1
            return
        data.pop(value)

    def check_frequency(data: dict[int, int], value) -> int | None:
        frequencies = data.values()
        return 1 if value in frequencies else 0

    operations = {
        QueryType.INSERT_ONE: insert_one,
        QueryType.DELETE_ONE: delete_one,
        QueryType.CHECK_INTEGER_FREQUENCY: check_frequency
    }
    response_array = []
    for operation_id, argument in queries:
        response = operations[operation_id](data, argument)
        if isinstance(response, int):
            response_array.append(response)
    return response_array

if __name__ == "__main__":
    operations: OperationsList = [
        [QueryType.INSERT_ONE, 5],
        [QueryType.INSERT_ONE, 6],
        [QueryType.CHECK_INTEGER_FREQUENCY, 2],
        [QueryType.INSERT_ONE, 10],
        [QueryType.INSERT_ONE, 10],
        [QueryType.INSERT_ONE, 6],
        [QueryType.DELETE_ONE, 5],
        [QueryType.CHECK_INTEGER_FREQUENCY, 2]
    ]
    query_results = query_for_information(operations)
    print(query_results)
