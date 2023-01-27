from random import randint, choice


class Room:

    total_room_list = []

    def __init__(self, x_length, y_length, pos, map):
        self.x_length = x_length
        self.y_length = y_length
        self.pos = pos
        self.left_wall = [(pos[0], pos[1] + i) for i in range(y_length)]
        self.right_wall = [(pos[0] + x_length, pos[1] + i) for i in range(y_length)]
        self.up_wall = [(pos[0] + i, pos[1]) for i in range(x_length)]
        self.down_wall = [(pos[0] + i, pos[1] + y_length) for i in range(x_length)]
        self.coordonates = [self.left_wall, self.up_wall, self.right_wall, self.down_wall]
        for coordonate in self.coordonates:
            map[coordonate[0], coordonate[1]] = 1
        self.doors_coordonates = []
        Room.total_room_list.append(self)

    
    def create_door(self, door_coordonate, wall_index, map):
        self.doors_coordonates.append(door_coordonate)
        map[door_coordonate[0], door_coordonate[1]] = 2
        self.coordonates[wall_index].remove(door_coordonate)
    
    def delete_isolated(self, map):
        if len(self.doors_coordonates) == 0:
            for i in range(4):
                for coords in self.coordonates[i]:
                    map[coords[0], coords[1]] = 0
        Room.total_room_list.remove(self)

    
    def generate_all_paths(map):
        """Génère tous les chemins de toutes les rooms. les rooms isolées sont supprimées"""
        #generation des chemins pour passer d'une room à une autre
        for i, r1 in enumerate(Room.total_room_list):
            for j, r2 in enumerate(Room.total_room_list):
                if j>=i:
                    continue
                create_paths(r1, r2, map)
        
        #recherche et effacement des rooms isolées
        for r in Room.total_room_list:
            r.delete_isolated(map)
        



        
def find_shortest_path(map, start, end):
    # Initialize a queue to store the next cells to visit
    queue = [start]
    # Create a set to keep track of visited cells
    visited = set([start])
    # Create a dictionary to store the previous cell for each cell
    previous = {start: None}
    # While the queue is not empty
    while queue:
        # Dequeue the first cell
        current = queue.pop(0)
        # If the current cell is the end cell, return the path
        if current == end:
            return construct_path(previous, end)
        # Iterate through the possible next moves
        for neighbor in get_neighbors(map, current):
            # If the neighbor has not been visited
            if neighbor not in visited:
                # Enqueue the neighbor
                queue.append(neighbor)
                # Mark the neighbor as visited
                visited.add(neighbor)
                # Store the current cell as the previous cell for the neighbor
                previous[neighbor] = current
    # If the queue is empty and the end was not reached, return None
    return None


def get_neighbors(map, cell):
    x, y = cell
    neighbors = []
    # Check if the cell above is a valid move
    if x > 0 and map[x-1][y] != 0:
        neighbors.append((x-1, y))
    # Check if the cell to the right is a valid move
    if y < len(map[0])-1 and map[x][y+1] != 0:
        neighbors.append((x, y+1))
    # Check if the cell below is a valid move
    if x < len(map)-1 and map[x+1][y] != 0:
        neighbors.append((x+1, y))
    # Check if the cell to the left is a valid move
    if y > 0 and map[x][y-1] != 0:
        neighbors.append((x, y-1))
    return neighbors

def construct_path(previous, current):
    # Initialize an empty list to store the path
    path = [current]
    # While the current cell has a previous cell
    while current in previous:
        # Set the current cell to the previous cell
        current = previous[current]
        # Append the current cell to the path
        path.append(current)
    # Return the path in the correct order
    return path[::-1]


def starting_path_position(room):
    wall_index = randint(0, 3)
    door_coordonate = choice(room.coordonates[wall_index])
    if wall_index == 0:
        starting_pos = (door_coordonate[0]-1, door_coordonate[1])
        return door_coordonate, starting_pos, wall_index
    elif wall_index == 1:
        starting_pos = (door_coordonate[0], door_coordonate[1]-1)
        return door_coordonate, starting_pos, wall_index
    elif wall_index == 2:
        starting_pos = (door_coordonate[0]+1, door_coordonate[1])
        return door_coordonate, starting_pos, wall_index
    else:
        starting_pos = (door_coordonate[0], door_coordonate[1]+1)
        return door_coordonate, starting_pos, wall_index

def create_paths(room_1, room_2, map):

    #Création d'une liste de chemins possibles sur 100 essaies de couple de portes différent
    path_list = []
    for _ in range(100):
        first_door_pos, first_starting_pos, wall_1_index = starting_path_position(room_1)
        second_door_pos, second_starting_pos, wall_2_index = starting_path_position(room_2)
        path = find_shortest_path(map, first_starting_pos, second_starting_pos)
        if path is not None:
            path_list.append(path, first_door_pos, second_door_pos, wall_1_index, wall_2_index)
    
    #On trouve le chemin le plus petit et on en fait un couloir
    path, first_door_pos, second_door_pos, wall_1_index, wall_2_index = min([path, len(path[0]) for path in path_list], axes = 1)[0]
    for coord in path:
        map[coord[0], coord[1]] = 3
        room_1.create_door(first_door_pos, wall_1_index, map)
        room_2.create_door(second_door_pos, wall_2_index, map)

