import sys
from Graph import Graph, dfs_generation, kruskal_generation
from Maze import Maze, create_maze, print_maze, bfs
from InOut import open_maze, write_maze

algo = int(sys.argv[1])


def main(algo):
    print('New/load ? n / l')
    ans = input()
    if ans == 'n':
        input_message = "Enter the size of your maze (height x width)\n"
        maze_height, maze_width = map(int, input(input_message).split())
        graph = Graph(maze_height, maze_width)
        if algo == 1:
            dfs_generation(graph)
            print("Generating with DFS...")
        elif algo == 2:
            kruskal_generation(graph)
            print("Generating with Kruskal algorithm")
        m = create_maze(graph)
        print_maze(m)
        print('Would you like to save it? y/n')
        ans = input()
        if ans == 'y':
            write_maze(m)
    else:
        print('Enter file name')
        file = input()
        m = open_maze(file)
    print('Would you like to solve it? y/n')
    ans = input()
    if ans == 'y':
        bfs(m)
        print_maze(m)


main(algo)
