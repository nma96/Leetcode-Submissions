class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = {}
        incoming = {}
        
        for i in range(len(paths)):
            outgoing[paths[i][0]] = 1
            incoming[paths[i][1]] = 1
        
        for key in incoming.keys():
            if key not in outgoing:
                return key