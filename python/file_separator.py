'''
Purpose: to separate the maze.py textfile into 4 separate parts:
1. Textures and their locations
2. Length and width of the maze
3. The maze itself
4. The correct path

Why?
We want to read these in using Unreal Engine blueprints, and I'd 
rather do the coding here than there. This way, it's easier to separate 
these values and feed them into the appropriate locations. 

'''
import sys  # we'll need to read in CLI arguments


def processFile(filename: str = './maze.txt'):
    '''
    Takes in a file and produces 4 files:
    1. Textures and their locations
    2. Length and width of the maze
    3. The maze itself
    4. The correct path 

    Inputs:
    - filename = path of the file to be processed
        by default, assumes maze file is in same directory
    '''
    f = open(filename, 'r')  # open in read only mode - we don't need to edit

    # the first line tells us how many textures we need to load in
    numTextures = f.readline()

    # now let's put all the textures into a file
    textures = open('output/textures.txt', 'w')
    textures.write(numTextures)

    for i in range(0, int(numTextures)):
        # writes all textures into the textures file
        textures.write(f.readline())

    textures.close()

    # now we read in the dimensions
    dim_list = f.readline().split(" ")
    (cols, rows) = int(dim_list[0]), int(dim_list[1])

    # we want one for each so we can turn them into a variable in Unreal
    cols_file = open('output/cols.txt', 'w')
    rows_file = open('output/rows.txt', 'w')

    cols_file.write(str(cols))
    rows_file.write(str(rows))

    cols_file.close()
    rows_file.close()

    # importantly, we have to roll up the maze given into one long line now.
    maze_string = ""
    for i in range(0,  rows):
        maze_string += f.readline()

    # removes end of line tokens, replaces with space
    maze_string = maze_string.replace('\n', ' ')

    # replace with x's for ease of use in Unreal
    maze_string = maze_string.replace(' ', 'x')

    maze = open('output/maze.txt', 'w')
    maze.write(maze_string)
    maze.close()

    # sanity check
    print("maze length = " + str(len(maze_string.split("x"))))
    lenMaze = cols * rows
    print("should be: " + str(lenMaze))

    # now we read the rest of it into the solution file
    solution = open('output/solution.txt', 'w')
    solution.write(f.read())
    f.close()
    print("All done!")


if __name__ == '__main__':
    processFile(sys.argv[1])
