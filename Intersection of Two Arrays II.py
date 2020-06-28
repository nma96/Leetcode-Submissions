class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        output = []
        
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                dict1[nums1[i]] +=1
            else:
                dict1[nums1[i]] = 1
        
        for i in range(len(nums2)):
            if nums2[i] in dict1.keys() and dict1[nums2[i]] > 0:
                output.append(nums2[i])
                dict1[nums2[i]] -= 1
            
        return output
        
        