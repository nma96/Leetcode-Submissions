class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_temp = []
        t_temp = []
        
        for i in range(len(S)):
            if S[i] != '#':
                s_temp.append(S[i])
            elif S[i] == '#' and len(s_temp) != 0:
                s_temp.pop()
        
        for i in range(len(T)):
            if T[i] != '#':
                t_temp.append(T[i])
            elif T[i] == '#' and len(t_temp) != 0:
                t_temp.pop()
        
        return s_temp==t_temp