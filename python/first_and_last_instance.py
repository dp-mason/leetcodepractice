# write binary search to find an instance of the number
# do two passes of binary search to find the two instances of the number that
# one:
#   is the first position in the array
#        OR
#   has an element to its left it is not equal to
# two:
#   is in the last position of the array
#       OR
#   has an element to its right that is not equal to it

def is_first_and_or_last_instance(nums: List[int], target_index):
        # ASSUMES VALUE AT THIS INDEX IS THE ONE YOU ARE LOOKING FOR IN THE LIST
        # record whether this is the first instance by checking left neighbor if one exists
        result = [False, None]
        if target_index == 0 or nums[target_index - 1] != nums[target_index]:
            result[0] = True
            result[1] = "First"
        # record whether this is the last instance by checking right neighbor if one exists
        if target_index == len(nums) - 1 or nums[target_index + 1] != nums[target_index]:
            result[0] = True
            if result[1] == None:
                result[1] = "Last"
            else:
                result[1] = "Both"
        # return a tuple that describes the result
        return result

#def binary_search_left_bookend(nums: List[int], start, end, target):

def binary_search_bookends(nums: List[int], start, end, target, first_last_both):
        bookends = [-1, -1]
        if first_last_both == "First":
            bookends[1] = -2 # marks it as found so the last bookend is ignored
        elif first_last_both == "Last":
            bookends[0] = -2 # marks it as found so that the first bookend is ignored
        
        while start <= end and (bookends[0] == -1 or bookends[1] == -1):
            midpt = (start + end) // 2
            if nums[midpt] == target:
                # check to see wither it is the first or last instance
                res = is_first_and_or_last_instance(nums, midpt)
                if res[0] == True:
                    if res[1] == "Both":
                        return [midpt, midpt]
                    elif res[1] == "First":
                        bookends[0] = midpt
                        # search the upper half of array to find last index
                        start = midpt + 1
                    elif res[1] == "Last":
                        bookends[1] = midpt
                        # search the lower half for the first instance
                        end = midpt - 1
                else:
                    bookends[0] = binary_search_bookends(nums, start, midpt - 1, target, "First")[0]
                    bookends[1] = binary_search_bookends(nums, midpt+1, end, target, "Last")[1]
            elif nums[midpt] < target:
                start = midpt + 1
            else:
                end = midpt - 1
        return bookends

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return binary_search_bookends(nums, 0, len(nums) - 1, target, "Both")
