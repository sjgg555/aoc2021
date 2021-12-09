test_data = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
[3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
[9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
[8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
[9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]

simple_test_data = [
    [0,1,2,3,4],
    [1,2,3,4,5],
    [2,3,2,5,6],
    [3,4,5,6,9],
    [4,5,6,9,8],
]

import numpy as np
from itertools import permutations
from day9data import data as data

def is_low_point(row: int, col: int) -> bool:
    cardinal_dirs = [dir for dir in permutations([-1, 0, 1], 2) if abs(dir[0]) != abs(dir[1])]
    for dir in cardinal_dirs:
        new_row = row + dir[0]
        new_col = col + dir[1]
        shape = np.shape(data)
        if new_row == shape[0] or new_col == shape[1] or new_row < 0 or new_col < 0:
            continue
        height = data[row][col]
        new_height = data[new_row][new_col]
        if new_height <= height:
            return False
    return True

lows = []
total = 0
for i, row in enumerate(data):
    for j, height in enumerate(row):
        if is_low_point(i, j):
            total += (height + 1)
            lows.append([[i,j],height])
print(total)

