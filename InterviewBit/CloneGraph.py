'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, start_node):

        import collections

        # Dictionary of node: clone pairs
        clones = {}

        # Initilize starting node of clone graph
        start_clone = UndirectedGraphNode(start_node.label)

        # Create the first node: clone pair in the dictionary
        clones[start_node] = start_clone

        # Deque (used as queue) to allow bfs of graph
        nodes = collections.deque()
        nodes.append(start_node)

        # While there are still values in the queue
        while nodes:
            # Take the first node
            node = nodes.popleft()
            # Iterate through all of this node's neighbors
            for neighbor in node.neighbors:
                # If the neighbor has not yet been cloned
                if neighbor not in clones:
                    # Create the clone of the node and assign to dictionary
                    clones[neighbor] = UndirectedGraphNode(neighbor.label)
                    # Then add this node to the queue to find its neighbors
                    nodes.append(neighbor)
                # Whether or not the node has been cloned, assign all neighbors to the clone of the original node
                clones[node].neighbors.append(clones[neighbor])
        # Return the first clone created
        return start_clone

    # Method to print out the node and its neighbors via dfs
    def print_graph(self, node):

        visited = {}

        def dfs(node):
            if node.label in visited:
                return
            visited[node.label] = node
            print node.label, ":",
            for n in node.neighbors:
                print n.label,
            print
            for neighbor in node.neighbors:
                dfs(neighbor)
        dfs(node)

node_a = UndirectedGraphNode("a")
node_b = UndirectedGraphNode("b")
node_c = UndirectedGraphNode("c")
node_d = UndirectedGraphNode("d")
node_e = UndirectedGraphNode("e")
node_f = UndirectedGraphNode("f")
node_a.neighbors = [node_b, node_d, node_e]
node_b.neighbors = [node_a, node_c, node_d, node_f]
node_c.neighbors = [node_b, node_e]
node_d.neighbors = [node_a, node_b]
node_e.neighbors = [node_a, node_c, node_f]
node_f.neighbors = [node_b, node_e]

soln = Solution()
clone = soln.cloneGraph(node_a)
soln.print_graph(clone)
