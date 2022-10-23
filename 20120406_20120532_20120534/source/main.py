from imp import reload
import mazeDrawing as mD
import dfs
import bfs
import ucs
import greedy
import A_star
import matplotlib.pyplot as plt
import sys

def main():
    mainFileNameLen = len("/source/main.py")
    _SH_FILE_DIR_ = sys.argv[0] # .../source/main.py
    
    # folder contain "run.sh" (no '/' character at the end)
    _SH_FILE_DIR_ = _SH_FILE_DIR_[:-mainFileNameLen]

    with open(f'{_SH_FILE_DIR_}/source/dir.py', 'w') as file:
        file.write(f'_SH_FILE_DIR_ = "{_SH_FILE_DIR_}"')

    import dir
    reload(dir)

    outputDir = f'{dir._SH_FILE_DIR_}/output'

    with open(f'{_SH_FILE_DIR_}/level1_InputFilenames.txt') as f:
        level1_InputFilenames = f.readlines()

    with open(f'{_SH_FILE_DIR_}/level2_InputFilenames.txt') as f:
        level2_InputFilenames = f.readlines()
    
    with open(f'{_SH_FILE_DIR_}/advance_InputFilenames.txt') as f:
        advance_InputFilenames = f.readlines()
    
    level1_InputFilenames = [filename[:-1] for filename in level1_InputFilenames]
    level2_InputFilenames = [filename[:-1] for filename in level2_InputFilenames]
    advance_InputFilenames = [filename[:-1] for filename in advance_InputFilenames]

    for inputFileName in level1_InputFilenames:
        minimalInputFileName = inputFileName.split('/')[-1].split('.txt')[0]

        #Get matrix
        matrix = mD.read_file(inputFileName)

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


        # #DFS
        
        # ax=plt.figure()
        # res = dfs.DFS(matrix, start, end)
        # mD.visualize_maze(ax, matrix,start,end, outputDir + '/level_1/' + minimalInputFileName + '/dfs',res)

        # BFS
        ax=plt.figure()
        res = bfs.bfs(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, outputDir + '/level_1/' + minimalInputFileName + '/bfs',res)

        # # UCS
        # ax=plt.figure()
        # res = ucs.UCS(matrix, start, end)
        # mD.visualize_maze(ax, matrix,start,end, outputDir + '/level_1/' + minimalInputFileName + '/ucs',res)

        # Greedy
        ax=plt.figure()
        res = greedy.greedy(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, outputDir + '/level_1/' + minimalInputFileName + '/Greedy',res)

        #A*
        ax=plt.figure()
        res = A_star.aStar(matrix, start, end)
        mD.visualize_maze(ax, matrix,start,end, outputDir + '/level_1/' + minimalInputFileName + '/A_star',res)

main()