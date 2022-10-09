from setupData import *
from mazeDrawing import *

def showResult(previous, start, goal, isRoutable):
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

    converter = pointNameToPointConverter(start, "_")
    start = (int(converter["x"]), int(converter["y"]))

    converter = pointNameToPointConverter(goal, "_")
    goal = (int(converter["x"]), int(converter["y"]))

    visualize_maze(read_file("maze.txt"), start, goal, route)
  else:
    converter = pointNameToPointConverter(start, "_")
    start = (int(converter["x"]), int(converter["y"]))

    converter = pointNameToPointConverter(goal, "_")
    goal = (int(converter["x"]), int(converter["y"]))
    
    visualize_maze(read_file("maze.txt"), start, goal, route)
  
def DFS(adjacencyList, start, goal):
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
    showResult(previous, start, goal, isRoutable)
    print('Path was found')
    return True
  else:
    isRoutable = False
    showResult(previous, start, goal, isRoutable)
    print('No path was found')
    return False

setupAdjacencyList()

from GlobalCache import adjacencyList
from GlobalCache import global_start
from GlobalCache import global_end

start = pointToPointNameConverter(global_start)
end = pointToPointNameConverter(global_end)

DFS(adjacencyList, start, end)