class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [0 for _ in range(n)]

        for k in range(n):
            length[k] = 1
            for i in range(k):
                if nums[i] < nums[k]:
                    length[k] = max(length[k], length[i] + 1)
                
        return max(length) + 1
    
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        total_number = len(nums)
        dp = [0 for _ in range(total_number)]
        for i in range(1, total_number):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1