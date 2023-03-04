def create_char_freq_map(a_string):
    # create freq map of the string
    freq_map = {}
    for char in a_string:
        if char in freq_map.keys():
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    return freq_map

# kind of slow, if there is a way to avoid this, try
def is_anagram(string1, p_freq_map):
    # create freq map of the string
    freq_map = {}
    # iterating backwards allows us to find the biggest jumps forward when a character is not in the p_freq_map
    for char_index in range(len(string1) - 1, -1, -1):
        # if this character does not exist in the p_freq_map, return false and provide an index to skip ahead to
        if string1[char_index] not in p_freq_map.keys():
            return (False, char_index)
        if string1[char_index] in freq_map.keys():
            freq_map[string1[char_index]] += 1
        else:
            freq_map[string1[char_index]] = 1
        # if the character appears too many times in this string to be an anagram, leave early
        if freq_map[string1[char_index]] > p_freq_map[string1[char_index]]:
            return (False, None)
    return (True, None)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_window = 0
        end_window = start_window + len(p)
        result = []
        p_char_freq = create_char_freq_map(p)

        last_window_was_anagram = False

        while end_window <= len(s):
            # if newly introduced letter is not in the substring
            if s[end_window - 1] not in p_char_freq.keys():
                last_window_was_anagram = False
                start_window = end_window
                end_window = start_window + len(p)
                continue # window has been adjusted according to speedup, skip incrementing
            elif last_window_was_anagram and s[start_window - 1] == s[end_window - 1]:
                result.append(start_window)
            else:
                anagram_comp_result = is_anagram(s[start_window:end_window], p_char_freq)
                if anagram_comp_result[0]:
                    last_window_was_anagram = True
                    result.append(start_window)
                elif anagram_comp_result[1] != None:
                    #char that is nort in p was seen in the current substring
                    last_window_was_anagram = False
                    # move the window forward according to the char in the substring that could not be found in p
                    start_window += anagram_comp_result[1] + 1
                    end_window = start_window + len(p)
                    continue # window has been adjusted according to speedup, skip incrementing
                else:
                    # anagram comp failed, because the frequency of the characters was different
                    last_window_was_anagram = False
            start_window += 1
            end_window = start_window + len(p)
        
        return result

