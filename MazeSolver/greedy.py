
import os
import matplotlib.pyplot as plt

def heuristicFunction(point, end):
    d = (point[0] - end[0])*(point[0] - end[0]) + (point[1] - end[1])*(point[1] - end[1])
    return d

def heapify(queue, index,end):
    length = len(queue)
    while (index < int(length / 2)):
        childIdx = 2 * index + 1
        if (childIdx < length - 1):
            if(heuristicFunction(queue[childIdx + 1],end) < heuristicFunction(queue[childIdx],end)):
                childIdx += 1
        if (heuristicFunction(queue[index], end) <= heuristicFunction(queue[childIdx], end)):
            break
        queue[index],queue[childIdx] = queue[childIdx], queue[index]
        index = childIdx

def reverseHeapify(queue,index,end):
    while index > 0:
        farIdx = int((index - 1)/2)
        if (heuristicFunction(queue[farIdx], end) > heuristicFunction(queue[index], end)):
            queue[index],queue[farIdx] = queue[farIdx], queue[index]
        else:
            break
        index = farIdx

def insert(queue, value, end):
    queue.append(value)
    reverseHeapify(queue,len(queue) - 1, end)

def pop(queue, end):
    result = queue[0]
    queue[0] = queue[len(queue) - 1]
    queue.pop()
    heapify(queue, 0, end)
    return result

def greedy(matrix,start,end):

    result = [] #Mang chua ket qua
    queue = []
    cost = -1
    openList = []
    
    rows = len(matrix) #So dong
    columns = len(matrix[0]) #So cot
    numNode = rows * columns 
    visited = [0 for i in range(0,numNode) ]
    privious = [(-1,-1) for i in range(0,numNode) ]

    insert(queue,start,end)
    openList.append(start)
    while len(queue) != 0:

        parent = pop(queue, end)
        visited[parent[0] * columns + parent[1]] = 1

        if parent == end:
            result.append(end)

            while parent != start:
                parent = privious[parent[0] * columns + parent[1]]
                result.append(parent)

            result.reverse()
            cost = len(result) - 1
            return [openList, result]

        for i in range(-1,1): #4 huong len, xuong, trai, phai 
            for j in range(0,2):

                x = parent[0] + i + (j % 2)
                y = parent[1] + i + ((j + 1) % 2)
                
                if (x >= 0) and (x < rows) and (y >= 0) and (y < columns):
                    index = x * columns + y
                    if(matrix[x][y] == ' 'or matrix[x][y] == '+') and (visited[index] == 0):
                        insert(queue,(x,y),end)
                        privious[index] = parent
                        openList.append((x,y))
    
    result.clear()
    return [openList, result]

#[result,openList,cost] = greedy(matrix,start,end)
#print(result)
#print(cost)
#print(openList)
#visualize_maze(matrix,start,end,result)