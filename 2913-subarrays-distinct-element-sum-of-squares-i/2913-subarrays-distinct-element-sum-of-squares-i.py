class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for _len in range(1, len(nums) + 1):
            for left in range(len(nums) - _len + 1):
                res += len(Counter(nums[left: left + _len])) ** 2
        
        return res
                
        
        