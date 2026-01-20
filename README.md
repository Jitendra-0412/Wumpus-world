# Wumpus-world
This project is a Python implementation of the Wumpus World problem. The world is created dynamically, where the positions of the Wumpus, pits, and gold are defined manually.

## Wumpus World Visualization using Knowledge-Based Agent (Python)

This project is a Python implementation of the classic Wumpus World problem from Artificial Intelligence.  
It demonstrates how a knowledge-based agent reasons about an uncertain environment using logical inference and percepts, and visualizes the world using Matplotlib.

## Objectives

- Dynamically create a Wumpus World of any size.
- Place Agent, Wumpus, Gold, and Pits using user input.
- Automatically generate percepts:
  - Breeze near pits.
  - Stench near the wumpus.
- Build a Knowledge Base (KB) using logical rules.
- Inference:
  - Possible pit locations.
  - Possible wumpus locations.
  - Safe cells.
- Visualize the complete world using a grid-based layout.

## Wumpus World Rules Implemented

- A **Breeze** is perceived in squares adjacent to a **Pit**
- A **Stench** is perceived in squares adjacent to the **Wumpus**
- If no Breeze is present, adjacent squares have **no Pit**
- If no Stench is present, adjacent squares have **no Wumpus**
- A square without Pit and Wumpus is considered **Safe**

## Features

Dynamic world size.  
User-defined positions (Agent, Wumpus, Gold, Pits).
Logical inference using a Knowledge Base.
Removal of contradictory KB facts. 
Graphical visualization using Matplotlib. 
