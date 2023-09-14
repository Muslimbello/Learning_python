#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input().strip())

    def my_loop(value):
        for i in range(2, 5):
            if value == i:
                return value

    def my_sec_loop(value):
        for i in range(6, 21):
            if value == i:
                return value

    is_less_range = my_loop(n)

    is_big_range = my_sec_loop(n)

    is_not_even = n % 2 == 1

    is_even = n % 2 == 0

    greater = n > 20

    if is_not_even:
        print("Weird")
    elif is_even and is_less_range:
        print("Not Weird")
    elif is_even and is_big_range:
        print("Weird")
    if is_even and greater:
        print("Not Weird")
