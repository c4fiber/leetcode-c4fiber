from itertools import permutations

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def can_make_m_bouquets(days: int):
            nonlocal bloomDay, m, k

            bouquets = 0
            cnt = 0

            for flower in bloomDay:
                # 연속되면 카운트 아니면 0으로 초기화
                if flower <= days:
                    cnt += 1
                else:
                    cnt = 0
                
                if cnt >= k:
                    bouquets += 1
                    cnt -= k
            
            return bouquets >= m

        # 부케 제작에 필요한 꽃의 개수가 충분한가?
        if m * k > len(bloomDay):
            return -1

        # 소요된 날짜를 기준으로 binary search 수행
        lo, hi = -1, max(bloomDay) + 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2

            if can_make_m_bouquets(mid):
                hi = mid
            else:
                lo = mid
        
        # 모든 경우에서 제작 실패하면 lo == max(bloomDay)가 된다.
        return -1 if lo == max(bloomDay) else hi

            
            
            
                    
        