# Interactive Maze Pathfinding Visualizer

An interactive Python-based maze solving and visualization project implementing DFS and BFS pathfinding algorithms with real-time traversal animation using Pygame.

---

# Features

* DFS (Depth First Search) maze solving using Stack
* BFS (Breadth First Search) shortest path algorithm using Queue
* Real-time maze visualization using Pygame
* Random maze and obstacle generation
* Animated path traversal
* Execution time comparison between DFS and BFS
* Dynamic obstacle handling
* Start and destination node visualization

---

# Algorithms Used

## DFS (Depth First Search)

* Implemented using a custom stack
* Explores deeply before backtracking
* Does not guarantee shortest path

## BFS (Breadth First Search)

* Implemented using queue data structure
* Guarantees shortest path in unweighted mazes
* Used for shortest path visualization

---

# Technologies Used

* Python
* Pygame
* Object-Oriented Programming
* Data Structures and Algorithms

---

# Project Structure

```text
Interactive-Maze-Pathfinding-Visualizer/
│
├── main.py
├── navigator.py
├── bfs_navigator.py
├── visualizer.py
├── maze.py
├── maze_generator.py
├── stack.py
├── exception.py
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/prathivds08/SDE-Projects.git
```

## Move Into Project Folder

```bash
cd Interactive-Maze-Pathfinding-Visualizer
```

## Install Dependencies

```bash
pip install pygame
```

---

# Run the Project

```bash
python main.py
```

---

# Visualization Legend

| Color       | Meaning                |
| ----------- | ---------------------- |
| White       | Empty Cell             |
| Black       | Obstacle / Ghost       |
| Green       | Traversed Path / Start |
| Red         | Destination            |
| Blue Border | Grid Boundary          |

---

# Sample Features Demonstrated

* Shortest path computation
* Graph traversal
* Backtracking
* Queue and Stack implementation
* Pathfinding visualization
* Randomized maze generation

---
