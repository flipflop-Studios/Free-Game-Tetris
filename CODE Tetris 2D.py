import pygame
import random
import time

# Initialisieren von Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("TetrisSong.mp3")
beep = pygame.mixer.Sound("TetrisBeep2.mp3")
whoosh = pygame.mixer.Sound("Tetris-Whoosh.mp3")
tik = pygame.mixer.Sound("Tetris-Switch.mp3")
tik.set_volume(0.5)
explosion = pygame.mixer.Sound("Tetris-Explosion.mp3")
cover = pygame.image.load('Tetris-Cover.jpg')
cover = pygame.transform.scale(cover, (300, 600))
grid = pygame.image.load('Tetris-Grid.png')
grid = pygame.transform.scale(grid, (300, 600))

# Fenstergröße und Farben
width, height = 300, 600
block_size = 30
cols, rows = width // block_size, height // block_size
bg_color = (0, 0, 0)  # Schwarzer Hintergrund
field_color = (50, 50, 50)  # Hintergrundfarbe des Spielfelds
cols, rows = width // block_size, height // block_size

# Erstellen eines Fensters
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

font = pygame.font.Font(None, 100)
score = 0
counterp = 300
counterpm = 0
counterc = 600
ending = 'None'
xc = 0
yc = 0
coverBlock = pygame.draw.rect(screen, (50, 50, 50), (xc, yc, 300, 600))
gridBlock = pygame.draw.rect(screen, (50, 50, 50), (0, 0, 300, 600))

# Funktion zum Zeichnen eines Tetris-Tetrominos
def draw_tetromino(matrix, color, x, y):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect((x + col) * block_size, (y + row) * block_size, block_size, block_size),
                )

# Intro-Animation
intro_tetrominos = [
    (
        [[0, 1, 0],
         [1, 1, 1]],
        (72, 82, 72)
    ),
    (
        [[1, 0, 0],
         [1, 1, 1]],
        (172, 182, 172)
    ),
    (
        [[0, 0, 0],
         [1, 1, 1]],
        (252, 255, 252)
    ),
]

intro_animation_duration = 3  # Dauer der Intro-Animation in Sekunden
intro_start_time = time.time()

# Tetromino-Formen und ihre Farben
tetrominos = [
    ([[1, 1, 1, 1]], (255, 0, 0)),  # Rot
    ([[1, 1], [1, 1]], (0, 255, 0)),  # Grün
    ([[1, 1, 1], [0, 1, 0]], (0, 0, 255)),  # Blau
    ([[1, 1, 1], [1, 0, 0]], (255, 255, 0)),  # Gelb
    ([[1, 1, 1], [0, 0, 1]], (255, 0, 255)),  # Lila
    ([[1, 1, 1], [0, 1, 0]], (0, 255, 255)),  # Cyan
    ([[1, 1, 1], [1, 0, 1]], (255, 165, 0)),  # Orange
    ([[1, 1, 1]], (140, 0, 230)),  # HPINK BY MICHELLE
    ([[1, 0], [1, 1]], (255, 125, 0)),  # HPINK BY MICHELLE
    ([[0, 1, 1], [1, 1, 0]], (4, 47, 102)),  # Orange
]

def draw_matrix(matrix, offset, color):
    for y, row in enumerate(matrix):
        for x, val in enumerate(row):
            if val:
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect((offset[0] + x) * block_size, (offset[1] + y) * block_size, block_size, block_size),
                )

def check_collision(board, shape, offset):
    for y, row in enumerate(shape):
        for x, val in enumerate(row):
            if val:
                board_x = x + offset[0]
                board_y = y + offset[1]
                if (
                    board_x < 0
                    or board_x >= cols
                    or board_y >= rows
                    or board[board_y][board_x]
                ):
                    return True
    return False

def clear_rows(board):
    global score
    full_rows = []
    for i, row in enumerate(board):
        if all(row):
            full_rows.append(i)
            score += 10
            explosion.play()
            time.sleep(0)
    for i in full_rows:
        del board[i]
        board.insert(0, [0] * cols)

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

# Spielvariablen
board = [[0] * cols for _ in range(rows)]
current_tetromino, current_color = random.choice(tetrominos)
current_x = cols // 2 - len(current_tetromino[0]) // 2
current_y = 0
fall_speed = 1

# Hauptprogrammschleife
running = True
clock = pygame.time.Clock()
fall_time = 0
bra = 0
animation = 1

while animation:

    if running == False:
        paygame.quit()

    coverBlock
    screen.blit(cover, coverBlock)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animation = False
            bra = 0
            running = False
            pygame.quit()

    pygame.display.update()

# Bewegung
#whoosh.play()
#while counterc != 0:
#    counterc -= 1
#    coverBlock = pygame.draw.rect(screen, (50, 50, 50), (xc, yc, 300, 600))
#    screen.fill(bg_color)
#    yc += 1
#    screen.blit(cover, coverBlock)
#    pygame.display.update()
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            animation = False
#            bra = 0
#            running = False
#            pygame.quit()
screen.blit(grid, gridBlock)
pygame.display.update()
time.sleep(0.5)

# Hauptprogrammschleife
running = True
clock = pygame.time.Clock()

counterm = 1
while running:
    text = font.render(str(score), True, (255,255,255))
    text_rect = text.get_rect(center=(250, 50))

    if score >= 999:
        score = 999
        running = False
        ending = 'won'

    if bra == 0:
        counterm -= 1
        counterp -= 1
    print(counterm, counterp, counterpm)

    if counterm == 0:
        pygame.mixer.music.play()
        counterm = 1160
    if counterp == 0:
        counterp = 300 - counterpm
        score += 1
        if counterpm <= 260:
            counterpm += 10


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            animation = False
            bra = 0
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if bra == 0:
                if event.key == pygame.K_LEFT:
                    new_x = current_x - 1
                    if not check_collision(board, current_tetromino, (new_x, current_y)):
                        current_x = new_x
                elif event.key == pygame.K_RIGHT:
                    new_x = current_x + 1
                    if not check_collision(board, current_tetromino, (new_x, current_y)):
                        current_x = new_x
                elif event.key == pygame.K_DOWN:
                    new_y = current_y + 1
                    if not check_collision(board, current_tetromino, (current_x, new_y)):
                        current_y = new_y
                elif event.key == pygame.K_UP:
                    rotated_tetromino = rotate_matrix(current_tetromino)
                    if not check_collision(board, rotated_tetromino, (current_x, current_y)):
                        current_tetromino = rotated_tetromino
            if event.key == pygame.K_b:
                bra = 1
                pygame.mixer.music.pause()
            if event.key == pygame.K_n:
                bra = 0
                pygame.mixer.music.unpause()
    if bra == 0:
        # Bewegung des Tetrominos nach unten
        current_time = pygame.time.get_ticks()
        if current_time - fall_time > 1000:  # Fallgeschwindigkeit (1 Sekunde = 1000 Millisekunden)
            new_y = current_y + 1
            if not check_collision(board, current_tetromino, (current_x, new_y)):
                current_y = new_y
                fall_time = current_time
            else:
                tik.play()
                # Wenn das Tetromino nicht weiter nach unten kann, fügen Sie es dem Spielfeld hinzu und generieren Sie ein neues Tetromino
                for y, row in enumerate(current_tetromino):
                    for x, val in enumerate(row):
                        if val:
                            board[current_y + y][current_x + x] = current_color
                clear_rows(board)
                current_tetromino, current_color = random.choice(tetrominos)
                current_x = cols // 2 - len(current_tetromino[0]) // 2
                current_y = 0

    screen.fill(bg_color)
    screen.blit(grid, gridBlock)
    draw_matrix(board, (0, 0), field_color)  # Verwenden Sie die Spielfeldfarbe für das Spielfeld
    draw_matrix(current_tetromino, (current_x, current_y), current_color)
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(30)  # Framerate auf 30 FPS begrenzen

running = True
while running:
    if ending == 'won':
        pygame.mixer.music.pause()
        fontW = pygame.font.Font(None, 80)  # Hier können Sie die Größe ändern (in diesem Fall auf 36)
        # Text erstellen
        textW = fontW.render("YOU WON", True, (255, 255, 255))
        # Text auf den Bildschirm zeichnen
        time.sleep(1)
        screen.fill(bg_color)
        screen.blit(textW, (15, 200))
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
