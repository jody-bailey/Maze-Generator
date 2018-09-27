# Jody Bailey
# 09/26/2018
# Artificial Intelligence
# This program is used to generate random mazes. It creates a single entry point, 'E', along
# the left side of the maze and randomly creates a path to one of the other three
# walls. Once it is complete, it places an 'X' to mark the exit point. Then the maze is
# saved into a text file in the user directory.

from subpackage.MazeGen import MyMaze

# Initialize a list with 10 chars 'W'
maze = ['W'] * 10

# Perform a for loop to set each element of the list as another list
# to make it 2D
for i in range(len(maze)):
    maze[i] = ['W'] * 10

# Create an instance of the MyMaze class
test = MyMaze()

# Initialize path variable to an empty list
path = []

# Set the location to what the method makeEntry() returns
location = test.makeEntry(maze)
# Set the row and col variables from location variable
# location variable is a tuple
row = location[0]
col = location[1]

# Move to the right to enter the maze
colNum = test.moveRight(row, col, maze, True)

# Update the location
location = (row, colNum)
row = location[0]
col = location[1]

# Set the current location data as 'P' for path
maze[row][col] = 'P'

# Add this location to the path
path.append((row, col))

# Get the next move by calling the getNextMove() method
coords = test.getNextMove(row, col, maze)
row = coords[0]
col = coords[1]

# Add this new location to the path
path.append(coords)

# Variable to keep track of the previous location
previous = 0, 0

# Variable to keep track of the attempts to make a move
attempts = 0

# Perform while loop, keep running until conditions inside
# the loop cause it to break out
while 1:

    # Check the current location and make sure it is inside the
    # bounds of the maze. (returns true if inside bounds)
    if test.checkBoundaries(row, col):
        try:
            # If current location is not marked with 'E' or 'P'
            # then mark it with a 'P'
            if maze[row][col] != 'E' and maze[row][col] != 'P':
                maze[row][col] = 'P'
        except IndexError:
            test.exit(row, col, maze)
            break

    # Check if coords are the same from the last run,
    # if they are then add one to attempts
    if coords == previous:
        attempts += 1
    else:
        # reset attempts
        attempts = 0

    # If attemps reach 20 then find an exit point in the maze
    # and break out of the loop
    if attempts == 20:
        test.exit(row, col, maze)
        break

    # Update previous location
    previous = coords

    # Get the next location
    coords = test.getNextMove(row, col, maze)
    # Reset recursion count for the MyMaze class (getNextMove() method)
    test.recursionCount = 0

    # If getNextMove() returns -1 for either x or y then pop the path
    # to go backwards to try another path
    if coords[0] == -1 or coords[1] == -1:
        if len(path) > 0:
            coords = path.pop()
            row = coords[0]
            col = coords[1]
        else:
            test.exit(row, col, maze)
            break
    # Else add the new location to the path and update row and column
    else:
        path.append(coords)
        row = coords[0]
        col = coords[1]


# Print the maze to the screen
print()
for row in maze:
    print(' '.join([str(elem) for elem in row]))
print()
# Save the maze in a text file named maze.txt in the user directory
# C:\Users\{user}\maze.txt
test.saveFile(maze)
