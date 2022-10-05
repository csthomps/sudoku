import pygame as p

p.init()





board = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


dif_list = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]


M = 9
def return_board(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ") # print board after solving it
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num: # if number is already in the column or row
            return False
             
 
    startRow = row - row % 3 # figure out where to start for 3x3 
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num: # check if number already in 3x3
                return False
    return True
 
def sudoku(grid, row, col, draw = False):
 
    if (row == M - 1 and col == M): # end of board
        return True
    if col == M: # when get to end of row, move to next row
        row += 1
        col = 0
    if grid[row][col] > 0: # if already solved move to next spot
        return sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num): # if it finds a number to put there
            
            grid[row][col] = num # put the number
            if draw:
                draw_board(screen, board)
                draw_lines(screen)
               
                p.display.update()
            dif_list[row][col] = num
            if sudoku(grid, row, col + 1): # if it can solve the next spot
                return True
        grid[row][col] = 0
    return False








SIZE = 600
BLOCKSIZE = round(SIZE/9)
 

def draw_lines(screen):
    for x in range(0, SIZE, BLOCKSIZE):
        for y in range(0, SIZE, BLOCKSIZE):
            rect = p.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            p.draw.rect(screen, p.Color("black"), rect, 1)
    for x in range(0, SIZE, BLOCKSIZE*3):
        for y in range(0, SIZE, BLOCKSIZE*3):
            rect = p.Rect(x, y, BLOCKSIZE*3, BLOCKSIZE*3)
            p.draw.rect(screen, p.Color("black"), rect, 3)
            
def draw_board(screen, board):
    font = p.font.SysFont("Helvetica", 60, True, False)
    for r in range(M):
        for c in range(M):
            num = board[r][c]
            if num != 0:
                text = str(num)
                text_object = font.render(text,0,p.Color("Black"))
                text_location = p.Rect(BLOCKSIZE*r+BLOCKSIZE//3-2, BLOCKSIZE*c, BLOCKSIZE,BLOCKSIZE)
                screen.blit(text_object, text_location)
            new_num = dif_list[r][c]
            if new_num != 0:
                text = str(num)
                text_object = font.render(text,0,p.Color("Blue"))
                text_location = p.Rect(BLOCKSIZE*r+BLOCKSIZE//3-2, BLOCKSIZE*c, BLOCKSIZE,BLOCKSIZE)
                p.draw.rect(screen,p.Color("white"),p.Rect(BLOCKSIZE*r, BLOCKSIZE*c, BLOCKSIZE,BLOCKSIZE))
                
                screen.blit(text_object, text_location)




running = True
setup_mode = False
solved = False
row = None
col = None

while running:

    screen = p.display.set_mode((SIZE,SIZE))
    screen.fill(p.Color("white"))
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
        if e.type == p.KEYDOWN:
            if e.key == p.K_RETURN and not setup_mode:
                solved = True
                sudoku(board, 0, 0, True)
            if setup_mode and not solved:
                    if row != None:
                        if e.key == p.K_0:
                            board[row][col] = 0
                        if e.key == p.K_1:
                           board[row][col] = 1
                        if e.key == p.K_2:
                            board[row][col] = 2        
                        if e.key == p.K_3:
                           board[row][col] = 3
                        if e.key == p.K_4:
                           board[row][col] = 4            
                        if e.key == p.K_5:
                            board[row][col] = 5            
                        if e.key == p.K_6:
                           board[row][col] = 6            
                        if e.key == p.K_7:
                           board[row][col] = 7          
                        if e.key == p.K_8:
                           board[row][col] = 8
                        if e.key == p.K_9:
                            board[row][col] = 9           
            if e.key == p.K_r:
                    setup_mode = False
                    solved = False
                    row = None
                    col = None
                    board = [[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]]

                    dif_list = [[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]]   
            if e.key == p.K_SPACE:
                setup_mode = not setup_mode
        
        if setup_mode and not solved:        
            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # x,y location of mouse
                row = location[0]//BLOCKSIZE
                col = location[1]//BLOCKSIZE
                print(row,col)


                            
                

    draw_board(screen, board)
    draw_lines(screen)

    p.display.update()