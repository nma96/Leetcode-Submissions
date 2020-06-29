class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = []
        
        for i in range(len(A)):
            if A[i]%2==0:
                res.insert(0,A[i])
            else:
                res.append(A[i])
        return res
            
        