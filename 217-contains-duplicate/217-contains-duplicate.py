class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # dict1 = {}
        # count = 0
        # for x in nums: 
        #     if x in dict1:
        #         dict1[x] = dict1[x] + 1
        #     else: 
        #         dict[x] == 1
        # if dict[x].value >= 2:
        #     return True
        # return False
        
#         nums.sort()
        
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False

        return len(nums) != len(set(nums))
        
        