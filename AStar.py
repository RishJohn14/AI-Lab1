from fringe import Fringe
from state import State
import room



def manhattan_distance(current,goal):
    #Manhattan distance as a heuristic function for A* algorithm
    
    x1, y1, z1 = current
    x2, y2, z2 = goal
    
    distance = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
    
    return distance

def AStar_solver(maze):
    
    fr = Fringe("PRIORITY")
    

    goalCoords = maze.get_goal()
    startCoords = maze.get_start()

    startRoom = maze.get_room(*maze.get_start())

    startDistance = manhattan_distance(startCoords,goalCoords)
    state = State(room=startRoom, parent=None, cost=0, priority=startDistance)

    fr.push(state)

    while not fr.is_empty():

        currentState =  fr.pop()
        currentRoom =  currentState.get_room()
        currentCoords = currentRoom.get_coords()

        if(currentCoords==goalCoords):
            print("Path obtained via A Star Algorithm")
            fr.print_stats()
            currentState.print_path()
            currentState.print_actions()
            print()  # print newline
            maze.print_maze_with_path(currentState)
            return True
        

        for direction in currentRoom.get_connections():
            newRoom,moveCost = currentRoom.make_move(direction,currentState.get_cost())
            newCoords = newRoom.get_coords()
           
            heuristic_value = manhattan_distance(newCoords,goalCoords)
            aStarPriority = moveCost + heuristic_value
            # print(f"Move Cost: {moveCost}, Heuristic Value: {heuristic_value}, Total Priority: {aStarPriority}")
            newState = State(room=newRoom, parent=currentState, cost=moveCost, priority=aStarPriority)
            fr.push(newState)
        

    print("Goal Not Found Via A Star Algorithm")
    return False

