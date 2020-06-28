class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prevMax = arr[-1]
        arr[-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            currentElement = arr[i]
            arr[i] = prevMax
            prevMax = max(currentElement, prevMax)
        
        return arr