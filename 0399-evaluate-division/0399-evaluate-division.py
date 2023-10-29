from collections import defaultdict

class Solution:
    '''
    연산 결과를 통해 equations에 사용된 a, b, c, .. 의 값을 찾아내야 한다.
    example1의 경우를 보면 a / b == 2.0, b / c == 3.0 이다.
    이를 통해 a / c == 6.0임을 추측할 수 있고
    b / a == 0.5, c / b = 0.3333... 임을 알 수 있다.
    e의 값은 알 수 없으므로 -1로 출력한다.
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)  # dict( left : dict( right : value ) )
        answer = []
        result: float = -1

        # a, b, c: find b that make calc (a, c) happen
        def try_evaluate(now: str, target: str, temp: float, visited: List[str]):
            nonlocal result

            if now == target:
                result = temp
                print('result: ', result, ', temp: ', temp)
                return

            # 다음 탐색할 노드가 전부 visited에 있으면 return
            for _next, value in d[now]:
                if _next not in visited:
                    break
            else:
                return

            # 방문하지 않는 노드에 대해 dfs 수행
            for _next, value in d[now]:
                if _next not in visited:
                    try_evaluate(_next, target, temp * value, visited + [_next])


        # put in dictionary that I can get answer of equation
        for idx, (i, j) in enumerate(equations):
            d[i].append([j, values[idx]])
            d[j].append([i, 1 / values[idx]])

        # answer will store in result
        for left, right in queries:
            if left not in d or right not in d:
                answer.append(float(-1))
                continue

            result = -1
            try_evaluate(left, right, 1, [left])
            answer.append(result)

        return answer
