class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        DP 방식으로 풀이
        k를 0 ~ N-1 까지 증가시키면서 k길이의 리스트의 LIS를 구한다.
        '''
        n = len(nums)
        length = [0 for _ in range(n)]

        for k in range(n):
            length[k] = 1
            for i in range(k):
                if nums[i] < nums[k]:
                    length[k] = max(length[k], length[i] + 1)
                
        return max(length)

    
        # Suppose, for example:
        #           nums = [1,8,4,5,3,7],
        # for which the longest strictly increasing subsequence is arr = [1,4,5,7],
        # giving len(arr) = 4 as the answer
        #
        # Here's the plan:
        #   1) Initiate arr = [num[0]], which in this example means arr = [1]
        #     
        #   2) Iterate through nums. 
        #     2a) If n in nums is greater than arr[-1], append n to arr. 
        #     2b) If not, determine the furthest position in arr at which n could be placed so that arr
        #         remains strictly increasing, and overwrite the element at that position in arr with n.

        #   3) Once completed, return the length of arr.

        # Here's the iteration for the example:

        #       nums = [ _1_, 8,4,5,3,7]     arr = [1]              (initial step)
        #       nums = [1, _8_, 4,5,3,7]     arr = [1, 8]           (8 > 1, so    append 8)
        #       nums = [1,8, _4_, 5,3,7]     arr = [1, 4]           (4 < 8, so overwrite 8)
        #       nums = [1_8,4, _5_, 3,7]     arr = [1, 4, 5]        (5 > 4, so    append 5)
        #       nums = [1_8,4,5, _3_, 7]     arr = [1, 3, 5]        (3 < 5, so overwrite 4)
        #       nums = [1_8,4,5,3, _7_ ]     arr = [1, 3, 5, 7]     (7 > 5, so    append 7)    

        # Notice that arr is not the sequence given above as the correct seq. The ordering for [1,3,5,7]
        # breaks the "no changing the order" rule. Cheating? Maybe... However len(arr) = 4 is the 
        # correct answer. Overwriting 4 with 3 did not alter the sequence's length.

    def solve02(self, nums: list[int]) -> int:
        '''
        이진탐색을 이용한 LIS 구하기
        배열은 항상 오름차순으로 정렬되어 있으며
        마지막 값보다 크면 -> 뒤에 붙이기
        아니면 적절한 위치를 찾아 '덮어씌운다'
        '''
        arr = [nums.pop(0)]                  # <-- 1) initial step
 
        for n in nums:                       # <-- 2) iterate through nums
            
            if n > arr[-1]:                  # <--    2a)
                arr.append(n)

            else:                            # <--    2b)
                arr[bisect_left(arr, n)] = n 

        return len(arr)                      # <-- 3) return the length of arr