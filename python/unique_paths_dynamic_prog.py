def count_paths_recursively(m_rows, n_cols, lookup_table, tally, curr_pos):
    if curr_pos == (m_rows - 1, n_cols - 1):
        return 1
    
    if curr_pos[0] < m_rows - 1:
        if lookup_table[curr_pos[0] + 1][curr_pos[1]] > -1:
            tally += lookup_table[ curr_pos[0] + 1 ][ curr_pos[1] ]
        else:
            tally += count_paths_recursively(m_rows, n_cols, lookup_table, 0, (curr_pos[0] + 1, curr_pos[1]))
    
    if curr_pos[1] < n_cols - 1:
        if lookup_table[curr_pos[0]][curr_pos[1] + 1] > -1:
            tally += lookup_table[ curr_pos[0] ][ curr_pos[1] + 1 ]
        else:
            tally += count_paths_recursively(m_rows, n_cols, lookup_table, 0, (curr_pos[0], curr_pos[1] + 1))
    
    lookup_table[ curr_pos[0] ][ curr_pos[1] ] = tally
    
    return tally

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lookup_table = [[-1] * n for col in range(m)]
        return count_paths_recursively(m, n, lookup_table, 0, (0,0))