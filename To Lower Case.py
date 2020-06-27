class Solution:
    def toLowerCase(self, str: str) -> str:
        # return str.lower() Trivial
        
        # Below is ascii
        result = []
        for char in str:
            ascii_num = ord(char)
            if 65 <= ascii_num <= 90:
                ascii_num += 32
            result.append(chr(ascii_num))
        return "".join(result)