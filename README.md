# Labyrinth Solver

A simple recursie python algorythm  I made a while ago for finding the path along a maze.

## Overview

This program finds paths through labyrinths containing various special tiles and obstacles. The algorithm uses a recursive approach to explore all possible routes while managing a character's health points (HP) and handling special interactive elements.

## Files

- `lab.py`: Main program with the solving algorithm
- `laberintos.py`: Collection of predefined labyrinths for testing

## Labyrinth Elements

Labyrinths are represented as 2D arrays with the following symbols:

- `O`: Starting point
- `X`: Wall (impassable)
- `-`: Path (passable)
- `⬛`: Visited path
- `K+n`: Health tile (adds n health points)
- `K-n`: Damage tile (subtracts n health points)
- `V`: Poison tile (continuously drains health)
- `Sn`: Trap trigger (activates corresponding trap wall when stepped on)
- `Tn`: Trap wall (becomes a wall when its trigger is activated)

## Exit Condition

The exit of the labyrinth is defined as any `-` tile adjacent to the border of the maze. When the character reaches such a tile, the labyrinth is considered solved.

## Health System

- The character starts with a predefined number of HP (set for each labyrinth)
- Walking on damage tiles (`K-n`) reduces HP by n points
- Walking on health tiles (`K+n`) increases HP by n points
- Walking on poison tiles (`V`) applies a poison effect that continuously drains HP
- If HP reaches 0, the character dies and that path is considered invalid

## Trap System

- When a character steps on a trap trigger (`Sn`), the corresponding trap wall (`Tn`) becomes a wall (`X`)
- This can change the available paths through the labyrinth

## How to Run

1. Make sure both files (`lab.py` and `laberintos.py`) are in the same directory
2. Run the main file:
   ```
   python lab.py
   ```
3. The program will attempt to solve the current labyrinth and display the result

## Modifying Labyrinths

To use a different predefined labyrinth:

1. Open `lab.py`
2. Import the desired labyrinth from `laberintos.py`
3. Call the function with the appropriate parameters:
   ```python
   from laberintos import lab2
   labyrinth, HP = lab2(labyrinth, 0, 10)  # Example parameters
   ```
 OR
4. dit the `laberynth` variable in `lab.py` 

## Creating Custom Labyrinths

You can create your own labyrinths by:

1. Opening `laberintos.py`
2. Adding a new function following the pattern of existing ones
3. Defining your labyrinth as a 2D array with appropriate symbols
4. Setting the initial HP value
5. Importing and using your new labyrinth in `lab.py`

## Output

The program will print:
- The final state of the labyrinth (showing the path taken)
- Whether the labyrinth could be solved
- The remaining HP if solved
- The reason for failure if not solved (no exit or character death)


```
Si se pudo resolver el laberinto
Con 5 de vida restante
```
Or in case of failure:
```
No se pudo resolver el laberinto
No hay salida
```

## Important Notes

- Set `predetermined_start = True` in the `lab_start` function to use the predefined starting point ('O')
- The algorithm uses a depth-first search approach to find a valid path
- The program automatically handles all special tiles and their effects
