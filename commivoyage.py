def path_length(a: dict, b: dict):
    return ((b['x'] - a['x']) ** 2 + (b['y'] - a['y']) ** 2) ** 0.5


def find_next_point(current_point, arr, passed_points):
    min_leght = 9999999
    save_index = 0
    for i in range(len(arr)):
        if not arr[i] in passed_points:
            current_lenght = path_length(current_point, arr[i])
            if min_leght > current_lenght:
                min_leght = current_lenght
                save_index = i
    passed_points.append(arr[save_index])
    return min_leght


def solution(arr):
    passed_points = []
    point = arr[0]
    result = 0
    passed_points.append(arr[0])
    while len(passed_points) < len(arr):
        result += find_next_point(point, arr, passed_points)
        point = passed_points[len(passed_points) - 1]
    return result


lst = [
    {'x': 0, 'y': 1},
    {'x': 0, 'y': 9},
    {'x': 0, 'y': 2},
    {'x': 0, 'y': 5},
    {'x': 0, 'y': 3},
    {'x': 0, 'y': 4},
    {'x': 0, 'y': 6},
    {'x': 0, 'y': 7},
    {'x': 0, 'y': 8},

]
print(solution(lst))
