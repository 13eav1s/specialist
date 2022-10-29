from typing import List

'''
00 01 02
10 11 12
20 21 22
'''


def snail(arr):
    result = []

    while True:

        # проход по верхней строчке
        for elem in arr[0]:
            result.append(elem)
        arr.pop(0)
        if len(arr) == 0:
            break

        #  Проход по правому столбцу
        for i in range(len(arr)):
            result.append(arr[i][len(arr[i]) - 1])
            arr[i].pop(len(arr[i]) - 1)
        if len(arr[0]) == 0:
            break

        #  Проход по нижней строчки
        st = arr[len(arr) - 1]
        st.reverse()
        for elem in st:
            result.append(elem)
        arr.pop(len(arr) - 1)
        if len(arr) == 0:
            break

        #  Проход по левому столбцу
        row = list()
        for i in range(len(arr)):
            row.append(arr[i][0])
            arr[i].pop(0)
        row.reverse()
        for elem in row:
            result.append(elem)
        if len(arr[0]) == 0:
            break
    return result


arr = [[1, 2, 3, 10],
       [8, 9, 4, 11],
       [7, 6, 5, 12],
       [13, 14, 15, 16]]
snail(arr)
