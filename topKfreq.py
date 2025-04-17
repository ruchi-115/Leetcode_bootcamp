class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {} # num -> cnt
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        heap = [(-val, key) for key, val in d.items()]
        largest = heapq.nsmallest(k, heap)
        largest = [key for (val, key) in largest]
        return largest
