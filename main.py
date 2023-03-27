from calculate_eggcost import calculate_eggcost
print("how many egg you want to buy ?")
num_eggs = int(input())
cost = calculate_eggcost(num_eggs)
print(cost)
print("want to calculate again ?(yes/no)")
answer = input()
while answer =="yes":
    print("how many egg you want to buy ?")
    num_eggs = int(input())
    cost = calculate_eggcost(num_eggs)
    print(cost)
    print("want to calculate again ?(yes/no)")
    answer = input()
print("thankyou, come again")
    