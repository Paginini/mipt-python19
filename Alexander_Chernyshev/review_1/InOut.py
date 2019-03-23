from Maze import *


def open_maze(file_name):
    f = open(file_name)
    h, w = map(int, f.read(4).split())
    m = Maze(h, w)
    i = 0
    for line in f:
        m.field[i] = [int(x) for x in line if x != '\n']
        i += 1
    return m


def write_maze(maze, file_name='output.txt'):
    f = open(file_name, 'w')
    f.write(str(maze.height//2) + ' ' + str(maze.width//2) + '\n')
    for line in maze.field:
        f.write("".join([str(x) for x in line]) + '\n')
