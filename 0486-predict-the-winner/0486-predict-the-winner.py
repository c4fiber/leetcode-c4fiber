class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:] # idx를 뽑았을 때 생기는 이득 or 손해를 기록

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # i를 뽑았을 때와 j를 뽑았을 때를 비교
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0