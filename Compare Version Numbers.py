class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # makes it into a list of numbers like ['0', '1'] ['1', '1']
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        

        i,j = 0,0
        n,m = len(ver1),len(ver2)
        
        while i < n or j < m:
            # compares both versions' corresponding numbers
            x = int(ver1[i]) if i < n else 0
            y = int(ver2[i]) if j < m else 0
            
            if x < y:
                return -1
            elif x > y:
                return 1
            i += 1
            j += 1
        return 0