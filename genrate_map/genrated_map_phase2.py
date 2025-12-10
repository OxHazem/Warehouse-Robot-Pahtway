from random_map_generator import is_reachable 
import random
def Random_map_for_multiple_bots(size, obstacle_density, weighted=False, heuristic=False):
    while True:
       
        grid = [["*" for _ in range(size)] for _ in range(size)]

      
        for r in range(size):
            for c in range(size):
                if random.random() < obstacle_density:
                    grid[r][c] = "|"

       
        if weighted:
            for r in range(size):
                for c in range(size):
                    if grid[r][c] == "*":
                        grid[r][c] = random.choices(
                            ["*", "~", "^"],
                            weights=[0.7, 0.2, 0.1],
                            k=1
                        )[0]

        
        free_cells = []

        for r in range(size):
            for c in range(size):
                if grid[r][c] != "|":
                    free_cells.append((r, c))


       
        if len(free_cells) < 4:
            continue

        
        start_A = random.choice(free_cells)
        free_cells.remove(start_A)

        start_B = random.choice(free_cells)
        free_cells.remove(start_B)

        drop_point = random.choice(free_cells)
        free_cells.remove(drop_point)

        objective = random.choice(free_cells)
        free_cells.remove(objective)

        
        if not is_reachable(grid, start_A, objective):
            continue
        if not is_reachable(grid, start_A, drop_point):
            continue
        if not is_reachable(grid, start_B, objective):
            continue
        if not is_reachable(grid, start_B, drop_point):
            continue

        
        ar, ac = start_A
        br, bc = start_B
        or_, oc = objective
        dr, dc = drop_point

        grid[ar][ac] = "A"  
        grid[br][bc] = "B"  
        grid[or_][oc] = "O"  
        grid[dr][dc] = "D"  

        return grid, start_A, start_B, objective, drop_point

