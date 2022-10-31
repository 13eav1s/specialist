from itertools import combinations
from typing import List


def path_length(a: dict, b: dict) -> float:
    return ((b['x'] - a['x']) ** 2 + (b['y'] - a['y']) ** 2) ** 0.5


def solution(arr: List[dict]) -> float:
    points = ''
    for i in range(len(arr)):
        points += str(i)
    all_combinations = set(combinations(points*len(points), len(points)))
    result_combinations = []
    for i in all_combinations:
        flag = 0
        for j in points:
            if i.count(j) != 1:
                flag = 1
                break
        if flag == 0:
            result_combinations.append(i)
    min_length = 99999
    for i in range(len(result_combinations)):
        length = 0
        for j in range(1, len(result_combinations[i])):
            length += path_length(arr[int(result_combinations[i][j - 1])], arr[int(result_combinations[i][j])])
        if min_length > length:
            min_length = length
    return min_length


lst = [
    {'x': 0, 'y': 0},
    {'x': 0, 'y': -3},
    {'x': 0, 'y': 2},
    {'x': 0, 'y': 3},
]
print(solution(lst))
