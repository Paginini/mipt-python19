import sys
from Graph import *
from InOut import *

algo = int(sys.argv[1])


def main(algo):
    print('New/load ? n / l')
    ans = input()
    if ans == 'n':
        maze_height, maze_width = map(int, input("Enter the size of your maze (height x width)\n").split())
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
