import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

score_surf = font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

# Use convert_alpha to remove the white background
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf= pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    print('space')
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and event.type == pygame.KEYDOWN:
                    game_active = True
                    snail_rect.left = 800

    if game_active:

        # If you dont setup a background you will be able to see previous frames so make sure to set a background
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surf, score_rect)

        # Move the snail to the right when it leaves the screen on the left
        snail_rect.x -= 4
        if snail_rect.right <-100: snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # player
        # gravity
        player_gravity += 1
        player_rect.y += player_gravity
        # make him not fall through the ground
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # End game if user touches the snail
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')
    
    # Update everything
    pygame.display.update() 
    # This tells that the while loop should not run quicker than 60 times a sec
    clock.tick(60)