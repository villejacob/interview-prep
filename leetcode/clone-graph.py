'''
Clone an undirected graph. Each node in the graph contains a label and a list of
its neighbors.

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and 
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as 
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming
a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

'''
from collections import deque

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """

        if not node: return node
        clones = {}
        q = deque([node])
        while q:
            n = q.pop()
            if n.label not in clones: 
                clones[n.label] = UndirectedGraphNode(n.label)
            for neighbor in n.neighbors:
                if neighbor.label not in clones:
                    clones[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    q.append(neighbor)
                clones[n.label].neighbors.append(clones[neighbor.label])
                
        #for c in clones:
        #    for nbr in clones[c].neighbors:
        #        print c, ":", nbr.label
        #    print
        return clones[node.label]


node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(3)
node4 = UndirectedGraphNode(4)
node5 = UndirectedGraphNode(5)
node6 = UndirectedGraphNode(6)
node1.neighbors = [node3, node4]
node2.neighbors = [node4]
node3.neighbors = [node1, node3, node4, node5, node6]
node4.neighbors = [node1, node2, node3]
node5.neighbors = [node3, node4, node6]
node6.neighbors = [node3, node5]
clone = Solution().cloneGraph(node2)
