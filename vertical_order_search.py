'''
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 

we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
        
    def verticalTraversal(self, root):
        
        self.map = {}
        map2 = {}
        res = []
        
        self.trav(root, 0, 0)
        
        for i in self.map: self.map[i].sort()
            
        d = self.map.keys()
        d.sort(key = lambda x: x[1], reverse = True)
        d.sort(key = lambda x: x[0]) 
        
        for (x, y) in d: 
            if x not in map2:
                map2[x] = []
            map2[x].extend(self.map[x, y])
            
        d = map2.keys()
        d.sort()
        
        for i in d:
            res.append(map2[i])
            
        return res
        
        
    def trav(self, node, x, y):
        if (x, y) in self.map:
            self.map[(x, y)].append(node.val)
        else:
            self.map[(x, y)] = [node.val]
        if node.left: self.trav(node.left, x - 1, y - 1)
        if node.right: self.trav(node.right, x + 1, y - 1) 