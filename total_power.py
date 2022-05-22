#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findTotalPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#

def findTotalPower(power):
    # Write your code here
    if not power:
        return 0
    n = len(power)
    min_val = 0
    sum_val = 0
    total = 0
    # print("p: %s, n: %s" % (power, n))
    for i in range(n):
        # initial min_val should be the first element
        if min_val == 0:
            min_val = power[i]
            
        # the list for comparison min and calc sum    
        remaining = power[i+1:]
        m = len(remaining)
        
        # calc the first element
        sum_val += power[i]
        total += min_val * sum_val
        # print("min: %s, sum: %s" % (min_val, sum_val))   
        
        # loop the remaining list, compare the min, add to total
        # print("r: %s, m: %s" % (remaining, m))
        for j in range(m):
            if remaining[j] < min_val:
                min_val = remaining[j]
            sum_val += remaining[j]
            total += min_val * sum_val
            # print("min: %s, sum: %s" % (min_val, sum_val))   
        # print("i: %s, total: %s" % (i, total))
        
        # reset min_val, sum_val for next iteration
        min_val = 0
        sum_val = 0
    #version 1
    # for i in range(n):
    #     remaining = power[i:]
    #     m = len(remaining)
    #     min_val = power[i]
    #     sum_val = 0
    #     for j in range(m):
    #         if j == 0:
    #             sum_val = power[i]   
    #         if i == j and j > 0:
    #             sum_val += remaining[j]
    #         if i < j:
    #             sum_val += remaining[j]
    #             if remaining[j] < min_val:
    #                 min_val = remaining[j]
    #         # elif i == j:
    #         #     sum_val = power[i]   
    #         # else:
    #         #     sum_val += remaining[j]
    #         total += min_val * sum_val
    #         print("min: %s, sum: %s" % (min_val, sum_val))   
            
    #         # print(total)
    #     print("i %s, total: %s" % (i, total))
        
        
    return total 
       
# def findTotalPower_v2(power):
#     # Write your code here
#     if not power:
#         return 0
#     n = len(power)
#     min_val = 0
#     sum_val = 0
#     total = 0

#     #version 1
#     for i in range(n):
#         remaining = power[i:]
#         m = len(remaining)
#         min_val = power[i]
#         sum_val = 0
#         for j in range(m):
#             if j == 0:
#                 sum_val = power[i]   
#             if i == j and j > 0:
#                 sum_val += remaining[j]
#             if i < j:
#                 sum_val += remaining[j]
#                 if remaining[j] < min_val:
#                     min_val = remaining[j]
#             # elif i == j:
#             #     sum_val = power[i]   
#             # else:
#             #     sum_val += remaining[j]
#             total += min_val * sum_val
#             # print("min: %s, sum: %s" % (min_val, sum_val))   
            
#             # print(total)
#         # print("i %s, total: %s" % (i, total))
        
        
#     return total   

inputs = [[2, 1, 3],
[9, 8, 8, 8, 7, 7, 6, 5, 5, 5],
[19, 19, 12, 15, 17, 20, 12, 14, 18, 18, 17, 19, 10, 11, 11, 12, 17, 17, 18, 11, 15, 11, 20, 10, 10, 20, 14, 15, 19, 19, 17, 13, 17, 17, 18, 14, 13, 16, 13, 14, 14, 16, 19, 16, 18, 19, 16, 11, 20, 10],
[30, 30, 30, 31, 31, 31, 31, 31, 32, 32, 32, 32, 33, 33, 33, 34, 34, 35, 35, 36, 36, 38, 40, 40, 40, 41, 41, 42, 43, 43, 44, 44, 45, 45, 45, 45, 46, 46, 47, 47, 47, 48, 50, 50, 50, 51, 51, 53, 53, 54, 54, 55, 57, 58, 58, 58, 58, 59, 59, 61, 61, 61, 63, 63, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 69, 70, 70, 71, 72, 72, 73, 73, 73, 74, 74, 74, 74, 76, 76, 77, 77, 78, 78, 78, 79, 79, 80, 80, 80, 80],
[625074647, 590937692, 952909273, 441099971, 266283305, 283046279, 255732073, 588141254, 657819970, 165660334, 410986119, 593013313, 323220122, 345122391, 257703182, 784368873, 958920333, 248822924, 184915452, 56451642, 105530844, 328213336, 252737523, 481519091, 503886123, 113226061, 349670329, 224762520, 392170369, 367325185, 73563320, 202427887, 883893451, 517189772, 988661631]
]

for s in inputs:
    result = findTotalPower(s)
    print("s: %s, \n result: %s" % (s, result))
    # result2 = findTotalPower_v2(s)
    # print("s: %s, \n result: %s, result2: %s" % (s, result, result2))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     power_count = int(input().strip())

#     power = []

#     for _ in range(power_count):
#         power_item = int(input().strip())
#         power.append(power_item)

#     result = findTotalPower(power)

#     fptr.write(str(result) + '\n')

#     fptr.close()
