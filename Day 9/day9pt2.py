import numpy as np
from itertools import permutations

from day9data import data as data

cardinal_dirs = [dir for dir in permutations([-1, 0, 1], 2) if abs(dir[0]) != abs(dir[1])]

def is_low_point(row: int, col: int) -> bool:
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
    

token = -1
def flood_fill(row:int , col:int) -> None:
    height = data[row][col]
    if height != token and height != 9:
        data[row][col] = token
        for dir in cardinal_dirs:
            new_row = row + dir[0]
            new_col = col + dir[1]
            shape = np.shape(data)
            if new_row == shape[0] or new_col == shape[1] or new_row < 0 or new_col < 0:
                continue
            flood_fill(new_row, new_col)



lows = []
for i, row in enumerate(data):
    for j, height in enumerate(row):
        if is_low_point(i, j):
            lows.append([[i,j],height])


for lp_coords, height in lows:
    flood_fill(lp_coords[0], lp_coords[1])
    token -= 1

values, counts = np.unique(data, return_counts=True)
counts = sorted(counts, reverse=True)
print(np.prod(counts[1:4]))

