# Exercise 1
def list_average(number_list):
    return sum(number_list) / len(number_list)

number_list = []
for i in range(5): # this will be executed 5 times
    number_list.append(float(input("Give a number: "))) # cast float

print(list_average(number_list))

# Exercise 2
def num_avg(num_list):
    return sum(num_list)/len(num_list)

num_list = []
for i in range(5):
    num_list.append(float(input("Give a number")))

print(num_avg(num_list))

# Exercise 3
def total_avg(numbers):
    return sum(numbers)/len(numbers)

numbers = []

for i in range(5):
    numbers.append(float(input("Give a number: ")))

print(total_avg(numbers))
