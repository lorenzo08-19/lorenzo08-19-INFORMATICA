import pygame
import sys
import time

# Assicurati che i file ball.py e paddle.py siano nella stessa cartella
from ball   import Ball
from paddle import Paddle

# ------------------------------------------------------------------ #
# COSTANTI                                                             #
# ------------------------------------------------------------------ #

SCREEN_W  = 800
SCREEN_H  = 600
FPS       = 60

COUNTDOWN = 60        
MAX_LIVES =  3        

BG_COLOR      = ( 20,  20,  40)
TEXT_COLOR    = (220, 220, 220)
COLOR_WIN     = ( 80, 220, 120)
COLOR_LOSE    = (220,  80,  80)

# ------------------------------------------------------------------ #
# INIZIALIZZAZIONE                                                     #
# ------------------------------------------------------------------ #

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Non farcela cadere!")
clock      = pygame.time.Clock()
font_large  = pygame.font.SysFont("Arial", 56, bold=True)
font_medium = pygame.font.SysFont("Arial", 30)
font_small  = pygame.font.SysFont("Arial", 20)

def load_heart(size: int = 28) -> pygame.Surface:
    import os
    path = os.path.join(os.path.dirname(__file__), "assets", "heart.png")
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (size, size))
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(surf, (220, 60, 60), (size // 2, size // 2), size // 2)
    return surf

heart_img = load_heart()

# ------------------------------------------------------------------ #
# FUNZIONI — Logica Timer                                             #
# ------------------------------------------------------------------ #

def time_remaining(start: float, duration: int) -> float:
    return max(0.0, duration - (time.time() - start))

def is_expired(start: float, duration: int) -> bool:
    return time.time() - start >= duration

# ------------------------------------------------------------------ #
# FUNZIONI — Disegno HUD                                              #
# ------------------------------------------------------------------ #

def draw_hud(surface: pygame.Surface, remaining: float, lives: int):
    # 1. Disegna il Timer testuale
    timer_text = f"{int(remaining)}s"
    timer_surf = font_medium.render(timer_text, True, TEXT_COLOR)
    timer_rect = timer_surf.get_rect(centerx=SCREEN_W // 2, top=10)
    surface.blit(timer_surf, timer_rect)

    # 2. Disegna le Vite (Cuori)
    for i in range(lives):
        margin = 10
        spacing = 4
        x = SCREEN_W - margin - (i + 1) * (heart_img.get_width() + spacing)
        surface.blit(heart_img, (x, 15))


def draw_timer_bar(surface: pygame.Surface, remaining: float, duration: int):
    bar_w = SCREEN_W - 100
    bar_h = 10
    x, y = 50, 48
    
    # Sfondo barra
    pygame.draw.rect(surface, (80, 40, 40), (x, y, bar_w, bar_h), border_radius=4)
    
    # Riempimento proporzionale
    fill_w = int(bar_w * (remaining / duration))
    if fill_w > 0:
        pygame.draw.rect(surface, (80, 200, 80), (x, y, fill_w, bar_h), border_radius=4)


def draw_end_screen(surface: pygame.Surface, won: bool):
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))

    msg   = "Hai vinto!" if won else "Hai perso!"
    color = COLOR_WIN    if won else COLOR_LOSE
    surf  = font_large.render(msg, True, color)
    surface.blit(surf, surf.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 - 40)))

    hint = font_medium.render("Premi R per rigiocare", True, TEXT_COLOR)
    surface.blit(hint, hint.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 + 40)))

# ------------------------------------------------------------------ #
# FUNZIONE — Reset Partita                                             #
# ------------------------------------------------------------------ #

def reset_game():
    ball = Ball(SCREEN_W // 2, int(SCREEN_H * (2/3)))
    paddle = Paddle()
    start_time = time.time()
    lives = MAX_LIVES
    return ball, paddle, start_time, lives

# ------------------------------------------------------------------ #
# LOOP PRINCIPALE                                                      #
# ------------------------------------------------------------------ #

ball, paddle, start_time, lives = reset_game()
game_over = False
won = False

running = True
while running:

    # ---- 1. EVENTI ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                ball, paddle, start_time, lives = reset_game()
                game_over = False
                won = False


    # ---- 2. AGGIORNA ---------------------------------------------- #
    if not game_over:
        keys = pygame.key.get_pressed()
        paddle.update(keys)
        ball.update(SCREEN_W, SCREEN_H)
        ball.bounce_off_paddle(paddle.rect)

        # Controllo caduta pallina
        if not ball.alive:
            lives -= 1
            if lives > 0:
                # Reset solo pallina
                ball = Ball(SCREEN_W // 2, int(SCREEN_H * (2/3)))
            else:
                game_over = True
                won = False

        # Controllo Timer
        if is_expired(start_time, COUNTDOWN):
            game_over = True
            won = True # Se scade il tempo e hai ancora vite, hai vinto


    # ---- 3. DISEGNA ----------------------------------------------- #
    screen.fill(BG_COLOR)

    # Disegno HUD e oggetti
    remaining = time_remaining(start_time, COUNTDOWN)
    draw_hud(screen, remaining, lives)
    draw_timer_bar(screen, remaining, COUNTDOWN)
    
    paddle.draw(screen)
    ball.draw(screen)

    if game_over:
        draw_end_screen(screen, won)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()











