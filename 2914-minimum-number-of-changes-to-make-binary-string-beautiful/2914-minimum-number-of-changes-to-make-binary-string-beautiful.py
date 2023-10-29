class Solution:
    def minChanges(self, s: str) -> int:
        answer = 0
        
        def two_subarray(sub: str):
            nonlocal answer
            
            # 어차피 0 또는 1로 맞추기 위해 한번 tweak 했음
            # 나중에 11,00 인 결과가 나왔다고 해도 00,00 인 결과를 위해 값을 바꾸는것과 횟수는 차이 없다.
            if len(sub) == 2:
                if sub[0] != sub[1]:
                    answer += 1
                return
            
            # 홀수개의 구간으로 나뉘어지면
            mid = len(sub) // 2
            if  mid % 2 == 1:
                mid -= 1              

            two_subarray(sub[:mid])
            two_subarray(sub[mid:])
            
        two_subarray(s)
        
        return answer
                      
        
        