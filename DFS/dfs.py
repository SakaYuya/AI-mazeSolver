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

  # un-comment the code below to show the out-path's visualization

  # converter = pointNameToPointConverter(start, "_")
  # start = (int(converter["x"]), int(converter["y"]))

  # converter = pointNameToPointConverter(goal, "_")
  # goal = (int(converter["x"]), int(converter["y"]))

  # visualize_maze(read_file(), start, goal, route)

  return route
  
def DFS():
  setupAdjacencyList()

  from GlobalCache import adjacencyList
  from GlobalCache import global_start
  from GlobalCache import global_end

  start = pointToPointNameConverter(global_start)
  goal = pointToPointNameConverter(global_end)
  
  # The result variable
  route = {"isRoutable": False, "path" : []}
  
  previous = []
  for point in adjacencyList.keys():
    previous.append((point, None))
  previous = dict(previous)

  def dfs(_start): 
    for point in adjacencyList[_start].keys():
      if previous[point] == None:
        previous[point] = _start
        if point == goal:
          return True  
        elif dfs(point):
          return True
    return False
  
  if (dfs(start)):
    isRoutable = True
    route["path"] = resultConverter(previous, start, goal, isRoutable)
    print('Path was found')
    route["isRoutable"] = isRoutable
  else:
    isRoutable = False
    resultConverter(previous, start, goal, isRoutable)
    print('No path was found')
    route["isRoutable"] = False

  return route



route = DFS()

if (route["isRoutable"]):
  print(f'The way to exit the maze: {route["path"]}')
else:
  print("There is no way to exit the maze")