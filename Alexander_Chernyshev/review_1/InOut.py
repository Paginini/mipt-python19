from Maze import Maze


def open_maze(file_name):
    f = open(file_name)
    lines = []
    for line in f:
        lines.append(line)
    h, w = map(int, lines[0].split())
    m = Maze(h, w)
    for k in range(1, len(lines)):
        m.field[k-1] = [int(x) for x in lines[k] if x != '\n']
    return m


def write_maze(maze, file_name='output.txt'):
    f = open(file_name, 'w')
    f.write(str(maze.height//2) + ' ' + str(maze.width//2) + '\n')
    for line in maze.field:
        f.write("".join([str(x) for x in line]) + '\n')

