class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 0:
            # print(stones)
            stones = sorted(stones)
            
            if len(stones) == 0: return 0
            if len(stones) == 1: return stones[0]
            if len(stones) == 2: return stones[1] - stones[0]
            
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            elif stones[-1] > stones[-2]:
                stones[-2] = stones[-1] - stones[-2]
                stones = stones[:-1]
            