# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where N is the number of nodes & E is the number of edges
        Space Complexity: O(N) where N is the number of nodes
    """

    if len(dislikes) == 0:
        return True
    
    groups = {}
    for key in dislikes.keys():
        groups[key] = 0
    
    first_pup = list(dislikes.keys())[0]
    groups[first_pup] = 1
    queue = [first_pup]
    visited = set()

    for pup in dislikes:
        while queue:
            current = queue.pop(0)
            visited.add(current)

            if dislikes[current]:
                for dog in dislikes[current]:
                    if groups[dog] == 0:
                        groups[dog] = groups[current] + 1
                        queue.append(dog)
                    elif groups[dog] == groups[current]:
                        return False
        if pup not in visited:
            queue.append(pup)
    return True
    