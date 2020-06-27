class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= collections.Counter(nums)
        return [key for (key,value) in count.most_common(k)]
        #return heapq.nlargest(k, count.keys(), key=count.get)