from random import choice
from typing import List


def get_arrangement(floor_count: int,people_count: int)-> List[int]:
    arrangement = []
    for i in range(people_count):
        arrangement.append(choice(range(floor_count)))
    return arrangement

def elevator_experiment(n_iter = 10**3) -> float:
    cnt_arrangement_distinct_floor = 0
    for i in range(n_iter):
        if len((arrangement := get_arrangement(6, 3))) == len(set(arrangement)):
            cnt_arrangement_distinct_floor += 1
    return float(cnt_arrangement_distinct_floor)/float(n_iter)

print(elevator_experiment(10**6))



            