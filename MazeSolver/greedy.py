import os
import matplotlib.pyplot as plt

def heuristicFunction1(point, end):
    d = (point[0] - end[0])*(point[0] - end[0]) + (point[1] - end[1])*(point[1] - end[1])
    return d

def heuristicFunction2(point,end):
    d = abs(point[0] - end[0]) + abs(point[1] - end[1]) 
    return d

def heuristicFunction(point,end,option):
    d = 0.0
    if option == 1:
        d = heuristicFunction1(point,end)
    else: 
        if option == 2:
            d = heuristicFunction2(point,end)
    return d 

def heapify(queue, index,end,option):
    length = len(queue)
    while (index < int(length / 2)):
        childIdx = 2 * index + 1
        if (childIdx < length - 1):
            if(heuristicFunction(queue[childIdx + 1],end,option) < heuristicFunction(queue[childIdx],end,option)):
                childIdx += 1
        if (heuristicFunction(queue[index], end,option) <= heuristicFunction(queue[childIdx], end,option)):
            break
        queue[index],queue[childIdx] = queue[childIdx], queue[index]
        index = childIdx

def reverseHeapify(queue,index,end,option):
    while index > 0:
        farIdx = int((index - 1)/2)
        if (heuristicFunction(queue[farIdx], end,option) > heuristicFunction(queue[index], end,option)):
            queue[index],queue[farIdx] = queue[farIdx], queue[index]
        else:
            break
        index = farIdx

def insert(queue, value, end,option):
    queue.append(value)
    reverseHeapify(queue,len(queue) - 1, end,option)

def pop(queue, end, option):
    result = queue[0]
    queue[0] = queue[len(queue) - 1]
    queue.pop()
    heapify(queue, 0, end,option)
    return result

def greedy(matrix,start,end,heuristicOption):

    result = [] #Mang chua ket qua
    queue = []
    openList = []
    
    rows = len(matrix) #So dong
    columns = len(matrix[0]) #So cot
    numNode = rows * columns 
    visited = [0 for i in range(0,numNode) ]
    privious = [(-1,-1) for i in range(0,numNode) ]

    insert(queue,start,end,heuristicOption)
    openList.append(start)
    while len(queue) != 0:

        parent = pop(queue, end,heuristicOption)
        visited[parent[0] * columns + parent[1]] = 1

        if parent == end:
            result.append(end)

            while parent != start:
                parent = privious[parent[0] * columns + parent[1]]
                result.append(parent)

            result.reverse()
            return [result,openList]

        for i in range(-1,1): #4 huong len, xuong, trai, phai 
            for j in range(0,2):

                x = parent[0] + i + (j % 2)
                y = parent[1] + i + ((j + 1) % 2)
                
                if (x >= 0) and (x < rows) and (y >= 0) and (y < columns):
                    index = x * columns + y
                    if(matrix[x][y] == ' 'or matrix[x][y] == '+') and (visited[index] == 0):
                        insert(queue,(x,y),end,heuristicOption)
                        privious[index] = parent
                        openList.append((x,y))
    
    result.clear()
    return [result,openList]
