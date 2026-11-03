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
from time import sleep

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
	temp = []

	while q!=[]:
		current = q.pop(0)
		if current not in path:
			path.append(current)
		if len(temp) < len(path):
			temp = path.copy()

		X, Y = int(current[0]), int(current[1])
		if (X,Y) == goal:
			return path
		up, left, down, right = (X-1,Y), (X,Y-1), (X+1,Y), (X,Y+1)

		if maze[X-1][Y]==0 and up not in path and up not in q: #up
			q.append(up)
		if maze[X][Y-1]==0 and left not in path and left not in q: #left
			q.append(left)
		if maze[X+1][Y]==0 and down not in path and down not in q: #down
			q.append(down)
		if maze[X][Y+1]==0 and right not in path and right not in q: #right
			q.append(right)

	
def dfs(maze, start, goal):
	path = []
	stack = [start]


def astar(maze, start, goal, heuristic):
    path = []

def dijkstra(maze, start, goal, cost):
    path = []
    
def visualize():
    pass
    
if __name__ == "__main__":
	start = (1,1)
	goal = (8,8)
	print ("The maze\n")
	for line in maze:
		print(line)
	print(f"The path {bfs(maze,start, goal)}")
		