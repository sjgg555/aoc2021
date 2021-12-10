from day10data import test_data, data

#data = test_data

pairs = ["{}", "<>", "()", "[]"]

def complete_pair(left:str, right:str) -> bool:
    return any([True if left in pair and right in pair else False for pair in pairs])

def calc_score(popped:str) -> int:
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

stack = []
incorrect = []
total_score = 0
for row in data:
    for item in row:
        if item == "{" or item == "(" or item == "[" or item == "<":
            stack.append(item)
        else:
            popped = stack.pop()
            if not complete_pair(popped, item):
                total_score += calc_score(item)
                incorrect.append(item)
                break

print(total_score)

