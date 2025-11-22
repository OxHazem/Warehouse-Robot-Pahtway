import time
from Algorithms.BFS import shortest_path , neighbors , is_goal

def DFS (grid , Start ,pickup,drop_points):
    visited = set()
    came_from={}
    start_time=time.time()
    stack =[Start]

    visited.add(Start)
    node_expansion= 0
    while stack : 
        current = stack.pop()
        node_expansion +=1
        if is_goal(current,drop_points):
            end_time=time.time() 
            return {
                'path' : shortest_path(came_from , current) , 
                'time' : end_time - start_time , 
                'visited': len(visited) , 
                'Node_expansion' : node_expansion
            }
        for nb  in neighbors(current , grid, pickup) : 
            if nb  not in  visited : 
                visited.add(nb)
                came_from[nb]=current
                stack.append(nb)


    end_time = time.time()
    return {
        "path": None,
        "nodes_expanded": node_expansion,
        "time": end_time - start_time,
    } 