class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        three_sums = []
        nums.sort()
        print(nums)
        for first_num_index in range(0,len(nums) - 2):
            # helps to avoid duplicates
            if first_num_index > 0 and nums[first_num_index - 1] == nums[first_num_index]:
                continue
            # init scnd_num_index to first_num_index + 1
            scnd_num_index = first_num_index + 1
            # init third to the end of the list
            third_num_index = len(nums) - 1
            # close in on the midpoint between these two, finding 3sums along the way
            while scnd_num_index < third_num_index:
                tsum = nums[first_num_index] + nums[scnd_num_index] + nums[third_num_index]
                if tsum < 0 or (scnd_num_index - 1 > first_num_index and nums[scnd_num_index] == nums[scnd_num_index - 1]):
                    scnd_num_index += 1
                elif tsum > 0 or (third_num_index < len(nums) - 1 and nums[third_num_index] == nums[third_num_index + 1]):
                    third_num_index -= 1
                else:
                    # this is a valid 3sum == 0
                    three_sums.append([nums[first_num_index], nums[scnd_num_index], nums[third_num_index]])
                    # increment the left index so the process can continue
                    scnd_num_index += 1
        return three_sums