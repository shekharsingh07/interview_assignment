#/usr/bin/env python3
# ------------------------------------------
# Creator: Shekhar Singh
# Date: 20/07/2021 
# Project: Corigine Technical Assignment
# Description: This program will find the sum of the digits of the factorial of the input number.
# ------------------------------------------

import numpy as np
import sys

def sep_func(fact_input):
    sep_array = []
    while fact_input !=0:
        x = np.mod(fact_input, 10)
        fact_input = fact_input//10
        sep_array.insert(0,x)
    return sep_array

def main(user_input = int(sys.argv[1]):
    # 1. Calculate factorial of input number
    fact_input = np.math.factorial(user_input)
    # 2. Seperate digits and sum them:
    sep_digits = sep_func(fact_input)
    fact_sum = np.sum(sep_digits)
    # 3. Print output value:
    print(fact_sum)
