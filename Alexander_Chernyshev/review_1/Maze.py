class Maze:
    height = 0
    width = 0
    field = None

    def __init__(self, maze_h, maze_w):
        self.height = maze_h*2 + 1
        self.width = maze_w*2 + 1
        self.field = [[1] * self.height for i in range(self.width)]
        for i in range(1, self.height, 2):
            for j in range(1, self.width, 2):
                self.field[i][j] = 0


def create_maze(graph):
    maze = Maze(graph.height, graph.width)

    for e in graph.edges:
        edge = list(e)
        f = edge[0]
        s = edge[1]
        wall_x = f[1] + s[1] + 1
        wall_y = f[0] + s[0] + 1
        maze.field[wall_y][wall_x] = 0
    return maze


def print_maze(m):
    for i in range(m.height):
        for j in range(m.width):
            if m.field[i][j] == 1:
                print('X', end=' ')
            elif m.field[i][j] == 2:
                print('.', end=' ')
            else:
                print(' ', end=' ')
        print()


def bfs(m):
    start_point = (1, 1)
    finish_point = (m.height - 2, m.width - 2)

    visited = dict()
    queue = list()

    queue.append(start_point)
    visited[start_point] = 0

    def get_neighbours(point):
        nonlocal visited
        y, x = point
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbours = []
        for i in range(4):
            dx, dy = steps[i]
            if m.field[y+dy][x+dx] == 0 and (y+dy, x+dx) not in visited:
                neighbours.append((y + dy, x + dx))
        return neighbours

    while finish_point not in visited:
        cur_p = queue.pop(0)
        current_neighbours = get_neighbours(cur_p)
        for x in current_neighbours:
            queue.append(x)
            visited[x] = visited[cur_p] + 1

    cur_p = finish_point
    finish_y, finish_x = finish_point
    m.field[finish_y][finish_x] = 2

    while cur_p != start_point:
        y, x = cur_p
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in steps:
            dy, dx = i
            if (y+dy, x+dx) in visited and visited[(y+dy, x+dx)] < visited[cur_p]:
                cur_p = (y + dy, x + dx)
                m.field[y + dy][x + dx] = 2
                break

