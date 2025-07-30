# Lab 3

# Task 1: Working with strings
food = 'chicken cutlets'
#print(food[0:3])
#print(food[-3:-1])
first_last = food[0]+ food[-1]
#print (first_last)
food_list = food.split()
#print(food_list)
joined_food =' '.join(food_list)
#print(joined_food)

# Task 2 working with lists
number_list = [1, 436463566554, 35, -7, 0, 234]
number_list.append(67)
#print(number_list)
number_list.insert(3, 1000)
number_list.pop()
#print(number_list)
number_list.remove(436463566554)
