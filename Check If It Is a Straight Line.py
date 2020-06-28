class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
        
        slope = self.slope(coordinates[0],coordinates[-1])
        for i in range(1,len(coordinates)-1):
            if self.slope(coordinates[i], coordinates[i+1]) != slope:
                return False
        return True
    
    def slope(self, p1, p2):
        return (p2[1]-p1[1])/(p2[0]-p1[0]) if (p2[0]-p1[0]) else 1