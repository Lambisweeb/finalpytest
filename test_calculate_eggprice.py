from calculate_eggcost import  calculate_eggcost

def test_result_egg_n1():
    num_eggs = -1
    expected_result = "Invalid input. Number of eggs cannot be negative."
    actual_result =  calculate_eggcost(num_eggs)
    assert expected_result == actual_result

def test_result_egg_12():
    num_eggs = 12
    expected_result = "Cost: 36 baht for 12 eggs."
    actual_result =  calculate_eggcost(num_eggs)
    assert expected_result == actual_result

def test_result_egg_60():
    num_eggs = 60
    expected_result = "Cost: 175 baht for 60 eggs."
    actual_result =  calculate_eggcost(num_eggs)
    assert expected_result == actual_result

def test_result_egg_0():
    num_eggs = 0
    expected_result = "Cost: 0 baht for 0 eggs."
    actual_result =  calculate_eggcost(num_eggs)
    assert expected_result == actual_result

def test_result_egg_59():
    num_eggs = 59
    expected_result = "Cost: 177 baht for 59 eggs."
    actual_result =  calculate_eggcost(num_eggs)
    assert expected_result == actual_result

def test_result_egg_11():
    num_eggs = 11
    expected_result = "Cost: 44 baht for 11 eggs."
    actual_result =  calculate_eggcost(num_eggs)
    assert expected_result == actual_result