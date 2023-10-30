class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # use dictionary as dynamic programming table, to store the score gap
        dp_table = {}
        
        def optimal_pick(left: int, right: int) -> int:
            nonlocal nums, dp_table
            
            if left == right:
                # Only one choice remains
                return nums[left]
            
            if (left, right) in dp_table:
                # If this query has been computed before
                # directly return by dp table
                return dp_table[ (left, right) ]
            
            # Maximize and compute the score gap by recurrence relationship
			# 
			# for player 1:
			# benefit of pick left = score of left - optimal pick of player 2 in ( left+1, right )
			# benefit of pick right = score of right - optimal pick of player 2 in ( left, right-1 )
            choose_left = nums[left] - optimal_pick(left+1, right)
            choose_right = nums[right] - optimal_pick(left, right-1)
            
            dp_table[(left, right)] = max(choose_left, choose_right)
            return dp_table[(left, right)] 
        
        # ------------------------------------------------------
        
        # score gap = score of player 1 - score of player 2
        # Player 1 is winner if score gap >= 0
        return optimal_pick(left=0, right=len(nums)-1 ) >= 0