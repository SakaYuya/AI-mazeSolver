from pickle import FALSE, TRUE
from re import search
import matplotlib.pyplot as plt
import math

class Node:
    def __init__(self, point, g, h, parent = None):
        self.point = point
        self.g = g
        self.h = h
        self.parent = parent

    def __gt__(self, other):
        return (self.g + self.h) > (other.g + other.h)

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __ge__(self, other):
        return (self.g + self.h) >= (other.g + other.h)

    def __le__(self, other):
        return (self.g + self.h) <= (other.g + other.h)

#Calculate the distant from point a to point b
def dis(a, b) -> int:
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

# Priority Queue
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    # heapify
    def heapify(self, index):
        length = len(self)
        while (index < int(length / 2)):
            childIdx = 2 * index + 1
            if (childIdx < length - 1):
                if(self.get(childIdx + 1) < self.get(childIdx)):
                    childIdx += 1
            if (self.get(index) <= self.get(childIdx)):
                break
            self.swap(index, childIdx)
            index = childIdx
    
    # use for insert
    def reverseHeapify(self,index):
        while index > 0:
            farIdx = int((index - 1)/2)
            if (self.get(farIdx) > self.get(index)):
                self.swap(farIdx, index)
            else:
                break
            index = farIdx
 
    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)
        self.reverseHeapify(len(self) - 1)

    def pop(self):
        result = self.get(0)
        self.swap(0, len(self)-1)
        self.queue.pop()
        self.heapify(0)
        return result
 
    # for popping an element based on Priority
    # def pop(self):
        # try:
        #     min_val = 0
        #     for i in range(len(self.queue)):
        #         if self.queue[i] < self.queue[min_val]:
        #             min_val = i
        #     item = self.queue[min_val]
        #     del self.queue[min_val]
        #     return item
        # except IndexError:
        #     print()
        #     exit()

    def __len__(self):
        return len(self.queue)

    def get(self, i):
        return self.queue[i]

def aStar(matrix, start, end):
    #Initialize
    g = 0
    h = dis(start, end)
    searchPath = []
    resultPath = []
    
    #Open priority queue
    openList = PriorityQueue()
    openList.push(Node(start, g, h, start))    

    #Create priority queue to save closed node
    closedList = PriorityQueue()

    #Find the next node
    while not openList.isEmpty():
        #Get node has the lowest distance to end point
        curNode = openList.pop()
        searchPath.append(curNode.point)
        #Move curNode to closed list
        closedList.push(curNode)
        #Check all node that reachable from curNode
        for i in range(0,4):
            nextPoint = (0,0)
            if i==0 and curNode.point[0]>0:
                nextPoint = (curNode.point[0]-1, curNode.point[1])
            elif i==1 and curNode.point[1]>0:
                nextPoint = (curNode.point[0], curNode.point[1]-1)
            elif i==2 and curNode.point[0]<len(matrix)-1:
                nextPoint = (curNode.point[0]+1, curNode.point[1])
            elif i==3 and curNode.point[1]<len(matrix[0])-1:
                nextPoint = (curNode.point[0], curNode.point[1]+1)
            else:
                continue

            #Check if next point is path
            if(matrix[nextPoint[0]][nextPoint[1]]!=' '):
                continue
            
            #Check if next point is in closed list
            check: bool = False 

            for i in range(0,len(closedList)):
                if closedList.get(i).point == nextPoint:
                    check = True
                    break  

            if check: continue            

            #Check if next point is in open list  
            check = False   
            index = -1    
            temp_g = curNode.g + 1
            temp_h = dis(nextPoint, end)
            tempNode = Node(nextPoint, temp_g, temp_h, curNode)  
            for i in range(0,len(openList)):
                if openList.get(i).point == nextPoint:
                    check = True
                    index = i
                    break

            if not check:                
                openList.push(tempNode)
                #print(nextPoint, temp_g, temp_h, curNode.point)
            else:                
                if openList.get(index) > tempNode:
                    openList.get(index).g = tempNode.g
                    openList.get(index).h = tempNode.h
                    openList.get(index).parent = tempNode.parent

        if curNode.point == end:
            #Get shortest path
            temp = curNode
            while temp != start:
                resultPath.append(temp.point)
                temp = temp.parent
            break
    # for i in range(len(closedList)):
    #     resultPath.append(closedList.get(i).point)
    
    return [searchPath, resultPath]