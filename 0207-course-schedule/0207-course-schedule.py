class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        # -1: being visit, 0: not visited, 1: visited
        visit = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)


        def dfs(now: int):
            if visit[now] == -1:
                return False
            if visit[now] == 1:
                return True

            visit[now] = -1
            for _next in graph[now]:
                if not dfs(_next):
                    return False
            visit[now] = 1
            return True

        # main
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True