class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_cities = sorted(costs, key = lambda x:x[0]-x[1])
        total = 0
        for i in range(len(costs)):
            if i<len(costs)/2:
                total += sorted_cities[i][0]
            else:
                total += sorted_cities[i][1]
                
        return total