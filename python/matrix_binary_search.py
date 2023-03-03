# helper function for thinking of the matrix as one long array
def linear_index_to_matrix_index(array_index, columns) -> (int, int):
    row_index = array_index // columns
    column_index = array_index % columns
    return (row_index, column_index)

# do normal binary search, but use the linear_index_to_matrix_index() helper function when comparing values
def matrix_binary_search(matrix: List[List[int]], linear_index_start, linear_index_end, target: int):
    while linear_index_start <= linear_index_end:
        linear_midpt_index = (linear_index_end - linear_index_start // 2) + linear_index_start
        mtx_midpt = linear_index_to_matrix_index(linear_midpt_index, len(matrix[0]))
        print(mtx_midpt)
        midpt_value = matrix[mtx_midpt[0]][mtx_midpt[1]]
        if midpt_value < target:
            # search upper half of linear representation
            linear_index_start = linear_midpt_index + 1
        elif midpt_value > target:
            # search lower half of linear representation
            linear_index_end = linear_midpt_index - 1
        else:
            return True
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(matrix)
        return matrix_binary_search(matrix, 0, len(matrix) * len(matrix[0]) - 1, target)
        