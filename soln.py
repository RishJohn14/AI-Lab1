#!/usr/bin/env python3

from state import State
from maze import Maze

def manhattan_distance(coords1, coords2):
    """Calculate Manhattan distance between two sets of coordinates"""
    return sum(abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) for (x1, y1, z1), (x2, y2, z2) in zip(coords1, coords2))

def greedy_best_first_search(maze):
    goal_coords = maze.get_goal()  # Get coordinates of the goal room

    # Initialize fringe with start state
    start_coords = maze.get_start()
    start_room = maze.get_room(*start_coords)
    start_heuristic = manhattan_distance(start_coords, goal_coords)
    start_state = State(room=start_room, cost=0, priority=start_heuristic)
    fringe = [start_state]

    while fringe:
        # Sort fringe based on heuristic value (priority queue)
        fringe.sort(key=lambda x: x.priority)

        # Pop state with lowest heuristic value
        current_state = fringe.pop(0)
        current_room = current_state.get_room()
        current_coords = current_room.get_coords()

        if current_coords == goal_coords:
            print("Goal room found!")
            current_state.print_path()  # Print the path to the goal state
            return True

        # Explore adjacent rooms
        for direction in current_room.get_connections():
            new_coords, _ = current_room.make_move(direction, 0)
            new_room = maze.get_room(*new_coords)
            heuristic_value = manhattan_distance(new_coords, goal_coords)
            new_state = State(room=new_room, parent=current_state, cost=current_state.get_cost() + 1, priority=heuristic_value)
            fringe.append(new_state)

    print("Goal room not found")
    return False

# Example usage
maze = Maze()  # Create the maze object
result = greedy_best_first_search(maze)
print("Solution found:", result)
