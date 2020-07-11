'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
    Input: nums = [1,2,3]
    Output:
    [
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
    ]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums : return []
        res = []
        x = []
        for i in (nums):
            x.append([i])
        while len(x[0]) < len(nums):
            y = []
            for i in range(len(x)):
                res.append(x[i])
                # print(res)
                for j in range(i+1, len(x)):
                    for k in x[j]:
                        if k not in x[i]:
                            z = x[i].copy()
                            z.append(k)
                            z.sort()
                            if z not in y:
                                y.append(z)
            x = y.copy()
            # print(y)
        res.append(x[0])
        res.append([])
        return(res)