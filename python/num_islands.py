def explore_island(grid, visited, queue):
    while len(queue) > 0:
        # take first elem off the queue
        curr = queue.pop()
        # visit right left and down
        # add them to the queue if they are land and have not been visited before
        
        # visit left
        if curr[1] > 0 and grid[curr[0]][curr[1] - 1] == "1" and (not visited[curr[0]][curr[1] - 1]):
            queue.append([curr[0], curr[1] - 1])
            visited[curr[0]][curr[1] - 1] = True
        # visit right
        if curr[1] < len(grid[0]) - 1 and grid[curr[0]][curr[1] + 1] == "1" and (not visited[curr[0]][curr[1] + 1]):
            queue.append([curr[0], curr[1] + 1])
            visited[curr[0]][curr[1] + 1] = True
        # visit down
        if curr[0] < len(grid) - 1 and grid[curr[0] + 1][curr[1]] == "1" and (not visited[curr[0] + 1][curr[1]]):
            queue.append([curr[0] + 1, curr[1]])
            visited[curr[0] + 1][curr[1]] = True
        # visit up
        if curr[0] > 0 and grid[curr[0] - 1][curr[1]] == "1" and (not visited[curr[0] - 1][curr[1]]):
            queue.append([curr[0] - 1, curr[1]])
            visited[curr[0] - 1][curr[1]] = True
    return
        


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for col in range(len(grid[0]))] for row in range(len(grid))]
        num_islands = 0

        for row_index in range(0, len(grid)):
            for col_index in range(0, len(grid[0])):
                if grid[row_index][col_index] == "1" and not visited[row_index][col_index]:
                    num_islands += 1
                    visited[row_index][col_index] = True
                    queue = [[row_index, col_index]]
                    explore_island(grid, visited, queue)
        
        return num_islands