def calculate_eggcost(num_eggs):
    if num_eggs < 0:
        return "Invalid input. Number of eggs cannot be negative."
    elif num_eggs < 12:
        return f"Cost: {num_eggs*4} baht for {num_eggs} eggs."
    elif num_eggs < 60:
        cost_per_egg = 3
        dozen_count = num_eggs // 12
        remainder_eggs = num_eggs % 12
        total_cost = dozen_count * 12 * cost_per_egg + remainder_eggs * cost_per_egg
        return f"Cost: {total_cost} baht for {num_eggs} eggs."
    else:
        dozen_count = num_eggs // 12
        total_cost = dozen_count * 35
        return f"Cost: {total_cost} baht for {num_eggs} eggs."