import mazeDrawing as mD
import bfs
import greedy
import A_star
import dfs
import ucs

def main():
    #Get matrix
    matrix = mD.read_file('maze.txt')

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

    # BFS
    res = bfs.bfs(matrix, start, end)
    mD.visualize_maze(matrix,start,end, "output/bfs",res)

    #Greedy
    res = greedy.greedy(matrix, start, end)
    mD.visualize_maze(matrix,start,end, "output/greedy",res)

    #A*
    res = A_star.aStar(matrix, start, end)
    mD.visualize_maze(matrix,start,end, "output/A_star",res)

    #DFS
    res = dfs.DFS(matrix, start, end)[1]
    mD.visualize_maze(matrix,start,end, "output/dfs",res)

    #UCS
    res = ucs.UCS(matrix, start, end)[1]
    mD.visualize_maze(matrix,start,end, "output/ucs",res)

main()