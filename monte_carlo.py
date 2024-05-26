import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6)


def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        results[total] += 1
    return results


def calculate_probabilities(results, num_rolls):
    probabilities = {k: (v / num_rolls) * 100 for k, v in results.items()}
    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    plt.bar(sums, probs)
    plt.title('Probability Distribution of Dice Rolls')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.xticks(sums)
    plt.show()


def main():
    num_rolls = 1000000
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
