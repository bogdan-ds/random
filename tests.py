import pytest

from generator import RandomGen


def test_probability_numbers_validation():
    random_nums = [-1, 0, 1, 2, 3, 4]
    probabilities = [0.01, 0.1, 0.3, 0.58, 0.01]
    with pytest.raises(ValueError, match="as many probabilities"):
        RandomGen(random_nums, probabilities)


def test_probability_validation():
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.4, 0.58, 0.1, 0.01]
    with pytest.raises(ValueError, match="should amount to"):
        RandomGen(random_nums, probabilities)


def test_weighted_random_numbers():
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.1, 0.3, 0.58, 0.01]
    random_gen = RandomGen(random_nums, probabilities)
    results = dict.fromkeys(random_nums, 0)
    for i in range(0, 100):
        num = random_gen.next_num()
        results[num] += 1
    p = [v/sum(results.values()) for v in results.values()]
    distance = 0.0
    for start_p, gen_p in zip(probabilities, p):
        distance += (start_p - gen_p)
    assert distance < 0.01
