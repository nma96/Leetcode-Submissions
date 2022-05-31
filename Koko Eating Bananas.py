class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r #Max bananas that can possibly be eaten to finish the piles
        
        # Basic approach: Binary Search
        # Possible values of k will be between 1 and max(piles)
        while l <= r: 
            k = (r+l)//2 # Find mid value
            hours = 0 # Initialize a temp hours variable to count how long it take for koko to eat the piles
            
            #Iterating through piles to calculate time
            for i in range(len(piles)): 
                hours+=math.ceil(piles[i]/k)
            
            # If koko could eat with more time remaining, then koko can potentially decrease k (so koko can utilize time better) 
            # Look in the left subarray of mid (k)
            if hours <= h: 
                result = min(result, k)
                r = k - 1
            # if koko could not finish in given time, then the k value was too low so increase k (so koko can eat more bananas to finish them all)
            # Look in the 3 subarray of mid (k)
            else: 
                l = k + 1
                
        return result
            