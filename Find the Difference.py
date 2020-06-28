class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # MY Solution
        dictionary = {}
        
        for i in range(len(t)):
            if t[i] in dictionary:
                dictionary[t[i]] +=1
            else:
                dictionary[t[i]] = 1
        
        for i in range(len(s)):
            if dictionary[s[i]] > 0:
                dictionary[s[i]] -= 1
        
        for key,value in dictionary.items():
            if value == 1:
                return key

    # Optimised solution
        # dic_s = collections.Counter(s)
        # dic_t = collections.Counter(t)
        # for key, val in dic_t.items():
        #     if key not in dic_s or val > dic_s[key]:
        #         return key
            
            