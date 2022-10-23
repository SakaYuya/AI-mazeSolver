import mazeDrawing as mD
import dfs
import bfs
import ucs
import greedy
import A_star
import matplotlib.pyplot as plt

def main():
    for k in '12345':
        #Get matrix
        inputFile = '/level_1/input' + k
        matrix = mD.read_file('input' + inputFile + '.txt')

        start = [0,0]
        end = [0,0]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='S':
                    start=(i,j)

                elif matrix[i][j]==' ':
                    if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                        end=(i,j)
                        
                else:
                    pass


        #DFS        
        ax=plt.figure()
        res = dfs.DFS(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/dfs',res)

        # BFS
        ax=plt.figure()
        res = bfs.bfs(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/bfs',res)

        # UCS
        ax=plt.figure()
        res = ucs.UCS(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/ucs',res)

        # Greedy 1
        ax=plt.figure()
        res = greedy.greedy(matrix, start, end, 1)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/gbfs1',res)

        # Greedy 2
        ax=plt.figure()
        res = greedy.greedy(matrix, start, end, 1)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/gbfs2',res)

        # A* with first heuristic
        ax=plt.figure()
        res = A_star.aStar(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/astar1',res)

        # A* with second heuristic
        ax=plt.figure()
        res = A_star.aStar(matrix, start, end, 1)
        mD.visualize_maze(ax, matrix,start,end, 'output' + inputFile + '/astar2',res)

main()