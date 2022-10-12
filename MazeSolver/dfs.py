from setupData import *
from mazeDrawing import *

def resultConverter(previous, start, goal, isRoutable):
  currentPoint = goal
  converter = pointNameToPointConverter(currentPoint, "_")
  point = (int(converter["x"]), int(converter["y"]))
  route = [point]

  if (isRoutable):
    while currentPoint != start:
      currentPoint = previous[currentPoint]
      converter = pointNameToPointConverter(currentPoint, "_")

      point = (int(converter["x"]), int(converter["y"]))
      route = [point] + route

  return route
  
def DFS(matrix, start, end):
  setupAdjacencyList(matrix)
  from GlobalCache import adjacencyList
  print(start, end)
  start = pointToPointNameConverter(start)
  end = pointToPointNameConverter(end)
  
  # The result variable
  route = []
  
  previous = []
  for point in adjacencyList.keys():
    previous.append((point, None))
  previous = dict(previous)

  def dfs(_start): 
    for point in adjacencyList[_start].keys():
      if previous[point] == None:
        previous[point] = _start
        if point == end:
          return True  
        elif dfs(point):
          return True
    return False
  
  if (dfs(start)):
    isRoutable = True
    route = resultConverter(previous, start, end, isRoutable)
    print('Path was found')
  else:
    print('No path was found')

  return route
