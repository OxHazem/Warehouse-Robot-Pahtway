from collections import deque
import time
from genrate_map.random_map_generator import print_grid
def shortest_path (came_from , goal_state) :
    path=[goal_state]
    current=goal_state

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path 

def neighbors(state, grid, pickup):
    size = len(grid)
    r, c, has_item = state
    result = []
    
    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] != "|":
            new_item = has_item
            if (nr, nc) == pickup:
                new_item = 1
            result.append((nr, nc, new_item))
    return result


def is_goal(state, drop_points):
    r, c, has_item = state
    return has_item == 1 and (r, c) == drop_points
    
def BFS (grid ,start , pickup, drop_points) : 
    visited = set()
    came_from={}
    start_time=time.time()
    qeueu =deque([start])

    visited.add(start)
    node_expansion= 0
    while qeueu : 
        current = qeueu.popleft()
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
                qeueu.append(nb)


    end_time = time.time()
    return {
        "path": None,
        "nodes_expanded": node_expansion,
        "time": end_time - start_time,
        "visited": len(visited)
    }


def print_grid_path(path_to_dropout,grid):
    drop_point = path_to_dropout[-1]
    for row_position, column_position, item in path_to_dropout:
        grid[row_position][column_position] = 'R'
        if item == 1:
            grid[row_position][column_position] = 'P'
            grid[drop_point[0]][drop_point[1]] = 'D'    
        print_grid(grid)


        
