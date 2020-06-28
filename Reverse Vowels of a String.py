class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        temp = []
        new = ''
        
        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(s[i])
        print(temp)
        
        for i in range(len(s)):
            if s[i] not in vowels:
                new += s[i]
            elif s[i] in vowels:
                new += temp.pop()
                
        return new