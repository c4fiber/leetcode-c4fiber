class Solution:
    def countCollisions(self, directions: str) -> int:
        '''
        set up walls at left and right (index를 가운데로 모아주고)
        count which car is not stop (not 'S')
        Time Complexity: O(n)
        '''
        n = len(directions)
        left, right = 0, n - 1

        # 왼쪽에 벽을 세운다.
        while left < n and directions[left] == 'L':
            left += 1

        # 오른쪽에 벽을 세운다.
        while 0 <= right and directions[right] == 'R':
            right -= 1

        collisions = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1

        return collisions;
