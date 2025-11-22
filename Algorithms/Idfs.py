from Algorithms.BFS import shortest_path, neighbors, is_goal
import time

def depth_limited_DFS(current, grid, pickup, drop_point, limit, came_from, visited):

    if limit == 0:
        if is_goal(current, drop_point):
            return current
        return None

    visited.add(current)

    for nb in neighbors(current, grid, pickup):
        if nb not in visited:
            came_from[nb] = current

            result = depth_limited_DFS(
                nb, grid, pickup, drop_point,
                limit - 1, came_from, visited
            )

            if result is not None:
                return result

    return None


def IDDFS(grid, start, pickup, drop_point, max_depth=100):

    start_time = time.time()

    for depth in range(max_depth):
        came_from = {}
        visited = set()

        result = depth_limited_DFS(
            start, grid, pickup,
            drop_point, depth,
            came_from, visited
        )

        if result is not None:
            end_time = time.time()
            return {
                "path": shortest_path(came_from, result),
                "visited": len(visited),
                "depth": depth,
                "time": end_time - start_time
            }
    end_time = time.time()
    return {
        "path": None,
        "visited": len(visited),
        "depth": max_depth,
        "time": end_time - start_time
    }
