# SLE-2: BFS vs DFS Performance Profiling

## 1. Project Overview

This project is part of **SLE-2: Empirical Performance Profiling** for the course **02AML204 – Introduction to Artificial Intelligence**.

The project compares two search algorithms:

* Breadth First Search (BFS)
* Depth First Search (DFS)

Both algorithms are tested on the **same 20-node graph**, with the same starting node and goal node.

The performance is evaluated using actual execution-time measurements and the number of nodes expanded.

---

## 2. Objective

The objectives of this project are:

* To implement BFS and DFS for graph searching.
* To compare the performance of BFS and DFS on the same problem.
* To measure actual execution time.
* To count the number of nodes expanded.
* To run the benchmark multiple times.
* To calculate the average performance over 3 trials.
* To use `py-spy` for performance profiling.
* To make a data-based comparison of the two algorithms.

---

## 3. Problem

A graph containing **20 nodes from A to T** is used.

The same graph, starting node **A**, and goal node **T** are used for both BFS and DFS.

### Graph Structure

```text
                         A
                    /    |    \
                   B     C     D
                /  |  \ / | \ / | \
               E   F   G H  I  J K  L  M
              / \  | \ / \ |  |  | \ / \
             N   O P  Q R  S R  T  S N  R
             |   | |  | |  | |  |  | |  |
             +---+---+--+---+--+--+--+---+
                         |
                         T
```

### Node Connections

```text
A
├── B
│   ├── E
│   │   ├── N
│   │   └── O
│   ├── F
│   │   ├── P
│   │   └── Q
│   └── G
│       ├── R
│       └── S
│
├── C
│   ├── H
│   │   ├── N
│   │   └── P
│   ├── I
│   │   ├── O
│   │   └── Q
│   └── J
│       ├── R
│       └── T
│
└── D
    ├── K
    │   ├── S
    │   └── T
    ├── L
    │   ├── N
    │   └── R
    └── M
        ├── Q
        └── S

N ──→ T
O ──→ T
P ──→ T
Q ──→ T
R ──→ T
S ──→ T
```

**Start Node:** A

**Goal Node:** T

**Total Nodes:** 20

---

## 4. Algorithms

### Breadth First Search (BFS)

BFS explores the graph level by level.

It uses a **queue** data structure.

In this project, BFS starts from node A and searches for node T.

### Depth First Search (DFS)

DFS explores one path deeply before backtracking.

It uses a **stack** data structure.

In this project, DFS starts from node A and searches for node T.

---

## 5. Benchmark Method

To obtain measurable execution times, each trial performs:

* **100,000 searches**
* Start node: A
* Goal node: T
* Same graph for BFS and DFS
* **3 trials**

The execution time is measured using Python's:

```python
time.perf_counter()
```

The average of the three trials is then calculated.

### Performance Metrics

The following metrics are recorded:

1. Execution time
2. Nodes expanded per search
3. Average execution time over 3 trials

---

## 6. Benchmark Results

The following results were obtained from the actual execution of the program.

| Metric                 |            BFS |            DFS |
| ---------------------- | -------------: | -------------: |
| Trial 1                |     0.364313 s |     0.118657 s |
| Trial 2                |     0.363185 s |     0.106662 s |
| Trial 3                |     0.331789 s |     0.115508 s |
| **Average Time**       | **0.353096 s** | **0.113609 s** |
| Average Time in ms     |     353.096 ms |     113.609 ms |
| Average Nodes Expanded |             20 |              5 |

### Important Note

The reported execution times are the benchmark times for **100,000 searches in each trial**.

They are not the execution time of one individual graph search.

---

## 7. Results Analysis

### BFS

BFS expanded an average of **20 nodes per search**.

The average benchmark execution time over the three trials was:

```text
0.353096 seconds
```

### DFS

DFS expanded an average of **5 nodes per search**.

The average benchmark execution time over the three trials was:

```text
0.113609 seconds
```

### Comparison

For this particular graph, graph structure, and implementation:

* BFS expanded more nodes than DFS.
* DFS expanded fewer nodes in this test case.
* The measured average benchmark time of DFS was lower than BFS.

Therefore, based on the actual measured data for this test case, DFS had the lower benchmark execution time.

---

## 8. Profiling Using py-spy

`py-spy` was used as an additional profiling tool.

The profiling command used was:

```bash
py-spy record -o profile.svg -- python bfs_dfs.py
```

The profiling process successfully generated:

```text
profile.svg
```

The py-spy profiling result contained:

```text
Samples: 113
Errors: 0
```

The generated flame graph can be used to observe where the Python program spends its execution time.

---

## 9. Tools and Technologies

### Programming Language

Python

### Algorithms

* Breadth First Search
* Depth First Search

### Python Libraries

```python
collections
time
```

### Profiling Tool

```text
py-spy
```

### Development Environment

Visual Studio Code

### Version Control

Git and GitHub

---

## 10. How to Run the Project

### Run the BFS and DFS benchmark

Open the terminal in the project folder and run:

```bash
python bfs_dfs.py
```

The program performs three trials and displays the individual trial results and the final average.

### Run py-spy

Use:

```bash
py-spy record -o profile.svg -- python bfs_dfs.py
```

This generates a flame graph named:

```text
profile.svg
```

---

## 11. Project Structure

```text
SLE2_BFS_DFS/
│
├── bfs_dfs.py
│
├── search_benchmark.py
│
├── README.md
│
├── CONTRIBUTION.md
│
├── .gitignore
│
└── profile/
    └── .gitkeep
```

### File Description

| File                  | Purpose                                              |
| --------------------- | ---------------------------------------------------- |
| `bfs_dfs.py`          | BFS and DFS implementation and performance benchmark |
| `search_benchmark.py` | Benchmark-related support code                       |
| `README.md`           | Project documentation                                |
| `CONTRIBUTION.md`     | Student contribution and AI assistance record        |
| `.gitignore`          | Files excluded from Git tracking                     |
| `profile/`            | Stores profiling results                             |

---

## 12. GitHub Repository

The project is maintained using Git and GitHub.

Git is used to track changes in the project, while GitHub is used to store and share the project repository.

The repository contains the source code, documentation, contribution information, and project configuration files.

---

## 13. AI Assistance

AI assistance was used during the development process for:

* Understanding BFS and DFS implementation.
* Understanding empirical performance profiling.
* Structuring the benchmark.
* Understanding how to use `py-spy`.
* Debugging installation and command-line issues.
* Preparing project documentation.
* Organizing the GitHub repository.

The code was executed and tested by the student, and the benchmark values reported in this README were obtained from actual program execution.

---

## 14. Conclusion

BFS and DFS were implemented and tested on the same 20-node graph.

Each algorithm was tested for three trials, with each trial performing 100,000 searches.

The average benchmark execution time was:

```text
BFS = 0.353096 seconds
DFS = 0.113609 seconds
```

The average number of nodes expanded was:

```text
BFS = 20 nodes
DFS = 5 nodes
```

For this particular graph and implementation, DFS showed a lower measured benchmark execution time and expanded fewer nodes than BFS.

The comparison is based on actual performance measurements rather than theory alone.
