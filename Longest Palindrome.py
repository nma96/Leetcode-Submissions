class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        res = 0
        flag = 0
        
        for i in range (len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1

        for key,value in count.items():
            res += value//2 * 2
            if res%2==0 and value%2==1:
                flag = 1
        
        if flag==1:
            return res+1
        else:
            return res