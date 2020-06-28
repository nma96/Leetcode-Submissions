class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = OrderedDict()
        
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        for key,value in count.items():
            if value == 1:
                return s.index(key)
        return -1