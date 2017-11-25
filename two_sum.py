"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15, 1, 4], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def two_sum(self, nums, target):
        buff_dict = {}
        for i in range(len(nums)):
            print(buff_dict)
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


nums = [2, 7, 11, 15, 1, 4]
target = 3
soln = Solution()
print("Indices: ",soln.two_sum(nums=nums,target=target))
