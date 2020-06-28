class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or nums is None:
            return []
        
        x= []
        for i in range(len(nums)):
            if i%2 == 0:             
                freq = nums[i]
                val = nums[i+1]
                for y in range(freq):         
                    x.append(val)
        return x