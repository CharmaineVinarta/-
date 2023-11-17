# Execise 1
def total_avg(number_list):
    return sum(number_list) / len(number_list)

number_list = [] # create a empty list

ask_user_for_numbers = True # create a boolean variable

while ask_user_for_numbers: # in while check some conditions
    user_input = float(input("Choose a number: "))
    if user_input == 0.0:
        ask_user_for_numbers = False
    else:
        number_list.append(user_input)
print(total_avg(number_list))

# Exercise 2
def avg_number(list_number):
    return sum(list_number)/len(list_number)

list_number = []
ask_user = True

while ask_user:
    user_inputs = float(input("Give a number: "))
    if user_inputs == 0.0:
        ask_user = False
    else:
        list_number.append(user_inputs)

print(avg_number(list_number))
