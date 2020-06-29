class Solution:
    def checkValidString(self, s: str) -> bool:
        OpenBracketStack = []
        StarStack = []
        
        # https://www.youtube.com/watch?v=KuE_Cn3xhxI
        # Balancing all the closed brackets
        for i in range(len(s)):
            if s[i] =='(':
                OpenBracketStack.append(i)
            elif s[i] == '*':
                StarStack.append(i)
            elif s[i] == ')':
                if OpenBracketStack != []:
                    OpenBracketStack.pop()
                elif OpenBracketStack == [] and StarStack != []:
                    StarStack.pop()
                elif OpenBracketStack == [] and StarStack == []:
                    return False
        # print(OpenBracketStack, StarStack)
            
        # Balancing all the open brackets
        # Check if the index of the open bracket is less than star
        # Meaning open bracket occurs before the star
        while OpenBracketStack != []:
            if StarStack == []:
                return False
            elif OpenBracketStack[-1] < StarStack[-1]:
                StarStack.pop()
                OpenBracketStack.pop()
            else:
                return False
        return True
                    
        
# Cleaner Code
        # stack = []
        # star_stack = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     elif s[i] == '*':
        #         star_stack.append(i)
        #     else:
        #         if not stack and not star_stack:
        #             return False
        #         if stack:
        #             stack.pop()
        #         else:
        #             star_stack.pop()
        # while stack and star_stack:
        #     if stack.pop()>star_stack.pop():
        #         return False
        # return not stack