
# 🤖 AI Search Systems Project  
### Phase 1: Warehouse Robot Pathfinding  
### Phase 2: Connect-4 Adversarial Search (Minimax & Alpha-Beta)

---

## 📌 Overview

This repository contains two major artificial intelligence systems developed using classical search and adversarial search algorithms.

---

# 🟦 PHASE 1 – Warehouse Robot Pathfinding System  
### Classical Uninformed & Informed Search Algorithms

Phase 1 implements a warehouse robot navigation system operating in a **randomly generated grid environment**. The objective is to navigate from:

- **Start (S)**  
- **Pickup point (O)**  
- **Drop-off point (D)**  

The warehouse grid includes obstacles and weighted terrain, making the search problem realistic and computationally meaningful.

---

## 🚀 Phase 1 Features

- Random grid generation every run  
- Weighted terrain types:  
  - `*` → free cell  
  - `~` → medium weight  
  - `^` → high weight  
  - `|` → obstacle  
- Automatic placement of S, O, D  
- Ensures all points are reachable  
- Step-by-step path visualization  
- Algorithm performance metrics:
  - Path cost  
  - Expanded nodes  
  - Visited states  
  - Execution time  

---

## 🧠 Phase 1 Algorithms Implemented

### 🔹 **Uninformed Search**
- **Breadth-First Search (BFS)** – shortest path for uniform-cost terrain  
- **Depth-First Search (DFS)** – deeper exploration; not optimal  
- **Iterative Deepening DFS (IDDFS)** – combines DFS space efficiency with BFS completeness  

### 🔹 **Informed / Optimal Search**
- **Uniform Cost Search (UCS)** – optimal path with weighted terrain  
- **Greedy Best-First Search** – fast heuristic-driven approach  
- **A\* Search** – optimal and efficient for weighted environments  

These algorithms allow for detailed comparison of speed, optimality, and node expansion.

---

## 📂 Phase 1 Folder Structure

```

Algorithms/
│── BFS.py
│── DFS.py
│── Idfs.py
│── UCS.py
│── Greedy.py
│── A_star.py

genrate_map/
│── random_map_generator.py
│── Test_random_map.py

main.py   ← Phase 1 runner

```

---

# 🟩 PHASE 2 – Connect-4 Adversarial Search  
### Minimax, Alpha-Beta Pruning & Heuristic Evaluation

Phase 2 implements a complete **Connect-4 game engine** and intelligent AI agents that make optimal moves using adversarial search algorithms.

This phase demonstrates how search trees, heuristics, pruning, and game modeling work together in a competitive environment.

---

## 🎮 Phase 2 Features

- Full Connect-4 board implementation  
- Game modeling:
  - State representation  
  - Move generation  
  - Terminal state detection  
- **Minimax algorithm** with depth-limited search  
- **Alpha-Beta pruning** for efficiency  
- Heuristic evaluation based on:
  - 4-cell window scoring  
  - Center-column advantage  
  - Threat detection  
- Bot-vs-Bot experiments:
  - Minimax vs Random  
  - Alpha-Beta vs Random  
  - Move-by-move stats (nodes expanded, time taken)  
- Reusable scripts for analysis and benchmarking  

---

## 🧪 Phase 2 Experimental Results

### ✔ **Single Board Evaluation**
Using a fixed mid-game position:

| Algorithm  | Best Move | Nodes Expanded | Time (s) | Score |
|------------|-----------|----------------|----------|--------|
| Minimax    | 3         | 18,935         | 3.63     | 33     |
| Alpha-Beta | 3         | 2,024          | 0.36     | 33     |

**Alpha-Beta produced the same optimal move while exploring ~90% fewer nodes.**

---

### ✔ **Full Game: Minimax vs Random**
- **Total nodes:** 18,331  
- **Total time:** 3.66s  
- **Winner:** AI  

Minimax expands ~2600–2800 nodes per move.

---

### ✔ **Full Game: Alpha-Beta vs Random**
- **Total nodes:** 2,618  
- **Total time:** 0.47s  
- **Winner:** AI  

Alpha-Beta expands only ~400–650 nodes per move, making it ~8× faster.

---

## 📂 Phase 2 Folder Structure

```

Phase2_game/
│
├── game/
│   ├── board.py
│   ├── logic.py
│   └── **init**.py
│
├── ai/
│   ├── minimax.py
│   ├── alphabeta.py
│   ├── evaluation.py
│   ├── random_bot.py
│   └── **init**.py
│
├── experiments/
│   ├── compare_algorithm.py
│   ├── compare_during_game.py
│   ├── bot_vs_bott.py
│   └── **init**.py
│
└── main.py   ← Connect-4 game runner

````

---

# ▶️ How to Run

### **Run Phase 1 (Warehouse Navigation)**  
```bash
python3 main.py
````

---

### **Run Phase 2 Experiments (Connect-4)**

#### Compare Minimax vs Alpha-Beta on the same board:

```bash
python -m Phase2_game.experiments.compare_algorithm
```

#### Run full bot-vs-bot games:

```bash
python -m Phase2_game.experiments.bot_vs_bott
```

#### Show move-by-move stats (nodes/time):

```bash
python -m Phase2_game.experiments.compare_during_game
```

#### Play or test the Connect-4 engine:

```bash
python Phase2_game/main.py
```

---

# 📜 License

This project is for academic and research purposes.

---

# 🙋‍♂️ Author

Omar Hazem Ahmed
Faculty of Computer and Artificial Intelligence | 2025


