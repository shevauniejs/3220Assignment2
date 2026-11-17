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

def manhattan(curr, goal):
	return abs(curr[0]-goal[0]) + abs([curr[1]-goal[1]])

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
		
		if maze[X-1][Y]==0 and up not in visited_order: #up
			q.append(up)
			tracer[up] = current
		if maze[X][Y-1]==0 and left not in visited_order: #left
			q.append(left)
			tracer[left] = current
		if maze[X+1][Y]==0 and down not in visited_order: #down
			q.append(down)
			tracer[down] = current
		if maze[X][Y+1]==0 and right not in visited_order: #right
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

		if maze[X][Y+1]==0 and right not in visited_order: #right
			stk.append(right)
			tracer[right] = current
		if maze[X+1][Y]==0 and down not in visited_order: #down
			stk.append(down)
			tracer[down] = current
		if maze[X][Y-1]==0 and left not in visited_order: #left
			stk.append(left)
			tracer[left] = current
		if maze[X-1][Y]==0 and up not in visited_order: #up
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
		return (path, visited_order, stats)


def astar(maze, start, goal, heuristic):
    path = []

def ucs(maze, start, goal, cost):
    path = []
    
def visualize():
    pass
    
if __name__ == "__main__":
	start = (1,1)
	goal = (8,8)
	#path =[]
	print ("The maze\n")
	for line in maze:
		print(line)

	algo = input("Enter 'A' for A*, 'B' for BFS, 'D' for DFS, and 'U' for UCS(dijkstra): ").upper()
	if algo =='A':
		path = astar(maze,start, goal)

	elif algo == 'B':
		path = bfs(maze, start, goal)

	elif algo == 'U':
		path = ucs(maze, start, goal)

	elif algo == 'D':
		path = dfs(maze,start, goal)

	print(f"The path {path[0]} \nvisiting order {path[1]} \nNUMBER: {len(path[1])}")
		