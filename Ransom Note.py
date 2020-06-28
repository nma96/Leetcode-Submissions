class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}

        for i in range(len(magazine)):
            if magazine[i] not in mag:
                mag[magazine[i]] = 1
            else:
                mag[magazine[i]] += 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in mag:
                mag[ransomNote[i]] -= 1
                if mag[ransomNote[i]] <= 0:
                    del mag[ransomNote[i]]
            else:
                return False
        
        return True