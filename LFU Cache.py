from collections import OrderedDict
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.caches={}
        self.cachesfre={}
        self.frekey={} 
        self.minfre=-1 
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.caches:
            return -1
        fre=self.cachesfre[key]
        self.cachesfre[key]+=1
        del self.frekey[fre][key]
        if fre+1 in self.frekey:
            self.frekey[fre+1][key]=-1
        else:
            self.frekey[fre+1]=OrderedDict()
            self.frekey[fre+1][key]=-1
        if fre==self.min and len(self.frekey[fre])==0:
            self.min+=1
        return self.caches[key]
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity==0:
            return 
        if key in self.caches:
            self.caches[key]=value
            self.get(key)
        else:
            if len(self.caches)>=self.capacity:
                minkey=self.frekey[self.min].popitem(last=False)[0]
                del self.caches[minkey]
                del self.cachesfre[minkey]                
            self.min=1
            self.caches[key]=value
            self.cachesfre[key]=self.min
            if self.min in self.frekey:
                self.frekey[self.min][key]=-1 
            else:
                self.frekey[self.min]=OrderedDict()
                self.frekey[self.min][key]=-1