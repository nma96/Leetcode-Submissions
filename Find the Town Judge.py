class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        count = defaultdict(int)
        for t in trust:
            count[t[1]] += 1
            count[t[0]] -= 1
            
        for k, v in count.items():
            if v == N - 1:
                return k
        return -1