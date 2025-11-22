
import heapq
from Algorithms.BFS import neighbors, is_goal, shortest_path
import time
def heuristic(state, drop_point):
    r, c, has_item = state
    dr, dc = drop_point
    return abs(r - dr) + abs(c - dc)

def terrain_cost(grid, r, c):
    cell = grid[r][c]
    if cell == "~":
        return 2
    elif cell == "^":
        return 3
    else:
        return 1   


def A_star(grid, start, pickup, drop_point):
    pq = [] 
    heapq.heappush(pq, (0, start))   
    start_time = time.time()
    came_from = {}
    cost_so_far = {start: 0}
    visited = set()
    node_expansion = 0

    while pq:
        f_score, current = heapq.heappop(pq)
        node_expansion += 1

        if current in visited:
            continue
        visited.add(current)


        if is_goal(current, drop_point):
            end_time = time.time()
            return {
                "path": shortest_path(came_from, current),
                "cost": cost_so_far[current],
                "visited": len(visited),
                "node_expansion": node_expansion,
                "time": end_time - start_time
            }   
            


        for nb in neighbors(current, grid, pickup):
            nr, nc, _ = nb

            move_cost = terrain_cost(grid, nr, nc)
            new_cost = cost_so_far[current] + move_cost


            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                came_from[nb] = current

                # A* priority = g + h
                priority = new_cost + heuristic(nb, drop_point)

                heapq.heappush(pq, (priority, nb))
    end_time = time.time()
    return {
        "path": None,
        "cost": None,
        "visited": len(visited),
        "node_expansion": node_expansion,
        "time": end_time - start_time
    }