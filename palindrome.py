#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minSwapsRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# https://stackoverflow.com/questions/72017854/minimum-number-of-swaps-required-to-make-a-binary-string-palindrome

def minSwapsRequired(s):
    # Write your code here        
    count = 0
    n = len(s)
    
    if isPalindrome(s):
        return count
    
    print("s: %s, n: %s, %s" % (s, n, n // 2))
    """
    Check from index 0 to middle of the length
    check if the mirrored element equals
    if already palindrome, return 0
    as the values contains on 0 and 1, 
    if the length is even number:
        the number of 0 and 1 should be even
        if the difference is odd number, it can never be palindrome
    if the length is odd:
        the number of 0 or 1 should be odd, another should be even
    count the number of difference, plus 1 for diff<2, then divide by 2 as swap from another position
    """
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            count += 1
            print("i: %s, n-1-i: %s, %s, %s" % (i, n//2, s[i], s[n-1-i]))
    if count %2 == 1 and n %2 ==0:
        return -1

    # for i, v in enumerate(s):
    #     if i < n-1:
    #         t = list(s)
    #         t[i], t[i+1] = t[i+1], t[i]
    #         count += 1
    #         t = ''.join(t)
    #         if isPalindrome(t):
    #             # return count
    #             if min_swap > 0 and min_swap > count:
    #                 min_swap = count
    #             print("Palindrome: %s, origin: %s" % (t, s))    
    return (count + 1) // 2

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
txt = ["0010010", "010000", "111000", "1010110", "100"]

for t in txt:
    min_swap = minSwapsRequired(t)
    print("t: %s, min_swap: %s" % (t, min_swap))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = minSwapsRequired(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
