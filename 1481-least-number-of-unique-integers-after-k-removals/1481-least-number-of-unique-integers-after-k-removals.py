class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequencies = sorted(Counter(arr).items(), key=lambda x: x[1])
        kinds = len(frequencies)
        
        for _, freq in frequencies:
            k -= freq
            if k >= 0:
                kinds -= 1
            else:
                return kinds
        
        return kinds
        