test_data = [3,4,3,1,2]
data = [3,4,1,2,1,2,5,1,2,1,5,4,3,2,5,1,5,1,2,2,2,3,4,5,2,5,1,3,3,1,3,4,1,5,3,2,2,1,3,2,5,1,1,4,1,4,5,1,3,1,1,5,3,1,1,4,2,2,5,1,5,5,1,5,4,1,5,3,5,1,1,4,1,2,2,1,1,1,4,2,1,3,1,1,4,5,1,1,1,1,1,5,1,1,4,1,1,1,1,2,1,4,2,1,2,4,1,3,1,2,3,2,4,1,1,5,1,1,1,2,5,5,1,1,4,1,2,2,3,5,1,4,5,4,1,3,1,4,1,4,3,2,4,3,2,4,5,1,4,5,2,1,1,1,1,1,3,1,5,1,3,1,1,2,1,4,1,3,1,5,2,4,2,1,1,1,2,1,1,4,1,1,1,1,1,5,4,1,3,3,5,3,2,5,5,2,1,5,2,4,4,1,5,2,3,1,5,3,4,1,5,1,5,3,1,1,1,4,4,5,1,1,1,3,1,4,5,1,2,3,1,3,2,3,1,3,5,4,3,1,3,4,3,1,2,1,1,3,1,1,3,1,1,4,1,2,1,2,5,1,1,3,5,3,3,3,1,1,1,1,1,5,3,3,1,1,3,4,1,1,4,1,1,2,4,4,1,1,3,1,3,2,2,1,2,5,3,3,1,1]

max_days = 80

#data = test_data

class Fish():
    def __init__(self, starting_count = 8) -> None:
        self.counter = starting_count
        self.first_time = True
    
    def decrement_and_spawn(self):
        self.counter -= 1
        if self.counter < 0:
            self.counter = 6
            return True
        return False

fishes = [Fish(timer) for timer in data]
new_fish = []

for day_num in range(max_days):
    for fish in fishes:
        if fish.decrement_and_spawn():
            new_fish.append(Fish())
    fishes.extend(new_fish)
    new_fish.clear()
    

print(len(fishes))