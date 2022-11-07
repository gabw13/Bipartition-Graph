# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if len(dislikes) == 0:
        return True

    all_puppies = list(dislikes.keys())
    first_pup = all_puppies[0]
    # if len(dislikes) == 1:
    #     return [first_pup]

    queue = [first_pup]
    visited = set()
    groups = {
        first_pup: "A"
    }
    

    # i = 0
    for pup in all_puppies:
        while queue:
        # while i < len(queue):
            current = queue.pop(0)
            opposite_group = "B" if groups[current] == "A" else "A"
            # i += 1
            visited.add(current)
            
            # for pup in dislikes[current]:
            if dislikes[current]:
                for pup in dislikes[current]:
                    # print(f"current:{current}")
                    # print(f"pup:{pup}")
                    if pup not in visited:
                        queue.append(pup)
                        # visited.add(pup)
                        groups[pup] = opposite_group
                    elif groups[current] == groups[pup]:
                        return False
        
    return True
    # return visited

dislikes = {
    "Ralph": ["Tony"],
    "Tony": ["Ralph"],
    "Fido": ["Alfie", "Bruno"],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Fido", "James", "T-Bone"],
    "T-Bone": ["Alfie", "Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"],
    "Bruno": ["Fido"]
}
    

print (possible_bipartition(dislikes))
