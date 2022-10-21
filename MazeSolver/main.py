import mazeDrawing as mD
import bfs
import greedy
import A_star
import matplotlib.pyplot as plt

def main():
    ax=plt.figure()

    #Get matrix
    matrix = mD.read_file('input/level_1/input1.txt')

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


    # # DFS
    # res = dfs.DFS(matrix, start, end)
    # for i in range(len(res)):
    #     print(res[i])

    # #mD.visualize_maze(matrix,start,end, "DFS",res)    
    # dfs.showResult()

    # BFS
    res = bfs.bfs(matrix, start, end)
    mD.visualize_maze(ax, matrix,start,end, "output/bfs",res)

    # #Greedy
    # res = greedy.greedy(matrix, start, end)
    # mD.visualize_maze(matrix,start,end, "output/greedy",res)

    # #A*
    # res = A_star.aStar(matrix, start, end)
    # mD.visualize_maze(matrix,start,end, "output/A_star",res)

main()