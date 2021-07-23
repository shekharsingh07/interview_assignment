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
def sep_sum_func(input_fact):
    sep_array = []
    # 1. Separating digits:
    while input_fact !=0:
        x = np.mod(input_fact, 10)      # Dividing by 10, the mod is separating the value
        input_fact = input_fact//10     # Updating input_fact with the quotient o dividing by 10
        sep_array.insert(0,x)           # adding the remainder value for each loop until input_fact reaches zero

    # 2. Summing values:
    fact_sum = np.sum(sep_array)
    return fact_sum

def main(user_input):
    # 1. Calculate factorial of input number
    input_fact = np.math.factorial(user_input)

    # 2. Separate digits and sum them:
    fact_sum = sep_sum_func(input_fact)

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
