import matplotlib.pyplot as plt

WORLD_SIZE = int(input("Enter Wumpus World size: "))

def neighbors(x, y):
    adj = []
    if x > 1: adj.append((x - 1, y))
    if x < WORLD_SIZE: adj.append((x + 1, y))
    if y > 1: adj.append((x, y - 1))
    if y < WORLD_SIZE: adj.append((x, y + 1))
    return adj

def create_world():
    world = {}
    for x in range(1, WORLD_SIZE + 1):
        for y in range(1, WORLD_SIZE + 1):
            world[(x, y)] = {
                "A": False,  # Agent
                "W": False,  # Wumpus
                "P": False,  # Pit
                "G": False,  # Gold
                "B": False,  # Breeze
                "S": False   # Stench
            }
    return world

def place_objects(world):
    print("\nEnter Agent position (x y):")
    ax, ay = map(int, input().split())
    world[(ax, ay)]["A"] = True

    print("Enter Wumpus position (x y):")
    wx, wy = map(int, input().split())
    world[(wx, wy)]["W"] = True

    print("Enter Gold position (x y):")
    gx, gy = map(int, input().split())
    world[(gx, gy)]["G"] = True

    pits = []
    n_pits = int(input("Enter number of pits: "))
    for i in range(n_pits):
        print(f"Enter Pit {i + 1} position (x y):")
        px, py = map(int, input().split())
        world[(px, py)]["P"] = True
        pits.append((px, py))

    return pits, (wx, wy)

def add_percepts(world, pits, wumpus):
    for pit in pits:
        for n in neighbors(*pit):
            world[n]["B"] = True

    for n in neighbors(*wumpus):
        world[n]["S"] = True

def cell_string(cell):
    symbols = []
    for k in ["A", "W", "P", "G", "B", "S"]:
        if cell[k]:
            symbols.append(k)
    return "".join(symbols) if symbols else "."

def display_world_matplotlib(world):
    fig, ax = plt.subplots(figsize=(WORLD_SIZE, WORLD_SIZE))

    # Draw grid lines
    for i in range(WORLD_SIZE + 1):
        ax.plot([0, WORLD_SIZE], [i, i])
        ax.plot([i, i], [0, WORLD_SIZE])

    # Fill grid cells
    for (x, y), cell in world.items():
        ax.text(
            x - 0.5,
            y - 0.5,
            cell_string(cell),
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold"
        )

    ax.set_xlim(0, WORLD_SIZE)
    ax.set_ylim(0, WORLD_SIZE)
    ax.set_xticks(range(WORLD_SIZE + 1))
    ax.set_yticks(range(WORLD_SIZE + 1))
    ax.set_aspect("equal")
    ax.set_title("Wumpus World")
    ax.grid(False)

    plt.show()
########################
KB = {
    "Pit": set(),
    "NoPit": set(),
    "Wumpus": set(),
    "NoWumpus": set(),
    "Safe": set()
}

def update_percepts(world):
    for (x, y), cell in world.items():
        adj = neighbors(x, y)

        # Breeze → Pit inference
        if cell["B"]:
            for n in adj:
                KB["Pit"].add(n)
        else:
            for n in adj:
                KB["NoPit"].add(n)

        # Stench → Wumpus inference
        if cell["S"]:
            for n in adj:
                KB["Wumpus"].add(n)
        else:
            for n in adj:
                KB["NoWumpus"].add(n)

        # Safe square inference
        if not cell["P"] and not cell["W"]:
            KB["Safe"].add((x, y))

def clean_KB():
    KB["Pit"] -= KB["NoPit"]
    KB["Wumpus"] -= KB["NoWumpus"]

def display_KB():
    print("\nKnowledge Base Inference:\n")

    print("Possible Pits:", sorted(KB["Pit"]))
    print("Confirmed No-Pits:", sorted(KB["NoPit"]))

    print("\nPossible Wumpus:", sorted(KB["Wumpus"]))
    print("Confirmed No-Wumpus:", sorted(KB["NoWumpus"]))

    print("\nSafe Squares:", sorted(KB["Safe"]))

world = create_world()
pits, wumpus = place_objects(world)
add_percepts(world, pits, wumpus)

display_world_matplotlib(world)

update_percepts(world)
clean_KB()
display_KB()