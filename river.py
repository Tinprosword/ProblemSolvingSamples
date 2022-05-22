from collections import deque
import numpy as np
"""
2D-Array contains only 0 and 1 and the size maybe not equal
Rivers are those with 1, the length of the river is calculated by the number of adjacent river but not diagonal 
Determine the total length of river is whatever sequence

e.g.
[
    [0, 0, 0, 1, 0]
    [0, 0, 1, 1, 0]    
    [1, 1, 1, 0, 0]
    [0, 0, 0, 0, 1]
]

1. Start with the first element with 1, river
2. Count the adjacent elements that contains 1
3. Store the elements already used
4. Repeat until the end of the array

Reference:
https://www.youtube.com/watch?v=lFseCKh6Ndw
https://leetcode.com/problems/number-of-islands/
https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/
https://www.javatpoint.com/bfs-vs-dfs
BFS: first in first out, add all adjacent nodes to queue
vertex-based technique to find the shortest path in a graph.
DFS: last in first out, any node can consider as root
edge-based technique because the vertices along the edge are explored first from the starting to the end node.
add only 1 adjacent node to stack
backtracking: from root to leaf, remove top, check if any unvisited node for the next, if so, add to the top
"""

map1 = [
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1]
        ]

# possible move: Up, Left, Right, Down
row_move = [0, -1, 0, 0]
col_move = [-1, 0, 1, 1]

def find_river(map):
    if not map:
        return []
    array = np.array(map)
    # rivers = np.argwhere(array == 1)
    # print(rivers)
    
    rivers_pos = []
    count = 0
    river_length = 0    
    rivers = [] 
    (M, N) = (len(array), len(array[0])) 
    print("Length of map: %s x %s" % (M, N))
    # Create map to indicate if position already used
    used_pos = [[False for x in range(N)] for y in range(M)]  
    q = deque()
    """
    Find all the river position
    """
    for i in range(M):
        for j in range(N):
            if array[i][j] == 1 and not used_pos[i][j]:  
                count += 1       
                river_length = 0         
                rivers_pos.append([i, j])
                used_pos[i][j] = True
                """
                BFS approach
                Count and calculation the length of each
                
                1. Loop through each river position
                2. check if the position being used
                3. If position is not used, river length+1, add to used_position
                4. the number of river and length of each of it would be the total count
                """
                q.append([i, j])
                while len(q):
                    river_length += 1
                    point = q.popleft()
                    row = point[0]
                    col = point[1]
                    # print(point)
                    # Check the point for all possible movement
                    # Check if index outbound and position already visited
                    # Up, Left, Right, Down                                       
                    if row-1 >= 0 and array[row-1][col] == 1 and not used_pos[row-1][col]:
                        used_pos[row-1][col] = True
                        q.append([row-1, col])                        
                        # print("Up")
                    if col-1 >= 0 and array[row][col-1] == 1 and not used_pos[row][col-1]:
                        used_pos[row][col-1] = True
                        q.append([row, col-1])                        
                        # print("Left")
                    if col+1 < N and array[row][col+1] == 1 and not used_pos[row][col+1]:
                        used_pos[row][col+1] = True
                        q.append([row, col+1])                        
                        # print("Right")
                    if row+1 < M and array[row+1][col] == 1 and not used_pos[row+1][col]:
                        used_pos[row+1][col] = True
                        q.append([row+1, col])                        
                        # print("Down")
                rivers.append(river_length) 
    # print(rivers_pos)
    # print(river_length)
    print(rivers)
    return rivers



result = find_river(map1)
print("Number of river: %s" % len(result))
# print(result)