from pickle import FALSE, TRUE
import priorityQueue as pQ
import matplotlib.pyplot as plt

class Node:
    def __init__(self, point, g, h, parent):
        self.point = point
        self.g = g
        self.h = h
        self.parent = parent

    def __gt__(self, other):
        return (self.g + self.h) > (other.g + other.h)

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

#Calculate the distant from point a to point b
def dis(a, b) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def aStar(matrix, start, end):
    #Initialize
    g = 0
    h = dis(start, end)
    res = []
    
    #Open priority queue
    openList = pQ.PriorityQueue()
    openList.push(Node(start, g, h, start))    

    #Create priority queue to save closed node
    closedList = pQ.PriorityQueue()

    #Find the next node
    while not openList.isEmpty():
        #Get node has the lowest distance to end point
        curNode = openList.pop()
        temp_point = curNode.point
        
        #Move curNode to closed list
        closedList.push(curNode)
        #Check all node that reachable from curNode
        for i in range(0,4):
            nextPoint = (0,0)
            if i==0 and curNode.point[0]>0:
                nextPoint = (curNode.point[0]-1, curNode.point[1])
            elif i==1 and curNode.point[1]>0:
                nextPoint = (curNode.point[0], curNode.point[1]-1)
            elif i==2 and curNode.point[0]<len(matrix[0]):
                nextPoint = (curNode.point[0]+1, curNode.point[1])
            elif i==3 and curNode.point[1]>len(matrix):
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
                res.append(temp.point)
                temp = temp.parent
            break

    #Get result
    res.reverse()
    
    return res




            
                


        
