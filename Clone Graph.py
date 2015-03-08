# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        ''' Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''
        if node is None:
            return None
        dict = {}
        queue = []
        preq = []
        queue.append(node)
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.label in preq:
                continue
            preq.append(cur.label)
            if cur.label not in dict:
                dict[cur.label] = UndirectedGraphNode(cur.label)
            copyNode = dict[cur.label]
            for tn in cur.neighbors:
                if tn.label not in dict:
                    dict[tn.label] = UndirectedGraphNode(tn.label)
                copyNode.neighbors.append(dict[tn.label])
                if tn.label not in preq:
                    queue.append(tn)
        return dict[node.label]

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
        res = str(self.label) + ":"
        for n in self.neighbors:
            res += " " + str(n.label)
        res += "# "
        for n in self.neighbors:
            if self.label != n.label:
                res += str(n)
        return res

N2 = UndirectedGraphNode(2)
N2.neighbors = [N2]
N1 = UndirectedGraphNode(1)
N1.neighbors = [N2]
N0 = UndirectedGraphNode(0)
N0.neighbors = [N1, N2]
so = Solution()
#print(N0)
print(so.cloneGraph(N0))