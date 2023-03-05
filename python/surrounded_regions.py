def discover(row_index, col_index, queue, region, visited):
    queue.append([row_index, col_index])
    region.append([row_index, col_index])
    visited[row_index][col_index] = True

# visit entire region and determine whether it is surrounded or not
# do not change any "O" to "X" yet
def find_region_and_capture(board, visited, start_pos):
    # use the queue to facilitate BFS
    queue = [start_pos]
    visited[start_pos[0]][start_pos[1]] = True
    # use region to accumulate all the indices that are a part of this region
    # another way of doing this that would save space is to move a left pointer oin the queue to the right
    # instead of popping the value off the queue
    region = [start_pos]
    # is_surrounded defaults as true, when an index that borders the edge of the board is found, is turned false
    is_surrounded = True

    while len(queue) > 0:
        curr = queue.pop()
        # check if bordering the edge of the board if we stil, think we are surrounded
        if is_surrounded and curr[0] == 0 or curr[0] == len(board) - 1 or curr[1] == 0 or curr[1] == len(board[0]) - 1:
            is_surrounded = False
        # check up neighbor
        if curr[0] > 0 and board[curr[0] - 1][curr[1]] == "O" and not visited[curr[0] - 1][curr[1]]:
            discover(curr[0] - 1, curr[1], queue, region, visited)
        # check down
        if curr[0] < len(board) - 1 and board[curr[0] + 1][curr[1]] == "O" and not visited[curr[0] + 1][curr[1]]:
            discover(curr[0] + 1, curr[1], queue, region, visited)
        # check right
        if curr[1] < len(board[0]) - 1 and board[curr[0]][curr[1] + 1] == "O" and not visited[curr[0]][curr[1] + 1]:
            discover(curr[0], curr[1] + 1, queue, region, visited)
        # check left
        if curr[1] > 0 and board[curr[0]][curr[1] - 1] == "O" and not visited[curr[0]][curr[1] - 1]:
            discover(curr[0], curr[1] - 1, queue, region, visited)
    
    if is_surrounded:
        # turn o to x within the accumulated region
        for spot in region:
            board[spot[0]][spot[1]] = "X"

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [  [False for col in range(0, len(board[0]))] for row in range(0,len(board))  ]

        for row_index in range(0, len(board)):
            for col_index in range(0, len(board[0])):
                if board[row_index][col_index] == "O" and not visited[row_index][col_index]:
                    find_region_and_capture(board, visited, [row_index, col_index])

