class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        nums=0
        for i in range(len(s)-1):
            if romans[s[i]]>=romans[s[i+1]]:
                nums+=romans[s[i]]
            else:
                nums-=romans[s[i]]
        return(nums+romans[s[-1]])