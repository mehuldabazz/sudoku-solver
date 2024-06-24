import pygame
import time

# Define the initial Sudoku board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Initialize Pygame
pygame.init()

# Set up display
width, height = 540, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

# Load font
font = pygame.font.SysFont("comicsans", 40)
small_font = pygame.font.SysFont("comicsans", 20)
winner_font = pygame.font.SysFont("comicsans", 60)

# Draw the grid
def draw_grid(win, board):
    win.fill((255, 255, 255))
    gap = width // 9

    for i in range(10):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(win, (0, 0, 0), (0, i * gap), (width, i * gap), thick)
        pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, width), thick)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), 1, (0, 0, 0))
                win.blit(text, (j * gap + 15, i * gap + 15))

# Highlight the selected box
def draw_selected(win, row, col):
    gap = width // 9
    pygame.draw.rect(win, (255, 0, 0), (col * gap, row * gap, gap, gap), 3)

# Find the empty cell
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

# Check if the board is valid
def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# Solve the Sudoku board
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            draw_grid(win, bo)
            pygame.display.update()
            pygame.time.delay(100)

            if solve(bo):
                return True

            bo[row][col] = 0

            draw_grid(win, bo)
            pygame.display.update()
            pygame.time.delay(100)

    return False

# Display the winner message
def draw_winner(win):
    text = winner_font.render("You Won!", 1, (0, 255, 0))
    win.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)

# Main loop
def main():
    key = None
    run = True
    selected = None
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // (width // 9), pos[0] // (width // 9)
                selected = (row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_SPACE:
                    if solve(board):
                        draw_winner(win)
                if event.key == pygame.K_DELETE:
                    if selected:
                        board[selected[0]][selected[1]] = 0
                        key = None
                if event.key == pygame.K_RETURN:
                    if selected and key is not None:
                        if valid(board, key, selected):
                            board[selected[0]][selected[1]] = key
                            key = None

        if selected and key is not None:
            board[selected[0]][selected[1]] = key
            key = None

        draw_grid(win, board)
        if selected:
            draw_selected(win, selected[0], selected[1])
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


