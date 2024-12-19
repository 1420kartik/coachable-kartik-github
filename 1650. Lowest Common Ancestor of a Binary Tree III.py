# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # We will store all the P ancestors in a set while iterating through it
        p_ancestors = set()
        current_node = p

        while current_node is not None:
            p_ancestors.add(current_node)
            current_node = current_node.parent

        # Then, while iterating through Q ancestors, we will check if we have seen the following ancestor in P ancestors
        current_node = q

        while current_node is not None:
            if current_node in p_ancestors:
                return current_node
            current_node = current_node.parent
