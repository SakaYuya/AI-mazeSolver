from cmath import sqrt
import os
from pydoc import doc
import matplotlib.pyplot as plt
import drawPath

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

def visualize_maze(fig, matrix, bonus, start, end, filename, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']
    # if route:
    #     direction=[]
    #     for i in range(1,len(route)):
    #         if route[i][0]-route[i-1][0]>0:
    #             direction.append('v') #^
    #         elif route[i][0]-route[i-1][0]<0:
    #             direction.append('^') #v        
    #         elif route[i][1]-route[i-1][1]>0:
    #             direction.append('>')
    #         else:
    #             direction.append('<')

    #     direction.pop(0)

    #2. Drawing the map
    # ax=plt.figure(dpi=100).add_subplot(111)

    # for i in ['top','bottom','right','left']:
    #     ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')

    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
               marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    # if route:
    #     for i in range(len(route)-2):
    #         plt.scatter(route[i+1][1],-route[i+1][0],
    #                     marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])

    #Get output
    file = open(filename + ".txt", "w")
    file.write(str(route[2]))

    file.close()

    # Draw search path and result
    drawPath.drawRoute(ax, route, filename)

    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus):
       print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


def read_file(file_name: str = 'maze.txt'):
  f=open(file_name,'r')
  n_bonus_points = int(next(f)[:-1])
  bonus_points = []
  for i in range(n_bonus_points):
    x, y, reward = map(int, next(f)[:-1].split(' '))
    bonus_points.append((x, y, reward))

  text=f.read()
  matrix=[list(i) for i in text.splitlines()]
  f.close()

  return (matrix,bonus_points)


(matrix,bonus_points) = read_file('input/input3.txt')

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

def route(result,pointIndex,columns):
    x = int(pointIndex / columns)
    y = int(pointIndex % columns)
    result.append([x,y])


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
            return [result,openList,cost]

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
    return [result,openList,cost]



print(bonus_points)
def distance(a,b):
    result = ((a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]))**0.5
    return result

def choose_bonus_points(start,end,bonus_points,visited):
    d1 = distance(start,end)
    result = end
    min = -1
    for i in range(0,len(bonus_points)):
        if(visited[i] == 0):
            point = (bonus_points[i][0],bonus_points[i][1])
            d2 = distance(start,point) + distance(point,end) + bonus_points[i][2]
            if (d2 < d1):
                d1 = d2
                result = point
                min = i
    if(min != -1):
        visited[min] = 1
    return result

def search(matrix,bonus_points,start,end):
    length_bonus = len(bonus_points)
    visited_bonus = [0 for i in range(0,length_bonus)]
    result = []
    openList =[]
    temp_start= start
    toContinue = True
    cost = -1
    [result,openList,cost] = greedy(matrix,start,end)
    if cost != -1:
        cost = -1
        openList.clear()
        result.clear()
        result.append((-1,-1))

        while(toContinue):
            temp_end = choose_bonus_points(temp_start,end,bonus_points,visited_bonus)
            [temp_result,temp_openList,cost] = greedy(matrix,temp_start,temp_end)

            for i in range(0,len(temp_openList)):
                openList.append(temp_openList[i])

            result.pop()
            for i in range(0,len(temp_result)):
                result.append(temp_result[i])
            temp_start = temp_end
            if(result[len(result) - 1] == end):
                cost = len(result) - 1
                for i in range(0,len(visited_bonus)):
                    if visited_bonus[i] == 1:
                        cost += bonus_points[i][2]
                toContinue = False


    return [openList, result,cost]

result = search(matrix,bonus_points,start,end)
# print(result)
# print(cost)
# print(openList)
ax = plt.figure()
visualize_maze(ax,matrix,bonus_points,start,end,'output/level_2/input3/greedy',result)