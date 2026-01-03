# Program for Summation of numbers passed through command line

import sys

sum_nos = 0
len_args = len(sys.argv)
for i in range(1, len_args):
    sum_nos = sum_nos + int(sys.argv[i])

print("The final sum of all numbers is:",+sum_nos)