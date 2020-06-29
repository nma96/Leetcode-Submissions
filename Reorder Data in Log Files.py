class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        
        # Split logs into digits list and letters list
        for log in logs:
            tokens = log.split()
            if tokens[1].isdigit(): 
                digits.append(log)
            else: 
                # Append split up letter logs for further processing
                letters.append(tokens)
        
        # print(letters, digits)
        
        letters.sort(key = lambda log: log[0]) # Sort by identifier first
        print(letters)
        letters.sort(key = lambda log: log[1:]) # Sort ignoring identifier
        print(letters)
        for i, log in enumerate(letters):
            letters[i] = ' '.join(log)
        
        return letters + digits