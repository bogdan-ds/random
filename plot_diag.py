import matplotlib.pyplot as plt
import random


if __name__ == "__main__":
    rand_num = random.random()
    probabilities = [0.01, 0.1, 0.3, 0.58, 0.01]

    prob_sum = 0.0
    intermediate_sum = list()
    for p in probabilities:
        prob_sum += p
        intermediate_sum.append(prob_sum)

    x = [i for i in range(0, len(probabilities))]
    y = intermediate_sum
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.plot(x, y, "ro")
    plt.grid(True)
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, f"({i_x}, {i_y})\nR "
                           f"({round(rand_num, 2)}) < {i_y}: {rand_num < i_y}")
    plt.xlabel("Iteration step")
    plt.ylabel("Probability sum")
    plt.savefig("assets/diag.png")
