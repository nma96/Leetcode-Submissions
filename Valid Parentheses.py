class Solution:
    def isValid(self, s: str) -> bool:
        # If length is 0
        if len(s)==0:
            return True
        # If length is odd
        if len(s)%2!=0:
            return False
        
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i=='[':
                stack.append(i)
            elif i == ')' and len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            elif i == '}' and len(stack)!=0 and stack[-1]=='{':
                stack.pop()
            elif i == ']' and len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                return False
        return len(stack) == 0
            
