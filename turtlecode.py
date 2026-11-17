from  maze_solver import *
from turtle import *
from time import sleep

#if input = BFS/DFS/A/DIJk generate the thing

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

def getAlgo(tt):
    alg = tt.screen.textinput("Algorithm", "Enter algorithm to display:\n('b' for bfs, 'd' for dfs, 'a' for astar) ").upper()
    start = (1, 1)
    maze[start[0]][start[1]] = 'S'
    goal = (8, 8)
    maze[goal[0]][goal[1]] = 'G'
    
    if alg == "A":
        result = astar(maze, start, goal, manhattan)
        
    elif alg == "B":
        result = bfs(maze, start, goal)
        
    elif alg =="D":
        result = dfs(maze, start, goal) 

    return result
    


def draw(maze, trtl, visited_order, path):
    sz = 30
    rows = len(maze)
    cols = len(maze[0])
    start_x = - (cols * sz) / 2
    start_y = (rows * sz) / 2

    
#draw each square
    def draw_square(r, c, fill_color):
        trtl.penup()
        x = start_x + c * sz
        y = start_y - r * sz
        trtl.goto(x, y)
        trtl.pendown()
        trtl.fillcolor(fill_color)
        trtl.begin_fill()
        for _ in range(4):
            trtl.forward(sz)
            trtl.right(90)
        trtl.end_fill()

#draw the maze
    for r in range(rows):
        for c in range(cols):
            char = maze[r][c]
            if char == 1:
                draw_square(r, c, "#000000")      
            elif char == 0:
                draw_square(r, c, "#ffffff")      
            elif char == 'S':
                draw_square(r, c, "#05f76a")      
            elif char == 'G':
                draw_square(r, c, "#ce1500")

#actual search
    for point in visited_order:
        if maze[point[0]][point[1]] not in ('S', 'G'): #if 0, color square yellow 
            sleep(0.2)
            draw_square(point[0], point[1], "#c2db34") 
#actual path
    for point in path:
        if maze[point[0]][point[1]] not in ('S', 'G'): #if 0, color square yellow 
            sleep(0.2)
            draw_square(point[0], point[1], "#0015ff") 

#update and maintain screen
    trtl.screen.update()
    trtl.screen.mainloop()

if __name__ == "__main__": 
    trtl = Turtle()  
    trtl.screen.tracer(10)

    while 1:
        result = getAlgo(trtl)
        draw(maze, trtl, result[1], result[0])    
    
    
