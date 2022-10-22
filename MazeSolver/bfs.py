def route(result,pointIndex,columns):
    x = int(pointIndex / columns)
    y = int(pointIndex % columns)
    result.append((x,y))


def bfs(matrix,start,end):

    result = [] #Mang chua ket qua
    openList = []
    cost = -1

    rows = len(matrix) #So dong
    columns = len(matrix[0]) #So cot
    numNode = rows * columns 

    visited = [-2 for i in range(0,numNode) ]
    queue = []

    #Xem ma tran la mang 1 chieu danh so tu 0 den (n*n -1) de xu ly

    startIndex = int(start[0] * columns + start[1]); 
    endIndex = int(end[0] * columns + end[1]);

    queue.append(startIndex);
    visited[startIndex]= -1;
    openList.append(start)

    while len(queue) != 0:

        parent = queue.pop(0)

        if parent == endIndex:
            route(result,endIndex,columns)

            while parent != -1:
                parent = visited[parent]
                if parent != -1:
                    route(result,parent,columns)

            result.reverse()
            cost = len(result) - 1
            return [openList, result]

        for i in range(-1,1): #4 huong len, xuong, trai, phai 
            for j in range(0,2):

                x = int(parent / columns) + i + (j % 2)
                y = int(parent % columns) + i + ((j + 1) % 2)
                
                if (x >= 0) and (x < rows) and (y >= 0) and (y < columns):
                    index = x * columns + y
                    if matrix[x][y] != 'x' and  visited[index] == -2 :
                        queue.append(index)
                        visited[index] = parent;
                        openList.append((x,y))
    
    result.clear()
    return [openList, result]


#[result,openList,cost] = bfs(matrix,start,end)
#print(result)
#print(cost)