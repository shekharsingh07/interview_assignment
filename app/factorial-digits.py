#/usr/bin/env python3
# ------------------------------------------
# Creator: Shekhar Singh
# Date: 20/07/2021 
# Project: Corigine Technical Assignment
# Description: This program will find the sum of the digits of the factorial of the input number.
# ------------------------------------------

import numpy as np
import sys

# Function to seperate and add the digits of the factorial:
def separate_sum_func(input_fact):
    separate_array = []
    # 1. Separating digits:
    while input_fact !=0:
        remainder = np.mod(input_fact, 10)      # Dividing by 10, the mod is separating the value
        input_fact = input_fact//10             # Updating input_fact with the quotient o dividing by 10
        separate_array.insert(0,remainder)      # adding the remainder value for each loop until input_fact reaches zero

    # 2. Summing values:
    fact_sum = np.sum(separate_array)
    return fact_sum

def main(user_input):
    # 1. Calculate factorial of input number
    input_fact = np.math.factorial(user_input)

    # 2. Separate digits and sum them:
    answer = separate_sum_func(input_fact)

    # 3. Print output value:
    print(answer)

if __name__ == "__main__":
    try:
        user_input = int(sys.argv[1])
        if user_input < 0:                      # Factorials of negative integers are invalid
            print("Invalid! Please enter a positive integer.")
        elif isinstance(user_input,float):
            print("Invalid! Please enter a positive integer")
        else:
            main(user_input)
    except ValueError:
        print("Error! Please enter a positive value of int type")
