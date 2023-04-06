import random

from typing import List


class RandomGen:

    def __init__(self, random_nums: List[int], probabilities: List[float]):
        if len(probabilities) != len(random_nums):
            raise ValueError("There should be as many probabilities as numbers")
        if sum(probabilities) != 1:
            raise ValueError("Probability sum should amount to 1")
        self._random_nums = random_nums
        self._probabilities = probabilities

    def next_num(self) -> int:
        random_num = random.random()
        probability_sum = 0.0
        for idx, probability in enumerate(self._probabilities):
            probability_sum += probability
            if random_num < probability_sum:
                return self._random_nums[idx]
