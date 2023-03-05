lookup_letters_at_num = [
            ["a","b","c"],
            ["d","e","f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"]
        ]

def letters_at_number(char_number):
    return lookup_letters_at_num[int(char_number) - 2]

def recursive_num(digits, curr_string, valid_strings):
    if len(curr_string) == len(digits):
        valid_strings.append(curr_string)
    else:
        possible_next_letters = letters_at_number(digits[len(curr_string)])
        for letter in possible_next_letters:
            recursive_num(digits, curr_string + letter, valid_strings)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        curr_string = ""
        valid_strings = []

        recursive_num(digits, curr_string, valid_strings)

        return valid_strings       