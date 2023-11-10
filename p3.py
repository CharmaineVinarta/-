Task 
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.

if __name__ == '__main__':
    n = int(input()) # This part of the code takes an integer input (n) from the user using the input() function and converts it into an integer using int().
    
    for i in range (n):
        print(i**2) # a for loop to iterate through all non-negative integers from 0 to n-1 (since the range(n) generates values from 0 to n-1). 
                    # In each iteration, it prints the square of the current number (i) using the print(i**2) statement.


# for example, 5, the program will print the squares of the non-negative integers less than 5:
# 0
# 1
# 4
# 9
# 16
# This is because 0**2 is 0, 1**2 is 1, 2**2 is 4, 3**2 is 9, and 4**2 is 16. The output will vary based on the user input for n.
