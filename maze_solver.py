"""
maze = 2d list of 1 or 0
start = row, col tuple
goal = row,col tuple

each method returns tuple (path, visited_order, stats
path = list of row, col tuple including S and G
visited order = list of row, col tuple in order of expansion
stats = dict {nodes_expanded: int,
              path_length: int,
              path cost: int/float}

"""

import heapq

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,1,0,0,1,0,0,1],
        [1,0,0,0,1,0,1,1,0,1],
        [1,1,1,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,0,0,0,0,1,0,1],
        [1,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]

def manhattan(curr, goal):
	return abs(curr[0]-goal[0]) + abs(curr[1]-goal[1])

def manhGn(curr, start):
	return abs(curr[0]-start[0]) + abs(curr[1]-start[1])

def bfs(maze, start, goal):
	"""
	maze = maze to search
	start = tuple: coordinates of the starting spot
	goal = tuple: coordinates of goal"""

	path = []
	q = [start]
	visited_order = []
	tracer ={}
	stats= {"nodes_expanded": 0,
	       "path_length": 0,
		   "path_cost": 0}

	while q!=[]:
		current = q.pop(0)
		stats["nodes_expanded"] += 1

		if current not in visited_order:
			visited_order.append(current)


		X, Y = int(current[0]), int(current[1])
		if (X,Y) == goal:
			break

		up, left, down, right = (X-1,Y), (X,Y-1), (X+1,Y), (X,Y+1)
		
		if maze[X-1][Y]!=1 and up not in visited_order: #up
			q.append(up)
			tracer[up] = current
		if maze[X][Y-1]!=1 and left not in visited_order: #left
			q.append(left)
			tracer[left] = current
		if maze[X+1][Y]!=1 and down not in visited_order: #down
			q.append(down)
			tracer[down] = current
		if maze[X][Y+1]!=1 and right not in visited_order: #right
			q.append(right)
			tracer[right] = current
	if q == []:
		return []
	else:
		currPos = goal
		while currPos != start:
			path.append(currPos)
			currPos = tracer[currPos]
		path.reverse()
		path.insert(0,start)
		stats["path_length"] = len(path)
		return (path, visited_order, stats)
	
def dfs(maze, start, goal):
	"""
	maze = maze to search
	start = tuple: coordinates of the starting spot
	goal = tuple: coordinates of goal"""
	path = []
	stk = [start]
	visited_order = []
	tracer ={}
	stats= {"nodes_expanded": 0,
	       "path_length": 0,
		   "path_cost": 0}
	
	while stk!=[]:
		current = stk.pop(-1)
		stats["nodes_expanded"] += 1

		if current not in visited_order:
			visited_order.append(current)

		X, Y = int(current[0]), int(current[1])
		
		if (X,Y) == goal:
			break

		up, left, down, right = (X-1,Y), (X,Y-1), (X+1,Y), (X,Y+1)

		if maze[X][Y+1]!=1 and right not in visited_order: #right
			stk.append(right)
			tracer[right] = current
		if maze[X+1][Y]!=1 and down not in visited_order: #down
			stk.append(down)
			tracer[down] = current
		if maze[X][Y-1]!=1 and left not in visited_order: #left
			stk.append(left)
			tracer[left] = current
		if maze[X-1][Y]!=1 and up not in visited_order: #up
			stk.append(up)
			tracer[up] = current

	if stk == []:
		return []
	else:
		currPos = goal
		while currPos != start:
			path.append(currPos)
			currPos = tracer[currPos]
		path.reverse()
		path.insert(0,start)
		stats["path_length"] = len(path)
		return (path, visited_order, stats)

def astar(maze, start, goal, heuristic):
	"""
	maze = maze to search
	start = tuple: coordinates of the starting spot
	goal = tuple: coordinates of goal"""
	path = []
	pq = []
	b = 3.14159 #bias to give costs?
	heapq.heappush(pq,(heuristic(start, goal),start))
	visited_order = []
	tracer ={}
	stats= {"nodes_expanded": 0,
	       "path_length": 0,
		   "path_cost": 0}
	
	while pq!=[]:
		currentA = heapq.heappop(pq)
		stats["nodes_expanded"] += 1
		currentCost = currentA[0]
		current = currentA[1]

		
		if current not in visited_order:
			visited_order.append(current)

		X, Y = int(current[0]), int(current[1])
		
		if (X,Y) == goal:
			goal = currentA
			break

		up, left, down, right = (X-1,Y), (X,Y-1), (X+1,Y), (X,Y+1)

		if maze[X-1][Y]!=1 and up not in visited_order: #up
			gn= manhGn(up,start) * b
			hn= heuristic(up,goal)
			add = (gn+hn,up)
			heapq.heappush(pq, add)
			gn, hn = 0,0
			tracer[add] = (currentCost,current)
		
		if maze[X][Y-1]!=1 and left not in visited_order: #left
			gn= manhGn(left,start) * b
			hn= heuristic(left,goal)
			add = (gn+hn,left)
			heapq.heappush(pq, add)
			tracer[add] = (currentCost,current)
			gn, hn = 0,0
		
		if maze[X+1][Y]!=1 and down not in visited_order: #down
			gn= manhGn(down, start) * b
			hn= heuristic(down,goal)
			add = (gn+hn,down)
			heapq.heappush(pq, add)
			tracer[add] = (currentCost,current)
			gn, hn = 0,0
		
		if maze[X][Y+1]!=1 and right not in visited_order: #right
			gn= manhGn(right, start) * b
			hn= heuristic(right,goal)
			add = (gn+hn,right)
			heapq.heappush(pq,add)
			tracer[add] = (currentCost,current)
			gn, hn = 0,0

	if pq == []:
		return []
	else:
		currPos = goal
		while currPos[1] != start: 
			path.append(currPos[1])
			stats["path_cost"] += currPos[0] #omit
			currPos = tracer[currPos]
		path.reverse()
		path.insert(0,start)
		stats["path_length"] = len(path)
		return (path, visited_order, stats)

def dijks(maze, start, goal):
	"""
	maze = maze to search
	start = tuple: coordinates of the starting spot
	goal = tuple: coordinates of goal"""
	path = []
	pq = []
	b = 3.14159 #bias to give costs?
	heapq.heappush(pq,(manhGn(start, goal),start))
	visited_order = []
	tracer ={}
	stats= {"nodes_expanded": 0,
	       "path_length": 0,
		   "path_cost": 0}
	
	while pq!=[]:
		currentA = heapq.heappop(pq)
		stats["nodes_expanded"] += 1
		currentCost = currentA[0]
		current = currentA[1]

		
		if current not in visited_order:
			visited_order.append(current)

		X, Y = int(current[0]), int(current[1])
		
		if (X,Y) == goal:
			goal = currentA
			break

		up, left, down, right = (X-1,Y), (X,Y-1), (X+1,Y), (X,Y+1)

		if maze[X-1][Y]!=1 and up not in visited_order: #up
			gn= manhGn(up,start) * b
			add = (gn,up)
			heapq.heappush(pq, add)
			gn = 0
			tracer[add] = (currentCost,current)
		
		if maze[X][Y-1]!=1 and left not in visited_order: #left
			gn= manhGn(left,start) * b
			add = (gn,left)
			heapq.heappush(pq, add)
			tracer[add] = (currentCost,current)
			gn = 0
		
		if maze[X+1][Y]!=1 and down not in visited_order: #down
			gn= manhGn(down, start) * b
			add = (gn,down)
			heapq.heappush(pq, add)
			tracer[add] = (currentCost,current)
			gn = 0
		
		if maze[X][Y+1]!=1 and right not in visited_order: #right
			gn= manhGn(right, start) * b
			add = (gn,right)
			heapq.heappush(pq,add)
			tracer[add] = (currentCost,current)
			gn = 0

	if pq == []:
		return []
	else:
		currPos = goal
		while currPos[1] != start: 
			path.append(currPos[1])
			stats["path_cost"] += currPos[0] #omit
			currPos = tracer[currPos]
		path.reverse()
		path.insert(0,start)
		stats["path_length"] = len(path)
		return (path, visited_order, stats)

if __name__ == "__main__":
	start = (1,1)
	goal = (4,4)

	result = dijks(maze, start, goal, manhattan)