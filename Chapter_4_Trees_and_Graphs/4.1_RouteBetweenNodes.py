# Assuming input graph is represented by adjacency list

g1 = {"a": ["b"],
      "b": ["c", "d"],
      "c": [],
      "d": ["c"],
      "e": ["c"]
    }

g2 = {"a": ["b"],
      "b": ["c", "d"],
      "c": ["e"],
      "d": ["c"],
      "e": ["c"]
    }

#print(g1)

def isPath(n1, n2, g):
    queue = []
    seen = {}
    queue.insert(0, n1)
    seen[n1] = 1

    while len(queue) > 0:
        n = queue.pop(0)
        for nbr in g[n]:
            if nbr == n2:
                return True
            if nbr not in seen:
                seen[nbr] = 1
                queue.insert(0, nbr)
    return False

print(isPath("a", "e", g2))

"""
Can just do BFS and check if each new node is the one we want to find

Time: O(V + E) where V is the number of nodes and E is the number of edges
    - this is because we go through all the nodes and explore all the edges
    out of them so we touch each node and edge once

Space: Adjacency Matrix O(V + E) storing all the nodes and edges in the 
    representation
"""