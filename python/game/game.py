import pygame
# from pygame.locals import K_ESCAPE, KEYDOWN

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
image_original = pygame.image.load('pikachu.png')
image_redimensionada = pygame.transform.scale(image_original, (128, 128))

scenario = pygame.image.load('scenario.png')
scenario_redimen = pygame.transform.scale(scenario, (1280, 720))
scenario_rect = scenario_redimen.get_rect()


# Defina a posição inicial da imagem
pos_x = (640 - 64) // 2
pos_y = (480 - 64) // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == KEYDOWN:
        #     if event.key == K_ESCAPE:
        #         running = False
  
    screen.fill("white")
    
    # pygame.draw.rect(screen, "green", player_pos, 10)
    
    screen.blit(scenario_redimen, scenario_rect)
    screen.blit(image_redimensionada, (pos_x, pos_y))
    
    
    # Movimentação do personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        pos_y -= 2
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        pos_y += 2
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        pos_x -= 2
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        pos_x += 2
    
    # Sair do jogo
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
    
    clock.tick(60)

def show_animations(animation):
    if animation == "correr_direita":
        correr_direita = ""
        screen.blit(correr_direita, (pos_x, pos_y))
        
    
pygame.display.quit()