def recursively_gen_paren(target_pairs, curr_string, curr_num_open_paren, curr_num_closed_paren, valid_paren):
    # cant do open parentheses last
    if len(curr_string) == (target_pairs * 2) - 1:
        curr_string += ")"
        curr_num_closed_paren += 1
        if curr_num_closed_paren == curr_num_open_paren:
            valid_paren.append(curr_string)
        return
    else:
        if curr_num_open_paren < target_pairs:
            # call adding another open parentheses
            recursively_gen_paren(target_pairs, curr_string + "(", curr_num_open_paren + 1, curr_num_closed_paren, valid_paren)
        if curr_num_closed_paren < curr_num_open_paren:
            # call adding another closed parentheses
            recursively_gen_paren(target_pairs, curr_string + ")", curr_num_open_paren, curr_num_closed_paren + 1, valid_paren)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return []

        valid_paren = []

        recursively_gen_paren(n, "(", 1, 0, valid_paren)

        return valid_paren
        