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

def draw(maze):
    trtl = Turtle()
    trtl.screen.tracer(10)
    sz = 30
    rows = len(maze)
    cols = len(maze[0])
    start_x = - (cols * sz) / 2
    start_y = (rows * sz) / 2
    
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


    start = (1, 1)
    goal = (8, 8)
    path = dfs(maze, start, goal)
    path = path[1]

    #print(f"path{path}")

    for point in path:
        #print(f"current point {point}")
        if maze[point[0]][point[1]] not in ('S', 'G'):
            sleep(0.5)
            draw_square(point[0], point[1], "#c2db34") 

    trtl.screen.update()
    trtl.screen.mainloop()

if __name__ == "__main__":
    draw(maze)
