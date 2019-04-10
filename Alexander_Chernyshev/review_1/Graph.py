import random


class Graph:
    height = 0
    width = 0
    vertices = []
    edges = []

    def __init__(self, graph_h, graph_w):
        self.height = graph_h
        self.width = graph_w
        for i in range(graph_h):
            for j in range(graph_w):
                self.vertices.append((i, j))


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


def dfs_generation(graph, start_h=0, start_w=0):
    stack = []
    visited = []
    cells = graph.width * graph.height
    current = (start_h, start_w)
    visited.append(current)

    def get_neighbours(cell):
        nonlocal visited
        y, x = cell
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbours = []
        for i in range(4):
            dx, dy = steps[i]
            if (y+dy, x+dx) in graph.vertices and (y+dy, x+dx) not in visited:
                neighbours.append((y+dy, x+dx))
        return neighbours

    while len(visited) < cells:
        current_neighbours = get_neighbours(current)
        if len(current_neighbours) > 0:
            stack.append(current)
            next_cell = random.choice(current_neighbours)
            graph.edges.append({current, next_cell})
            current = next_cell
            visited.append(current)
        else:
            current = stack.pop()


def kruskal_generation(graph):
    trees = [{x} for x in graph.vertices]
    graph_h = graph.height
    graph_w = graph.width
    edges = []

    for i in range(1, graph_h):
        edges.append({(i - 1, 0), (i, 0)})

    for i in range(1, graph_w):
        edges.append({(0, i - 1), (0, i)})

    for i in range(1, graph_h):
        for j in range(1, graph_w):
            edges.append({(i - 1, j), (i, j)})
            edges.append({(i, j - 1), (i, j)})

    while len(edges) > 0:
        e = random.choice(edges)
        v1 = list(e)[0]
        v2 = list(e)[1]
        t1 = None
        t2 = None
        for t in trees:
            if v1 in t:
                t1 = t
            if v2 in t:
                t2 = t
        if t1 != t2:
            graph.edges.append(e)
            tmp = t1 | t2
            trees.remove(t1)
            trees.remove(t2)
            trees.append(tmp)
        edges.remove(e)
