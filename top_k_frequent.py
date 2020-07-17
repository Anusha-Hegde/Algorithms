'''
Given a non-empty array of integers, return the k most frequent elements.

Example:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        dics = {}
        res = []
        q = PriorityQueue()

        for i in nums:
            if i in dics: dics[i] += 1
            else: dics[i] = 1
        for i in dics:
            q.put([-dics[i],i])
        while k:
            res.append(q.get()[-1])
            k -= 1
        return(res)
        
        

#Solution using counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        counter = collections.Counter(nums)
        
        return heapq.nlargest(k, counter.keys(), key = counter.get)