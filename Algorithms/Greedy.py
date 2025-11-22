import heapq
import time
from Algorithms.BFS import is_goal , neighbors , shortest_path
def heuristic_map (grid, drop_points):
    dr ,dc =drop_points 
    h_map=[]
    for i in range(len(grid)): 
        rows=[]
        for j in range(len(grid)): 
            rows.append(0)
        h_map.append(rows)
    for r in range(len(grid)): 
        for c in range(len(grid)): 
            if grid[r][c]=="|" : 
                h_map[r][c]= float("inf")
            else : 
                h_map[r][c] = abs(r-dr)+abs(c-dc)
    return h_map


def Greedy(grid, start, pickup, drop_point, h_map):

    pq = []
    heapq.heappush(pq, (0, start))  
    came_from = {}
    visited = set()
    node_expansion = 0
    start_time= time.time()
    while pq:
        h, current = heapq.heappop(pq)
        node_expansion += 1

        if current in visited:
            continue
        visited.add(current)

        if is_goal(current, drop_point):
            end_time=time.time()
            return {
                "path": shortest_path(came_from, current),
                "visited": len(visited),
                "node_expansion": node_expansion,
                "time" : end_time-start_time
            }

        for nb in neighbors(current, grid, pickup):
            if nb not in visited:
                r, c, _ = nb
                priority = h_map[r][c]  
                came_from[nb] = current
                heapq.heappush(pq, (priority, nb))
    end_time= time.time()
    return {
        "path": None,
        "visited": len(visited),
        "node_expansion": node_expansion,
        "time": end_time-start_time

    }

def print_heuristic_map(h_map):
    for row in h_map:
        printable_row = []
        for value in row:
            if value == float("inf"):
                printable_row.append(" X ")     
            else:
                printable_row.append(f"{value:2}")
        print(" ".join(printable_row))
    print("\n\n")
