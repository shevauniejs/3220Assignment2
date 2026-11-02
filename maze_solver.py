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

def bfs(maze, start, goal):
	path = []
	q = [start]
	
	while q!=[]:
		current = q.pop(0)
		path.append(current)
		X, Y = int(current[0]), int(current[1])
		if maze[X-1][Y]==0 and maze[X-1][Y] not in q: #up
			q.append((X-1, Y))
			print ((X-1,Y)==goal)
			if (X-1,Y)==goal:
				return path
		elif maze[X][Y-1]==0 and maze[X][Y-1] not in q: #left
			q.append((X, Y-1))
			if (X,Y-1)==goal:
				return path
		elif maze[X+1][Y]==0 and maze[X+1][Y] not in q: #down
			q.append((X+1, Y))
			if (X+1,Y)==goal:
				return path
		elif maze[X][Y+1]==0 and maze[X][Y+1] not in q: #right
			q.append((X, Y+1))
			if (X,Y+1)==goal:
				return path
				
			
		
						
	
def dfs(maze, start, goal):
    path = []

def astar(maze, start, goal, heuristic):
    path = []

def dijkstra(maze, start, goal, cost):
    path = []
    
def visualize():
    pass
    
if __name__ == "__main__":
	start = (1,1)
	goal = (1,2)
	print ("The maze\n")
	for line in maze:
		print(line)
	print(bfs(maze,start, goal))
		