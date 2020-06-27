class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        elif name[0] != typed[0]:
            return False
        else:
            length_n = len(name)
            length_t = len(typed)

            i = 0 
            j = 0
            count = 0

            while j < length_t:    
                if name[i] == typed[j]:
                    if i < length_n - 1:
                        i += 1
                        j += 1
                        count += 1
                    else:
                        j += 1
                        count += 1
               
                elif name[i] != typed[j] and typed[j] != typed[j - 1]:
                    return False
                else:
                    j += 1
#       it doesn't matter if count > length n (for case alex vs alexx)
        if count >= length_n:
            return True
        else:
            return False