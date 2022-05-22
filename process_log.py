
import math
import os
import random
import re
import sys


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

"""
check the number of access that reach threshold
Data structure: sender, recipient, value, concat by space, contains 0-9 only, and not started at 0, max length is 9
If sender equals recipient, it would count as once only
Result is expected to sorted by sender/recipient in ascending order (Not the total number of attempts)

Constraints:
n = number of logs
1 <= n and n <= math.pow(10, 5) and 1 <= threshold and threshold <= n

Input:
["89 99 5",
"99 89 12",
"12 12 5",
"55 99 20"]
Threshold = 2

Output: {'89': 2, '99': 3}
"""
def processLogs(logs, threshold):
    # Write your code here
    results = {}
    n = len(logs)
    # print(n)
    if 1 <= n and n <= math.pow(10, 5) and 1 <= threshold and threshold <= n:        
        for log in logs:
            # print(log)
            v = log.split(' ')
            sender = v[0]
            recipient = v[1]
            amount = v[2]
            
            # count = 0
            # for t in log.split(' '):
            #     if len(t) == 0 or len(t) > 9:
            #         next
            #     if count == 0:
            #         sender = t
            #     elif count == 1:
            #         recipient = t
            #     elif count == 2:
            #         amount = t
            #     if count > 2:
            #         break
            #     else:
            #         count += 1
            # print("sender: %s, recipient: %s, amount: %s" % (sender, recipient, amount))
            
            if sender in results:
                results[sender] = results.get(sender, 0)+ 1
            else:
                results[sender] = 1
            
            if sender != recipient:
                if recipient in results:
                    results[recipient] = results.get(recipient, 0)+ 1
                else:
                    results[recipient] = 1
    result = {k:v for (k, v) in results.items() if v >= threshold}
    # sortedresult = sorted(result.items(), key = lambda x: x[1], reversed = True)
    sortedresult = dict(sorted(result.items(), key=lambda item: int(item[0])))
    # print(results)
    # print(result)
    print(sortedresult)
    return sortedresult

# Sample
logs = [
            "89 99 5",
            "99 89 12",
            "12 12 5",
            "55 99 20"
        ]
threshold = 2
result = processLogs(logs, threshold)
# print(result)

# from original input

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     logs_count = int(input().strip())

#     logs = []

#     for _ in range(logs_count):
#         logs_item = input()
#         logs.append(logs_item)

#     threshold = int(input().strip())

#     result = processLogs(logs, threshold)

#     fptr.write('\n'.join(result))
#     fptr.write('\n')

#     fptr.close()
