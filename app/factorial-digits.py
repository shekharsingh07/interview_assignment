#/usr/bin/env python3
# ------------------------------------------
# Creator: Shekhar Singh
# Date: 20/07/2021 
# Project: Corigine Technical Assignment
# Description: This program will find the sum of the digits of the factorial of the input number.
# ------------------------------------------

import numpy as np
import sys

# Function to seperate the digits of the factorial:
def sep_func(fact_input):
    sep_array = []
    while fact_input !=0:
        x = np.mod(fact_input, 10)      # Dividing by 10, the mod is separating the value
        fact_input = fact_input//10     # Updating fact_input with the quotient o dividing by 10
        sep_array.insert(0,x)           # adding the remainder value for each loop until fact_input reaches zero
    return sep_array

def main(user_input):
    # 1. Calculate factorial of input number
    fact_input = np.math.factorial(user_input)

    # 2. Separate digits and sum them:
    sep_digits = sep_func(fact_input)
    fact_sum = np.sum(sep_digits)

    # 3. Print output value:
    print(fact_sum)

if __name__ == "__main__":
    try:
        user_input = int(sys.argv[1])
        if user_input < 0:              # Factorials of negative integers are invalid
            print("Invalid! Please enter a positive integer.")
        else:
            main(user_input)
    except:
        print("Error!")
