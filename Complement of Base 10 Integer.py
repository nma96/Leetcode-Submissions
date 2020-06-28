class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binRep = bin(N)[2:]
        comp = ''
        for i in range(len(binRep)):
            
            if binRep[i] == '1':
                comp += '0'
            else:
                comp += '1'
        
        return int(comp,2)