def find_shortest_path(maze, start, end):
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
        for neighbor in get_neighbors(maze, current):
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


def get_neighbors(maze, cell):
    x, y = cell
    neighbors = []
    # Check if the cell above is a valid move
    if x > 0 and maze[x-1][y] == 1:
        neighbors.append((x-1, y))
    # Check if the cell to the right is a valid move
    if y < len(maze[0])-1 and maze[x][y+1] == 1:
        neighbors.append((x, y+1))
    # Check if the cell below is a valid move
    if x < len(maze)-1 and maze[x+1][y] == 1:
        neighbors.append((x+1, y))
    # Check if the cell to the left is a valid move
    if y > 0 and maze[x][y-1] == 1:
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



# print(set(['hello','hello','hi']))

# a = {'fils': 'père'}
# print('fils' in a, 'père' in a)

import maze
A = maze.Maze().new_maze(dimx=50,dimy=50)

def color(m, pos, col) :
    x,y = pos
    xm,ym = m.shape
    if m[pos] == 0 :
        m[pos] = col 
        if x+1<xm :
            color(m, (x+1,y), col)
        if y+1<ym :
            color(m, (x,y+1), col)
        if x-1 >=0 :
            color(m, (x-1,y), col)
        if y-1 >=0 :
            color(m, (x,y-1), col)

def color_group(m) :
    n,p = m.shape
    col = 2
    for i in range(n) :
        for j in range(p) :
            if m[i,j] == 0 :
                color(m, (i,j), col)
                col+=1
    return m

maze = (color_group(A)==2).astype('uint8')
n,p = maze.shape
for i in range(n) :
    for j in range(p):
        if maze[i,j] == 1 :
            start = i,j
        if maze[-i-1,-j-1] == 1 :
            end = n-i-1,p-j-1


path = find_shortest_path(maze, start, end)

if path :
    for pos in path :
        if pos :       #corrige un None (mère de la cellule initiale)
            maze[pos] = 2
else :
    print('pas de chemin possible')



import matplotlib.pyplot as plt
plt.imshow(maze)
plt.colorbar()
plt.show()
plt.close()