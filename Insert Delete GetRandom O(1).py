import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        x = self.index[val]
        last_digit = self.arr[-1]

        self.arr[x] = last_digit
        self.index[last_digit] = x

        self.arr.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
y=RandomizedSet
r=y.insert((10))
print(r)



        
