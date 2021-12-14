from day14data import simple_test_data, data
import numpy as np
from collections import Counter

#data = simple_test_data

steps = 10
template = data[0]
start, end = np.array(data[1]).T

result = template
for step in range(steps):
    step_result = ""
    for i in range(len(result)):
        search = result[i:i+2]
        try:
            idx = np.where(start == search)[0][0]
            addition = search[0] + end[idx]
        except:
            addition = search[0]
        step_result += addition
    result = step_result

res_count = Counter(result).most_common(26)
most = res_count[0][1]
least = res_count[-1][1]
print(f"result = {most - least}")