import math
from queue import PriorityQueue


#I used the idea in here https://dbader.org/blog/priority-queues-in-python

def shortest_path(graph, start, goal):
    
    openSet = PriorityQueue()
    openSet.put(start, 0)
    
    previous = {start: None}
    gScore = {start: 0}

    while not openSet.empty():
        current = openSet.get()

        if current == goal:
            pathReconstructing(previous, start, goal)

        for neighbor in graph.roads[current]:
            temporaryGScore = gScore[current] + heuristicMeasure(graph.intersections[current], graph.intersections[neighbor])
            
            if neighbor not in gScore or temporaryGScore < gScore[neighbor]:
                gScore[neighbor] = temporaryGScore
                totalScore = temporaryGScore + heuristicMeasure(graph.intersections[current], graph.intersections[neighbor])
                openSet.put(neighbor, totalScore)
                previous[neighbor] = current

    return pathReconstructing(previous, start, goal)


#returning distance from start to goal
def heuristicMeasure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def pathReconstructing(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path