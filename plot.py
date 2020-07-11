'''
Given a matrix of 0's and 1's with plot = 1 and parking lot = 0,
find out 
Assume there is a Land on top which a Builder decides to build a gated community. 
So he prepares an entire black/white schematic as to how this plot is to be built. 
This Black and White Image of the entire plot is fed to an Image Processing system. 
Let us assume that all of the dark area in this image corresponds to the parking area of this plot(0). 
If there are adjacent dark areas, it is still considered to be belonging to a single plot. 
Write a Polynomial Time algorithm for this Image processing system which indicates the number of parking lots and size of the largest parking lot ?

Example:
input:
[
    [0, 1, 0, 0]
    [0, 1, 0, 0]
    [0, 1, 0, 0]
    [1, 1, 0, 0]
    [0, 1, 0, 0]
    [0, 1, 1, 0]
    [1, 0, 0, 0]
    ]
output: [3, 12]
'''

def plot() -> List[int, int]:
    x, y = map(int, input().split(' '))
    matrix = []
    count_list = []
    count = 0
    for i in range(x): matrix.append([int(input()) for j in range(y)]) 
    queue = []
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == 0:
                count = 0
                queue.append([i,j])
                while queue:
                    row, col = queue.pop(0)
                    count += 1
                    matrix[row][col] = 1
                    if col+1 < y and matrix[row][col+1] == 0 and [row, col+1] not in queue:
                        queue.append([row, col+1])
                    if col-1 >= 0 and matrix[row][col-1] == 0 and [row, col-1] not in queue:
                        queue.append([row, col-1])
                    if row+1 < x and matrix[row+1][col] == 0 and [row+1, col] not in queue:
                        queue.append([row+1, col])
                    if row-1 >= 0 and matrix[row-1][col] == 0 and [row-1, col] not in queue:
                        queue.append([row-1, col])
                count_list.append(count)
    return([len(count_list), max(count_list)])