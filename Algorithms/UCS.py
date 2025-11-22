import time
import heapq
from Algorithms.BFS import shortest_path, neighbors, is_goal

def UCS(grid, start, pickup, drop_points):

    start_time = time.time()
    visited = set()
    came_from = {}
    cost_so_far = {start: 0}
    priority_queue = []

    heapq.heappush(priority_queue, (0, start))
    node_expansion = 0

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)
        node_expansion += 1
        if current in visited:
            continue
        

        visited.add(current)

 
        if is_goal(current, drop_points):
            end_time = time.time()
            return {
                'path': shortest_path(came_from, current),
                'time': end_time - start_time,
                'visited': len(visited),
                'Node_expansion': node_expansion,
                'cost': current_cost
            }


        for nb in neighbors(current, grid, pickup):
            terrain = grid[nb[0]][nb[1]]


            if terrain == "~":
                move_cost = 2
            elif terrain == "^":
                move_cost = 3
            else:
                move_cost = 1  

            new_cost = current_cost + move_cost


            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                came_from[nb] = current
                heapq.heappush(priority_queue, (new_cost, nb))

    end_time = time.time()
    return {
        "path": None,
        "nodes_expanded": node_expansion,
        "time": end_time - start_time,
        "visited": len(visited),
        "cost": float("inf")
    }
