class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return self.solve02(nums)

    def solve00(self, nums: List[int]) -> int:
        '''
        sort 이후 두번째 값 반환
        '''
        if len(nums) < 3:
            return -1

        nums.sort()
        return nums[1]

    def solve01(self, nums: List[int]) -> int:
        '''
        min, max 하나씩 구하고 둘 다 아닌 값이 나오면 바로 리턴 -> O(n) 
        '''
        if len(nums) < 3:
            return -1
            
        mini = min(nums)
        maxi = max(nums)

        for i in nums:
            if i != mini and i != maxi:
                return i
        
        return -1

    def solve02(self, nums: List[int]) -> int:
        '''
        2. 인덱스 0, 1 을 구하고 
        값 3개를 sort 돌려서 min, max 둘 다 아니면 (중간에 낑겨있으면) 중간값이다
        -> time complexity O(1)
        '''    
        if len(nums) < 3:
            return -1

        '''
        a, b, c = nums[0], nums[1], nums[2]
        if a > b:
            if b > c:
                return b
            else:
                return a if a < c else c
        else:
            if b < c:
                return b
            else:
                return a if a > c else c
        '''

        return sorted(nums[:3])[1]