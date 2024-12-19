# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We will initiate the default dictionary to maintain the node values on each column
        column_values = defaultdict(list)

        # We will use queue DS to iterate over binary tree in BFS, so we can keep track of nodes row-wise
        queue = deque([(root, 0)])

        while queue:
            # Current stoes the current visited node value and level stores the value of column number based on root
            current, level = queue.popleft()

            if current:
                # We will store the current node value in column_values dictionary based on its level
                column_values[level].append(current.val)

                # We will append the values in queue and update the level accordingly
                queue.append((current.left, level - 1))
                queue.append((current.right, level + 1))

        # Ultimately, we sort the values of the dictionary based on it's keys                
        result = [ column_values[x] for x in sorted(column_values.keys()) ]
        
        return result
