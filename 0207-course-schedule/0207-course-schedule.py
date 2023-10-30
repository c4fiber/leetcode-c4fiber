class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        # -1: being visit, 0: not visited, 1: visited
        visit = [0 for _ in range(numCourses)]

        # set up vector(directed vertex)
        for x, y in prerequisites:
            graph[x].append(y)

        
        def dfs(now: int):
            '''
            now를 시작으로 연쇄적으로 필요한 코스를 탐색한다.
            확인이 끝난 코스(1)은 pass
            현재 확인중인 코스 중 하나(-1)이면 사이클이 존재한다.
            '''
            nonlocal visit, graph
            
            if visit[now] == -1:
                return False
            if visit[now] == 1:
                return True

            visit[now] = -1
            for _next in graph[now]:
                if not dfs(_next):
                    return False
                
            # now 코스를 듣기 위한 코스들을 연쇄적으로 모두 확인했다.
            visit[now] = 1
            return True

        
        # main
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True