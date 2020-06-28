class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=HKHkzKvb0J4&t=600s
        people  = sorted(people, key = lambda x: (-x[0], x[1]))
        
        result = []
        for p in people:
            result.insert(p[1], p)
        
        return result