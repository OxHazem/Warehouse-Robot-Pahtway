import random

from collections import deque

def is_reachable(grid, start, goal):
    size = len(grid)
    (sr, sc) = start
    (gr, gc) = goal

    queue = deque([(sr, sc)])
    visited = set([(sr, sc)])
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == (gr, gc):
            return True
        
        # possible movements
        moves = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        for nr, nc in moves:
            if 0 <= nr < size and 0 <= nc < size:
                if grid[nr][nc] != "|" and (nr, nc) not in visited:  
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    return False


def Random_map (size,obstacle_density,weighted=False , heurisitc=False) : 
    while True : 
        grid = [] # made 2d materces filled * 
        for r in range(size) : 
            row=[]
            for c in range(size): 
                row.append("*")
            grid.append(row)
        
        for r in range(size) : 
            for c in range(size): 
                if random.random() < obstacle_density : 
                    grid[r][c]= "|"
        if weighted :
            free_cells=[]
            for r in range (size) : 
                for c in range(size): 
                    if grid[r][c] == "*" :
                        grid[r][c] = random.choices(
                        
                            ["*", "~", "^"], 
                            weights=[0.7, 0.2, 0.1],  # probability distribution
                            k=1
                        
                        )[0]
            for r in range (size) : 
                for c in range(size): 
                    if grid[r][c] != "|" : 
                        free_cells.append((r,c))       
        else:
            free_cells =[]
            for r in range (size) : 
                for c in range(size): 
                    if grid[r][c] == "*" : 
                        free_cells.append((r,c))
        
        
        if len(free_cells) < 3 : 
            continue
        
        start= random.choice(free_cells)
        free_cells.remove(start)

        drop_point=random.choice(free_cells)

        objective=random.choice(free_cells)
        free_cells.remove(objective)

        if not is_reachable(grid,start,drop_point): 
            continue
        if not is_reachable(grid,objective,drop_point): 
            continue

        sr,sc=start
        Objr,Objc=objective
        dr ,dc=drop_point


        grid[sr][sc]="S"
        grid[Objr][Objc]="O"
        grid[dr][dc]="D"

        return grid ,start , objective ,drop_point

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n \n \n")
# test 
# grid = Random_map (10 , 0.2)
# print_grid(grid=grid)


