"""
Gas station
Given 1 list of gas station filling capacity and another for the cost traveling to the next 
If the gas become negative, it would not be able to get to next gas station
To indicate the first station that could travel all stations

Time complexity = n iteration, each O(1), total O(n)
Space complexity = 4 variable, O(1)
Ref: 
https://www.youtube.com/watch?v=Peq4GCPNC5c
"""

gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]

def find_candidate_station(gas, cost):
    remaining = 0
    candidate = 0
    n = len(gas)
    
    for i in range(n):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i + 1
            remaining = 0
            
    prev_remaining = sum(gas[:candidate]) - sum(cost[:candidate])
    # print("Candidate: %s, Remaining: %s, Prev: %s" % (candidate, remaining, prev_remaining))    
    if candidate == n or remaining + prev_remaining < 0:
        return -1
    else:
        return candidate
            
            
result = find_candidate_station(gas, cost)
print(result)            