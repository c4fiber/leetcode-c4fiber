class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        
        for i in range(32):
            temp = 0
            for n in nums:
                if 1 << i & n:
                    temp += 1
            if temp >= k:
                res += 1 << i
                
        return res
                    
