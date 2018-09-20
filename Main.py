import random

colSize = 10
rowSize = 10

maze = ['W'] * colSize

for i in range(len(maze)):
    maze[i] = ['W'] * colSize


def makeEntry():
    num = random.randint(0, 9)
    maze[num][0] = 'E'
    return str(num) + '0'


def checkBoundaries(x, y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    else:
        return False


def moveRight(col):
    return col + 1


def moveLeft(col):
    return col - 1


def moveUp(row):
    return row + 1


def moveDown(row):
    return row - 1


def getNextMove(row, col):
    num = random.randint(1, 4)

    if num == 1:
        newCol = moveRight(col)
        # maze[row][newCol] = 'P'
        # if newCol >= 9:
        #     return row, col
        # else:
        return row, newCol
    elif num == 2:
        newCol = moveLeft(col)
        # maze[row][newCol] = 'P'
        # if newCol <= 0:
        #     return row, col
        # else:
        return row, newCol
    elif num == 3:
        newRow = moveUp(row)
        # maze[newRow][col] = 'P'
        # if newRow <= 0:
        #     return row, col
        # else:
        return newRow, col
    elif num == 4:
        newRow = moveDown(row)
        # maze[newRow][col] = 'P'
        # if newRow >= 9:
        #     return row, col
        # else:
        return newRow, col


location = makeEntry()
row = int(location[0])
col = int(location[1])

colNum = moveRight(col)

location = str(row) + str(colNum)
row = int(location[0])
col = int(location[1])
maze[row][col] = 'P'

coords = getNextMove(row, col)

while checkBoundaries(row, col):

    if checkBoundaries(row, col):
        try:
            if maze[row][col] != 'E':
                maze[row][col] = 'P'
        except IndexError:
            print('oops')

    coords = getNextMove(row, col)
    row = coords[0]
    col = coords[1]

for row in maze:
    print(' '.join([str(elem) for elem in row]))
