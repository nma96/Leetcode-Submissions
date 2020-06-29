class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # This stores last occurrance of each letter in order. 
        # 0th spot will store last occurance of a, 1st stop will of b and so on
        lastOccurance = {c: i for i, c in enumerate(S)}
        
        #print(lastOccurance)
        
        
        j = anchor = 0
        ans = []
        
        # Main loop
        # anchor is the start, j is the end of current partition
        for i, c in enumerate(S):
            
            # j will be the max lastOccurance of all the charecters in the partition
            # ex: defegde: after d's last occurance, e is occuring which is a part of the partition
            j = max(j, lastOccurance[c])
            
            # if end of the partition is reached, append the length to the result
            if i == j:
                ans.append(j - anchor + 1)
                # Anchor has to be incremented to the next partition start
                anchor = i + 1
            
        return ans
