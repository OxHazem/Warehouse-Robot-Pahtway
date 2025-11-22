from Algorithms.BFS import BFS ,shortest_path , print_grid_path
from genrate_map.random_map_generator import Random_map , is_reachable ,print_grid
from Algorithms.DFS import DFS
from Algorithms.UCS import UCS
from Algorithms.Idfs import IDDFS
from Algorithms.Greedy import heuristic_map ,Greedy , print_heuristic_map
from Algorithms.A_star import A_star , heuristic
import copy

def run_BFS(grid, start_state, objective, drop_points):
    print("\n=========== BFS Algorithm Execution ===========\n")
    grid_bfs = copy.deepcopy(grid)
    print_grid(grid_bfs)
    result = BFS(grid_bfs,start_state,objective,drop_points)
    if not result:
        print("No path.")
        return
    path = result['path']
    print("Path to pickup:", path)
    print("Visited:", result['visited'])
    print("Node expansions:", result['Node_expansion'])
    last = path[-1]
    grid_bfs[last[0]][last[1]] = ' '
    drop = BFS(grid_bfs, last, None, drop_points)
    print("\nPath to drop:", drop['path'])
    print_grid_path(path, grid_bfs)

def run_DFS(grid, start_state, objective, drop_points):
    print("\n=========== DFS Algorithm Execution ===========\n")
    grid_dfs = copy.deepcopy(grid)
    print_grid(grid_dfs)
    result = DFS(grid_dfs,start_state,objective,drop_points)
    if not result:
        print("No path.")
        return
    path = result['path']
    print("Path to pickup:", path)
    last = path[-1]
    grid_dfs[last[0]][last[1]]=' '
    drop = DFS(grid_dfs,last,None,drop_points)
    print_grid_path(path, grid_dfs)

def run_UCS(grid, start_state, objective, drop_points):
    print("\n=========== UCS Algorithm Execution ===========\n")
    grid_cp = copy.deepcopy(grid)
    print_grid(grid_cp)
    result = UCS(grid_cp,start_state,objective,drop_points)
    if not result:
        return
    path = result['path']
    print("Path:", path)

def run_IDDFS(grid, start_state, objective, drop_points):
    print("\n=========== IDDFS Algorithm Execution ===========\n")
    grid_cp = copy.deepcopy(grid)
    print_grid(grid_cp)
    result = IDDFS(grid_cp,start_state,objective,drop_points,max_depth=100)
    if not result:
        return
    path = result['path']
    print("Path:", path)

def run_Greedy(grid, start_state, objective, drop_points):
    print("\n=========== Greedy Algorithm Execution ===========\n")
    grid_cp = copy.deepcopy(grid)
    print_grid(grid_cp)
    hmap = heuristic_map(grid_cp,drop_points)
    print_heuristic_map(hmap)
    result = Greedy(grid_cp,start_state,objective,drop_points,hmap)
    print(result['path'])

def run_Astar(grid, start_state, objective, drop_points):
    print("\n=========== A* Algorithm Execution ===========\n")
    grid_cp = copy.deepcopy(grid)
    print_grid(grid_cp)
    hmap = heuristic_map(grid_cp,drop_points)
    print_heuristic_map(hmap)
    result = A_star(grid_cp,start_state,objective,drop_points)
    print(result['path'])


def main():
    print("Generating map...")
    grid, start, objective, drop_points = Random_map(10, 0.2, weighted=True)
    start_state = (start[0], start[1], 0)

    while True:
        print("\n====== MENU ======")
        print("1. BFS")
        print("2. DFS")
        print("3. UCS")
        print("4. IDDFS")
        print("5. Greedy")
        print("6. A*")
        print("7. Run ALL algorithms")
        print("8. Regenerate map")
        print("9. Exit")
        
        choice = int(input("Choose: "))

        if choice == 1:
            run_BFS(grid, start_state, objective, drop_points)

        elif choice == 2:
            run_DFS(grid, start_state, objective, drop_points)

        elif choice == 3:
            run_UCS(grid, start_state, objective, drop_points)

        elif choice == 4:
            run_IDDFS(grid, start_state, objective, drop_points)

        elif choice == 5:
            run_Greedy(grid, start_state, objective, drop_points)

        elif choice == 6:
            run_Astar(grid, start_state, objective, drop_points)

        elif choice == 7:
            run_BFS(grid, start_state, objective, drop_points)
            run_DFS(grid, start_state, objective, drop_points)
            run_UCS(grid, start_state, objective, drop_points)
            run_IDDFS(grid, start_state, objective, drop_points)
            run_Greedy(grid, start_state, objective, drop_points)
            run_Astar(grid, start_state, objective, drop_points)

        elif choice == 8:
            print("\n=== NEW MAP GENERATED ===")
            grid, start, objective, drop_points = Random_map(10, 0.2, weighted=True)
            start_state = (start[0], start[1], 0)
            print_grid(grid)

        elif choice == 9:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
