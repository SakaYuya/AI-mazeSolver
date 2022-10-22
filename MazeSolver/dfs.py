from lib2to3.pytree import convert
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
  else:
    route = []
    
  return route
  
def DFS(matrix, start, end):
  setupAdjacencyList(matrix)
  
  import GlobalCache
  reload(GlobalCache)
  adjacencyList = GlobalCache.adjacencyList

  start = pointToPointNameConverter(start)
  end = pointToPointNameConverter(end)

  route = []
  
  previous = []
  for point in adjacencyList.keys():
    previous.append((point, None))
  previous = dict(previous)

  visited = []
  visitedConverter = pointNameToPointConverter(start, '_')
  visited.append((int(visitedConverter['x']), int(visitedConverter['y'])))
  
  def dfs(_start): 
    for point in adjacencyList[_start].keys():
      if previous[point] == None:
        visitedConverter = pointNameToPointConverter(point, '_')
        visited.append((int(visitedConverter['x']), int(visitedConverter['y'])))
        previous[point] = _start
        if point == end:
          return True  
        elif dfs(point):
          return True
    return False
  
  if (dfs(start)):
    isRoutable = True
    route = resultConverter(previous, start, end, isRoutable)

  return [visited, route]