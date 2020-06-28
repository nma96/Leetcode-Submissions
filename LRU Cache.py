from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
        return self.cache.get(key, -1)

    def put(self, key, value):
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False)
            

    # Without using libraries
#     def __init__(self, capacity: int):
#         self.dic1={}
#         self.c=0
#         self.lru=[]
#         self.capacity=capacity

#     def get(self, key: int) -> int:
#         if key in self.dic1:
#             self.lru.remove(key)
#             self.lru.append(key)
#             return self.dic1[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.dic1:
#             self.dic1[key]=value
#             self.lru.remove(key)
#             self.lru.append(key)
#         else:
#             if self.c>=self.capacity:
#                 if self.lru[0] in self.dic1:
#                     del self.dic1[self.lru[0]]
#                     self.lru.pop(0)
#                     self.c-=1
#                 else:
#                     return "Runtime Error"


#             self.dic1[key]=value
#             self.c+=1
#             self.lru=self.lru+[key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

