from day14data import simple_test_data, data
import numpy as np
from collections import Counter, defaultdict

#data = simple_test_data

def combine_dicts(left:dict, right:dict) -> dict:
    for key, value in right.items():
        left[key] += value
    return left

steps = 40
template = data[0]
pairs, new_chars = np.array(data[1]).T
pair_counts = defaultdict(int)
letter_counts = defaultdict(int)

for i in range(len(template)):
    letter = template[i]
    letter_counts[letter] += 1

for i in range(len(template) - 1):
    search = template[i:i+2]
    pair_counts[search] += 1

for _ in range(steps):
    new_pairs = defaultdict(int)
    for key in pair_counts:
        val = pair_counts[key]
        pair_counts[key] -= val
        idx = np.where(pairs == key)[0][0]
        new_char = new_chars[idx]
        new_l = key[0] + new_char
        new_r = new_char + key[1]
        letter_counts[new_char] += val
        new_pairs[new_l] += val
        new_pairs[new_r] += val
    pair_counts = combine_dicts(pair_counts, new_pairs)
    new_pairs.clear()
res = [v for k, v in letter_counts.items()]
most = max(res)
least = min(res)
print(most - least)

