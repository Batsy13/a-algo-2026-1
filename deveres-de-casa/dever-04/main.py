import math

def recursive_function(n):
    if n == 1:
        return 2
    
    return 2 * recursive_function(n-1) + pow(n,2)

quest1 = int(input("Enter a number: "))

if quest1 <= 0:
    print("Enter a valid number (greater than 0)")
else:
    print(recursive_function(quest1))