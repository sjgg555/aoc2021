from day11data import test_data, simple_test_data, data
import itertools
import numpy as np

# data = simple_test_data
#data = test_data

steps = 100000
dirs = [dir for dir in itertools.product([-1, 0, 1], repeat=2)]
initial_flashes = []
has_flashed = np.zeros(np.shape(data), dtype=int)
total_flashes = 0

def flash_and_continue(row:int, col:int) -> None:
    has_flashed[row][col] = 1
    data[row][col] = 0
    global total_flashes 
    total_flashes += 1
    for dir in dirs:
        new_row = row + dir[0]
        new_col = col + dir[1]
        shape = np.shape(data)
        if new_row == shape[0] or new_col == shape[1] or new_row < 0 or new_col < 0:
            continue
        if has_flashed[new_row][new_col] != 1:
            data[new_row][new_col] += 1
        if data[new_row][new_col] > 9:
            if has_flashed[new_row][new_col] != 1:
                flash_and_continue(new_row, new_col)


for step in range(steps):
    for row in range(len(data)):
        for col in range(len(data[0])):
            data[row][col] += 1
            if data[row][col] > 9:
                data[row][col] = 0
                initial_flashes.append([row, col])
                if len(initial_flashes) == (len(data) * len(data[0])):
                    print(step - 9)
                    exit()

    for flash in initial_flashes:
        flash_and_continue(flash[0], flash[1])
    
    has_flashed.fill(0)
    initial_flashes.clear()

print(total_flashes)
