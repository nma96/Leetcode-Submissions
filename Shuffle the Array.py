class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j = n
        
        result = []
        
        for i in range(n):
            result.append(nums[i])
            result.append(nums[j])
            j+=1
            
        return result