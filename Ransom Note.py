class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        possibleLetters = {}
        
        for i in range(len(magazine)): 
            if magazine[i] in possibleLetters: 
                possibleLetters[magazine[i]] += 1
            else: 
                possibleLetters[magazine[i]] = 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in possibleLetters.keys(): 
                return False
            else: 
                possibleLetters[ransomNote[i]] -= 1
                
            if possibleLetters[ransomNote[i]] == 0: 
                del possibleLetters[ransomNote[i]]
        
        return True