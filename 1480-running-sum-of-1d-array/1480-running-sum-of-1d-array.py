class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list1 = []
        sum = 0
        
        for i in nums:
            sum += i
            list1.append(sum)
            
        return list1
            