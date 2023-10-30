class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        사실상 피보나치 수열과 동일함
        '''
        max_value = 45
        dp = [0 for _ in range(max_value + 1)]
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        # dp[3] = 3
        # dp[4] = 5
        
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        
        return dp[n]