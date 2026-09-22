from collections import deque
import time


# ==================================================
# 20-NODE GRAPH: A TO T
# ==================================================

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'I', 'J'],
    'D': ['K', 'L', 'M'],

    'E': ['N', 'O'],
    'F': ['P', 'Q'],
    'G': ['R', 'S'],

    'H': ['N', 'P'],
    'I': ['O', 'Q'],
    'J': ['R', 'T'],

    'K': ['S', 'T'],
    'L': ['N', 'R'],
    'M': ['Q', 'S'],

    'N': ['T'],
    'O': ['T'],
    'P': ['T'],
    'Q': ['T'],
    'R': ['T'],
    'S': ['T'],

    'T': []
}


# ==================================================
# BFS ALGORITHM
# ==================================================

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return nodes_expanded


# ==================================================
# DFS ALGORITHM
# ==================================================

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# ==================================================
# BENCHMARK SETTINGS
# ==================================================

NUMBER_OF_SEARCHES = 100000
NUMBER_OF_TRIALS = 3


# ==================================================
# MEASURE BFS
# ==================================================

def measure_bfs():
    total_nodes = 0

    start_time = time.perf_counter()

    for _ in range(NUMBER_OF_SEARCHES):
        total_nodes += bfs(graph, 'A', 'T')

    end_time = time.perf_counter()

    return end_time - start_time, total_nodes


# ==================================================
# MEASURE DFS
# ==================================================

def measure_dfs():
    total_nodes = 0

    start_time = time.perf_counter()

    for _ in range(NUMBER_OF_SEARCHES):
        total_nodes += dfs(graph, 'A', 'T')

    end_time = time.perf_counter()

    return end_time - start_time, total_nodes


# ==================================================
# RUN BENCHMARK
# ==================================================

if __name__ == "__main__":

    bfs_times = []
    dfs_times = []

    bfs_nodes = []
    dfs_nodes = []

    print("==============================================")
    print("          BFS vs DFS PERFORMANCE")
    print("==============================================")

    print("\nGraph: A to T")
    print("Number of nodes: 20")
    print("Searches per trial:", NUMBER_OF_SEARCHES)
    print("Number of trials:", NUMBER_OF_TRIALS)

    # ==================================================
    # RUN 3 TRIALS
    # ==================================================

    for trial in range(1, NUMBER_OF_TRIALS + 1):

        bfs_time, bfs_total_nodes = measure_bfs()
        dfs_time, dfs_total_nodes = measure_dfs()

        bfs_times.append(bfs_time)
        dfs_times.append(dfs_time)

        bfs_nodes.append(
            bfs_total_nodes / NUMBER_OF_SEARCHES
        )

        dfs_nodes.append(
            dfs_total_nodes / NUMBER_OF_SEARCHES
        )

        print(f"\n--------------- Trial {trial} ---------------")

        print(
            "BFS time:",
            round(bfs_time, 6),
            "seconds"
        )

        print(
            "BFS nodes expanded:",
            round(bfs_nodes[-1], 2)
        )

        print(
            "DFS time:",
            round(dfs_time, 6),
            "seconds"
        )

        print(
            "DFS nodes expanded:",
            round(dfs_nodes[-1], 2)
        )

    # ==================================================
    # CALCULATE AVERAGE
    # ==================================================

    average_bfs_time = (
        sum(bfs_times) / NUMBER_OF_TRIALS
    )

    average_dfs_time = (
        sum(dfs_times) / NUMBER_OF_TRIALS
    )

    average_bfs_nodes = (
        sum(bfs_nodes) / NUMBER_OF_TRIALS
    )

    average_dfs_nodes = (
        sum(dfs_nodes) / NUMBER_OF_TRIALS
    )

    # ==================================================
    # FINAL RESULTS
    # ==================================================

    print("\n==============================================")
    print("             AVERAGE RESULTS")
    print("==============================================")

    print("\nBFS")

    print(
        "Average time:",
        round(average_bfs_time, 6),
        "seconds"
    )

    print(
        "Average time:",
        round(average_bfs_time * 1000, 3),
        "ms"
    )

    print(
        "Average nodes expanded:",
        round(average_bfs_nodes, 2)
    )

    print("\nDFS")

    print(
        "Average time:",
        round(average_dfs_time, 6),
        "seconds"
    )

    print(
        "Average time:",
        round(average_dfs_time * 1000, 3),
        "ms"
    )

    print(
        "Average nodes expanded:",
        round(average_dfs_nodes, 2)
    )

    # ==================================================
    # COMPARISON
    # ==================================================

    print("\n==============================================")
    print("              COMPARISON")
    print("==============================================")

    if average_bfs_time < average_dfs_time:
        print(
            "BFS has lower average benchmark execution time."
        )

    elif average_dfs_time < average_bfs_time:
        print(
            "DFS has lower average benchmark execution time."
        )

    else:
        print(
            "Both algorithms have approximately the same time."
        )