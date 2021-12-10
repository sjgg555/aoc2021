from day10data import test_data, data

#data = test_data

pairs = ["{}", "<>", "()", "[]"]

def complete_pair(left:str, right:str) -> bool:
    return any([True if left in pair and right in pair else False for pair in pairs])


def get_closer(item:str):
    for pair in pairs:
        if item in pair:
            return pair[1]


def calc_corrupt_score(item:str) -> int:
    if item == ")":
        return 3
    elif item == "]":
        return 57
    elif item == "}":
        return 1197
    elif item == ">":
        return 25137
    else:
        return "woops"


def calc_autocomplete_score(item:str, current_score:int) -> int:
    current_score *= 5
    addition = 0
    if item == ")":
        addition = 1
    elif item == "]":
        addition =  2
    elif item == "}":
        addition =  3
    elif item == ">":
        addition =  4
    else:
        addition = "woops"
    return current_score + addition


pt1_score = 0
pt2_scores = []
for row in data:
    stack = []
    score = 0
    for item in row:
        if item == "{" or item == "(" or item == "[" or item == "<":
            stack.append(item)
        else:
            popped = stack.pop()
            if not complete_pair(popped, item):
                pt1_score += calc_corrupt_score(item)
                stack.clear()
                break
    while len(stack) != 0:
        score = calc_autocomplete_score(get_closer(stack.pop()), score)
    if score != 0: pt2_scores.append(score)

        
print(pt1_score)
test = sorted(pt2_scores)
idx = int(len(pt2_scores) / 2)
print(test[idx])