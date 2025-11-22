Intelligent Navigation Using Classical AI Search Algorithms
Overview

This project implements an intelligent warehouse robot navigation system designed to operate in a dynamic, randomly generated grid environment. The robot must navigate from a designated start position (S) to a pickup point (O) and finally deliver the item to a drop-off location (D).

The warehouse map includes obstacles and weighted terrain types that affect movement cost, enabling meaningful and realistic comparisons of different search algorithms. The system provides detailed performance metrics and visual path representations to help evaluate algorithm efficiency and behavior.

This represents Phase 1 of the project, focusing on classical search algorithms.
Phase 2 (Reinforcement Learning) will be added in the future.

Features

Randomized grid-based warehouse environment

Obstacles (|), free cells (*), and weighted terrain:

~ medium weight

^ high weight

Automatic placement of Start, Pickup, and Drop-off points

Reachability validation to ensure solvable maps

Detailed step-by-step path visualization

Performance metrics for each algorithm, including:

Path cost

Node expansions

Visited states

Execution time

Implemented Search Algorithms (Phase 1)
Uninformed Algorithms

Breadth-First Search (BFS) – shortest path in uniform grids

Depth-First Search (DFS) – explores deeper paths; not optimal

Iterative Deepening DFS (IDDFS) – combines DFS efficiency with BFS completeness

Informed & Optimal Algorithms

Uniform Cost Search (UCS) – optimal on weighted terrain

Greedy Best-First Search – heuristic-driven; fast but not optimal

A* Search – optimal and efficient; combines heuristics with path cost

Project Structure