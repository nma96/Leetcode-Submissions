class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        number = k
        
        for digit in num:
            while number and stack and stack[-1] > digit:
                stack.pop()
                number -= 1
            stack.append(digit)
        answer = "".join(stack[:len(stack)-number]).lstrip("0")
        if len(answer):
            return answer
        else:
            return "0"