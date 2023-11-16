# Exercise 1
def compute_max_value(n_list): # name of function, and parameter(n-list)
    max_value = 0 # variable initialize to 0
    for num in n_list: # for each number
        if num > max_value: # check if number is greater than max_value
            max_value = num
    return max_value

n_list = [3,2,-3, 9 ,4]
max_value = compute_max_value(n_list)
print(max_value)

# Exercise 2
def computing_max_value(number_list):
    maximum_value = 0
    for number in number_list:
       if number > maximum_value:
           maximum_value = number

    return maximum_value

listings = [4, 3, 8, -9, 10]
maximum_value = computing_max_value(listings)
print(maximum_value)

# Exercise 3
def give_max_value(num_list):
    maxvalue = 0
    for numbers in num_list:
        if numbers > maxvalue:
            maxvalue = numbers
    return maxvalue

few_list = [13, 84, 59, 27, 33, 75]
maxvalue = give_max_value(few_list)
print(maxvalue)
