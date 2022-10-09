def bfs(matrix,start,end):

    result = [] #Mang chua ket qua

    rows = len(matrix) #So dong
    columns = len(matrix[0]) #So cot
    numNode = rows * columns 

    visited = [-2 for i in range(0,numNode) ]
    queue = []

    #Xem ma tran la mang 1 chieu danh so tu 0 den (n*n -1) de xu ly

    startIndex = start[0] * columns + start[1]; 
    endIndex = end[0] * columns + end[1];

    queue.append(startIndex);
    visited[startIndex]= -1;

    while len(queue) != 0:

        parent = queue.pop()
        
        if parent == endIndex:
            
            while parent != startIndex:

                parent = visited[parent]
                if parent != startIndex:
                    x = int(parent / columns)
                    y = int(parent % columns)

                    result.append([x,y])
            
            return result

        for i in range(-1,1): #4 huong len, xuong, trai, phai
            
            for j in range(0,2):

                x = int(parent / columns) + i + (j % 2)
                y = int(parent % columns) + i + ((j + 1) % 2)
                
                if (x >= 0) and (x < rows) and (y >= 0) and (y < columns):
                    index = x * columns + y
                    if matrix[x][y] != 'x' and  visited[index] == -2 :
                        queue.append(index)
                        visited[index] = parent;
    
    return result