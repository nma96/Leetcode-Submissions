class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
             "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        res = set()
        for word in words:
            m = []                          # store the Morse representation of each letter in a word
            for ch in word:
                m.append(codes.get(ch))
            res.add("".join(m))
        return len(res)