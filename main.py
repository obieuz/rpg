import pygame

# Inicjalizacja pygame
pygame.init()

# Ustawienia okna gry
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moja Gra")

# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizacja ekranu
    screen.fill((0, 0, 0))  # Czyszczenie ekranu (czarny kolor)
    pygame.display.flip()  # Odświeżenie ekranu

# Zakończenie pygame
pygame.quit()