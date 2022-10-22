import queue
from sqlite3 import converters
from setupData import *
from mazeDrawing import *

def QuickSort(array, previous, sortBy='TotalCost'):
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
  else:
    route = []

  return route

def UCS(matrix, start, goal):
  visited = []

  setupAdjacencyList(matrix)
  from GlobalCache import adjacencyList

  isRoutable = False
  start = pointToPointNameConverter(start)
  goal = pointToPointNameConverter(goal)
  route = []
  visited = []

  q = queue.deque()
  q.append(start)

  previous = [] 
  for point in adjacencyList.keys():
    previous.append((point, {'from': None, 'TotalCost': 0}))
  previous = dict(previous)

  while 1:
    curPoint = q.popleft() 

    converter = pointNameToPointConverter(curPoint, '_')
    converter = (int(converter['x']), int(converter['y']))
    if (curPoint not in visited):
      visited.append(converter)
    
    preCurPointTotalCost = previous[curPoint]['TotalCost']
    
    if curPoint != goal:
      for point in adjacencyList[curPoint].keys(): 
        prePointTotalCost = previous[point]['TotalCost']
        totalCost = adjacencyList[curPoint][point]['cost'] + preCurPointTotalCost
        
        if previous[point]['from'] == None or totalCost < prePointTotalCost:
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
  return [visited, route]

  