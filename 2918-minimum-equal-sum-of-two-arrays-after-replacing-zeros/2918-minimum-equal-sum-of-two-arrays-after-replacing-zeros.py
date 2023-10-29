class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, c1 = sum(nums1), nums1.count(0)
        s2, c2 = sum(nums2), nums2.count(0)
        
        # 0을 1로 취급해서 하나의 sum으로 취급한 뒤 대소비교를 진행한다.
        if s1 + c1 > s2 + c2:
            # num2에 0이 하나라도 있어야 sum을 맞춰줄 수 있다.
            if s1 + c1 >= s2 + c2 and c2:
                return s1 + c1
            else:
                return -1
        elif s2 + c2 > s1 + c1:
            # mirror of above code
            if s2 + c2 >= s1 + c1 and c1:
                return s2 + c2
            else:
                return -1
        else:
            # 두 값의 합이 동일하다.
            return s1 + c1
                
            
        
        