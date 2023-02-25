import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        if len(deck) < 2:
            return False

        freq_dict = {}

        for card in deck:
            if card not in freq_dict.keys():
                freq_dict[card] = 1
            else:
                freq_dict[card] = freq_dict[card] + 1
        
        # set the gcd to the first element
        frequencies = list(freq_dict.values())
        curr_gcd = frequencies[0]

        for freq in frequencies:
            curr_gcd = math.gcd(curr_gcd, freq)
            if curr_gcd < 2:
                return False

        return True