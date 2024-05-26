def greedy_algorithm(foods, budget):
    sorted_items = sorted(foods.items(), key=lambda x: x[1].get('calories') / x[1].get('cost'), reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for food, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(food)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= list(items.values())[i - 1]['cost']:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - list(items.values())[i - 1]['cost']] + list(items.values())[i - 1]['calories'])

    # Відновлення оптимального набору страв
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= list(items.values())[i - 1]['cost']

    total_cost = sum(items[item]['cost'] for item in selected_items)
    total_calories = dp[n][budget]

    return selected_items, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


if __name__ == '__main__':
    budget = 100
    selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print("Вибрані страви:", selected_items_greedy)
    print("Загальна вартість:", total_cost_greedy)
    print("Загальна калорійність:", total_calories_greedy)

    selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
    print("\nАлгоритм динамічного програмування:")
    print("Вибрані страви:", selected_items_dp)
    print("Загальна вартість:", total_cost_dp)
    print("Загальна калорійність:", total_calories_dp)
