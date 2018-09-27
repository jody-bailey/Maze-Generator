# Jody Bailey
# 09/26/2018
# Artificial Intelligence
# This file contains the class and methods needed for the program to execute.

import random
import os
from pathlib import Path

# Globals for folder path and file path
FOLDER = Path.home()
FILE = os.path.join(FOLDER, 'maze.txt')


class MyMaze:

    # Constructor
    def __init__(self):
        self.colSize = 10
        self.rowSize = 10

    # Variable to track the amount of times the
    # getNextMove() method is called
    recursionCount = 0

    # Method to make the entry of the maze, returns a tuple
    def makeEntry(self, maze):
        num = random.randint(1, 8)
        maze[num][0] = 'E'
        return num, 0

    # Method to check if the current location is within the
    # bounds of the maze
    def checkBoundaries(self, x, y):
        if 0 <= x <= 9 or 0 <= y <= 9:
            return True
        else:
            return False

    # Method to move the current location to the right
    def moveRight(self, row, col, maze, entry=False, check=False):
        # If this method is called for the entry then just add 1 to the column
        if entry:
            return col + 1

        # If move is on the outer perimeter then don't move
        if row < 1 or row > 8 or col < 1 or row > 8:
            return col
        # Make sure the move is not blocked
        elif maze[row - 1][col] == 'P' and maze[row - 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return col
        # Make sure the move is not blocked
        elif maze[row + 1][col] == 'P' and maze[row + 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return col
        # If all checks pass then make the move to the right
        else:
            newCol = col + 1
            # Check the new move and make sure it is not blocked
            if newCol < 1 or newCol > 8:
                return -1
            elif maze[row - 1][newCol] == 'P' and maze[row - 1][newCol + 1] == 'P':
                return -1
            elif maze[row + 1][newCol] == 'P' and maze[row + 1][newCol + 1] == 'P':
                return -1
            else:
                return newCol

    # Method to move current location to the left
    def moveLeft(self, row, col, maze, check=False):
        # Check if new location would be on the perimeter, if so
        # just return current column
        if row < 1 or row > 8 or col < 1 or row > 8:
            return col
        # Make sure the move would not be blocked on the top
        elif maze[row - 1][col] == 'P' and maze[row - 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return col
        # Make sure the move would not be blocked on the bottom
        elif maze[row + 1][col] == 'P' and maze[row + 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return col
        # If the conditions above pass then make the move
        else:
            newCol = col - 1
            # Check the new location to make sure it is not blocked
            if newCol < 1 or newCol > 8:
                return -1
            elif maze[row - 1][newCol] == 'P' and maze[row - 1][newCol - 1] == 'P':
                return -1
            elif maze[row + 1][newCol] == 'P' and maze[row + 1][newCol - 1] == 'P':
                return -1
            else:
                return newCol

    # Method to move the current location up
    def moveUp(self, row, col, maze, check=False):
        # Make sure the new location would not be on the perimeter of the maze
        if row < 1 or row > 8 or col < 1 or row > 8:
            return row
        # Check to see if the new location would be blocked to the left
        elif maze[row][col - 1] == 'P' and maze[row - 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return row
        # Check to see if the new location would be blocked to the right
        elif maze[row][col + 1] == 'P' and maze[row - 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return row
        # If all check above pass then make the move
        else:
            newRow = row - 1
            # Check to make sure the new location is not blocked
            if newRow < 1 or newRow > 8:
                return -1
            elif maze[newRow][col - 1] == 'P' and maze[newRow - 1][col - 1] == 'P':
                return -1
            elif maze[newRow][col + 1] == 'P' and maze[newRow - 1][col + 1] == 'P':
                return -1
            else:
                return newRow

    # Method to move the current location down
    def moveDown(self, row, col, maze, check=False):
        # Check to make sure the new location would not be on the perimeter
        if row < 1 or row > 8 or col < 1 or row > 8:
            return row
        # Make sure the new location would not be blocked on the left
        elif maze[row][col - 1] == 'P' and maze[row + 1][col - 1] == 'P':
            if check:
                return -1
            else:
                return row
        # Make sure the new location would not be blocked on the right
        elif maze[row][col + 1] == 'P' and maze[row + 1][col + 1] == 'P':
            if check:
                return -1
            else:
                return row
        # If all conditions above pass then make the move
        else:
            newRow = row + 1
            # Make sure the new location is not blocked
            if newRow < 1 or newRow > 8:
                return -1
            elif maze[newRow][col - 1] == 'P' and maze[newRow + 1][col - 1] == 'P':
                return -1
            elif maze[newRow][col + 1] == 'P' and maze[newRow + 1][col + 1] == 'P':
                return -1
            else:
                return newRow

    # Method to find an exit point for the maze
    def exit(self, row, col, maze):
        # If current position is the row below the top,
        # set the position above it with an 'X' for the exit point
        if row == 1:
            maze[row - 1][col] = 'X'
        # If current position is the row above the bottom,
        # set the position below it with an 'X' for the exit point
        elif row == 8:
            maze[row + 1][col] = 'X'
        # If current position is the column to the left of the far right,
        # set the position to the right with an 'X' for the exit point
        elif col == 8:
            maze[row][col + 1] = 'X'
        # Else, search along the edges to see which edges contain the letter 'P'.
        # Store their location values in lists and randomly choose which list to use
        # to choose the exit point from. Then from within that list randomly choose
        # which point to exit from.
        else:
            first = []
            second = []
            third = []

            # Find all 'P' values in the second row
            for i in range(self.colSize):
                if maze[1][i] == 'P':
                    first.append((1, i))

            # Find all 'P' values in the ninth row
            for i in range(self.colSize):
                if maze[8][i] == 'P':
                    second.append((8, i))

            # Find all 'P' values in the ninth column
            for i in range(self.colSize):
                if maze[i][8] == 'P':
                    third.append((i, 8))

            done = False
            while not done:
                # Get a random number
                num = random.randint(1, 3)

                # Use the random number to determine what code gets ran
                if num == 1:
                    '''first'''
                    # Make sure the list contains at least one value
                    if len(first) != 0:
                        done = True
                        # Generate another random number between 0 and the size of the list
                        anotherNum = random.randint(0, len(first) - 1)
                        # Use this random number to get that index of the list
                        coords = first[anotherNum]
                        # Set this position to the exit point
                        maze[0][coords[1]] = 'X'
                elif num == 2:
                    '''second'''
                    # Make sure the list contains at least one value
                    if len(second) != 0:
                        done = True
                        # Generate another random number between 0 and the size of the list
                        anotherNum = random.randint(0, len(second) - 1)
                        # Use this number to get that index of the list
                        coords = second[anotherNum]
                        # Set this position to the exit point
                        maze[9][coords[1]] = 'X'
                elif num == 3:
                    '''third'''
                    # Make sure the list contains at least one value
                    if len(third) != 0:
                        done = True
                        # Generate another random number between 0 and the size of the list
                        anotherNum = random.randint(0, len(third) - 1)
                        # Use this number to get that index of the list
                        coords = third[anotherNum]
                        # Set this position to the exit point
                        maze[coords[0]][9] = 'X'

    # Method to save the file to the user directory
    def saveFile(self, maze):
        # Open the file
        file = open(FILE, 'w')

        # Perform for loop to write to the file
        for i in range(self.rowSize):
            for j in range(self.colSize):
                file.write(maze[i][j] + '\n')

        # Close the file
        file.close()

        print('File saved at location: {}'.format(file.name))

    # Method to get the next move. A random number is generated and used to determine
    # which block of code is ran. Depending on the block of code that is selected,
    # the program will try to move that particular direction. If unsuccessful, it
    # will call itself using recursion until it finds a valid move or the recursion
    # count gets to 20. Then the method return a tuple of x, y coordinates
    def getNextMove(self, row, col, maze):
        # Generate a random number
        num = random.randint(1, 4)

        # Check to see if we can move anywhere. If not then return the current row and column
        if self.moveRight(row, col, maze, False, True) == -1 and self.moveLeft(row, col, maze, True) == -1 and \
                self.moveUp(row, col, maze, True) == -1 and self.moveDown(row, col, maze, True) == -1:
            return row, col

        if self.recursionCount == 20:
            return -1, -1

        if num == 1:
            newCol = self.moveRight(row, col, maze)

            if newCol == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newCol):
                return row, newCol
            if maze[row][newCol] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return row, newCol
        elif num == 2:
            newCol = self.moveLeft(row, col, maze)

            if newCol == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newCol):
                return row, newCol
            if maze[row][newCol] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return row, newCol
        elif num == 3:
            newRow = self.moveUp(row, col, maze)

            if newRow == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newRow):
                return row, newRow
            if maze[newRow][col] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return newRow, col
        elif num == 4:
            newRow = self.moveDown(row, col, maze)

            if newRow == -1:
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            if not self.checkBoundaries(row, newRow):
                return row, newRow
            if maze[newRow][col] == 'P':
                self.recursionCount += 1
                return self.getNextMove(row, col, maze)
            else:
                return newRow, col
