#1609
# Given an array of length 24, each element represents the number of new subscribers during the corresponding hour.
# Implement a data structure that:
# Increment the element at index hour by value.
# Retrieve the number of subscribers that have signed up between start and end (inclusive).

import random

class hashtable:

    def __init__(self):
        self.hashmap = [0]*24

    def index(self,x):
        return x % len(self.hashmap)

    def update(self, hour, value):
        mod = self.index(hour)
        self.hashmap[mod] += value

    def query(self, start, end):
        mod_start = self.index(start)
        mod_end = self.index(end)
        count = 0
        for i in range(mod_start,mod_end+1):
            count += self.hashmap[i]
        return count

def main():
    random.seed(3)

    sub1 = random.sample(range(0,101),24)
    sub2 = random.sample(range(0,450),24)

    h = hashtable()
    for i,v in enumerate(sub1):
        h.update(i,v)
    print(h.query(2,4))

    h2 = hashtable()
    for i,v in enumerate(sub2):
        h2.update(i,v)
    print(h2.query(2,4))

main()

