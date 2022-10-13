import queue
from setupData import *
from mazeDrawing import *

def QuickSort(array, previous, sortBy='TotalCost'): # QuickSort (python version)
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = previous[array[0]][sortBy]
        for elem in array:
            cost = previous[elem][sortBy]
            if cost < pivot:
                less.append(elem)
            if cost == pivot:
                equal.append(elem)
            if cost > pivot:
                greater.append(elem)
        return QuickSort(less, previous, sortBy) + equal + QuickSort(greater, previous, sortBy)
    else:  
        return array

def resultConverter(previous, start, goal, isRoutable):
  currentPoint = goal
  
  converter = pointNameToPointConverter(currentPoint, "_")
  point = (int(converter["x"]), int(converter["y"]))
  
  route = [point]

  if (isRoutable):
    while currentPoint != start:
      currentPoint = previous[currentPoint]['from']
      
      converter = pointNameToPointConverter(currentPoint, "_")
      point = (int(converter["x"]), int(converter["y"]))

      route = [point] + route

  return route

def UCS(matrix, start, goal):
  setupAdjacencyList(matrix)
  from GlobalCache import adjacencyList

  isRoutable = False
  start = pointToPointNameConverter(start)
  goal = pointToPointNameConverter(goal)
  route = []

  q = queue.deque()
  q.append(start)

  previous = [] 
  for point in adjacencyList.keys():
    previous.append((point, {'from': None, 'TotalCost': 0}))
  previous = dict(previous)

  counter = 0
  while 1:
    counter += 1
    curPoint = q.popleft() 

    curPointTotalCost = previous[curPoint]['TotalCost']
    
    if curPoint != goal:
      for point in adjacencyList[curPoint].keys(): 
        cityTotalCost = previous[point]['TotalCost']
        totalCost = adjacencyList[curPoint][point]['cost'] + curPointTotalCost
        
        if previous[point]['from'] == None or totalCost < cityTotalCost :
          if q.count(point) != 0: 
            q.remove(point)
          q.append(point) 
          previous[point]['from'] =  curPoint
          previous[point]['TotalCost'] = totalCost 
    else:
      isRoutable = True
    
    if len(q) == 0: break
    q = queue.deque(QuickSort(q, previous)) 

  route = resultConverter(previous, start, goal, isRoutable)
  return route

  