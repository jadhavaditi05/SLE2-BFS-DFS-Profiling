import cProfile
import pstats

from bfs_dfs import bfs, dfs, graph


def run_bfs():
    for _ in range(100000):
        bfs(graph, 'A', 'T')


def run_dfs():
    for _ in range(100000):
        dfs(graph, 'A', 'T')


print("==============================================")
print("          BFS PROFILING")
print("==============================================")

bfs_profiler = cProfile.Profile()
bfs_profiler.enable()

run_bfs()

bfs_profiler.disable()

bfs_stats = pstats.Stats(bfs_profiler)
bfs_stats.sort_stats("cumulative")
bfs_stats.dump_stats("profile/bfs_profile.prof")
bfs_stats.print_stats(10)


print("\n==============================================")
print("          DFS PROFILING")
print("==============================================")

dfs_profiler = cProfile.Profile()
dfs_profiler.enable()

run_dfs()

dfs_profiler.disable()

dfs_stats = pstats.Stats(dfs_profiler)
dfs_stats.sort_stats("cumulative")
dfs_stats.dump_stats("profile/dfs_profile.prof")
dfs_stats.print_stats(10)