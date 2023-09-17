#!/usr/bin/env python3
import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Définition de la taille de la grille
GRID_SIZE = (10, 10)

# Définition de la taille des cases et des bordures
CASE_SIZE = (40, 40)
BORDER_SIZE = 2

# Définition de la position de la case centrale
central_case_x = 4
central_case_y = 4

# Création de la liste de positions des points pour chaque case
points = []
for i in range(GRID_SIZE[0]):
    points.append([])
    for j in range(GRID_SIZE[1]):
        point_x1 = random.randint(5, 15)
        point_y1 = random.randint(5, 15)
        point_x2 = CASE_SIZE[0] - random.randint(5, 15)
        point_y2 = random.randint(5, 15)
        point_x3 = CASE_SIZE[0] - random.randint(5, 15)
        point_y3 = CASE_SIZE[1] - random.randint(5, 15)
        points[i].append([(point_x1, point_y1), (point_x2, point_y2), (point_x3, point_y3)])

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affichage de la grille
    screen.fill((255, 255, 255))  # Fond blanc
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Calcul de la position de la case
            case_x = i * (CASE_SIZE[0] + BORDER_SIZE) + BORDER_SIZE
            case_y = j * (CASE_SIZE[1] + BORDER_SIZE) + BORDER_SIZE

            # Affichage des bordures rouges pour la case centrale
            if i == central_case_x and j == central_case_y:
                pygame.draw.rect(screen, (255, 0, 0), (case_x, case_y, CASE_SIZE[0], CASE_SIZE[1]), BORDER_SIZE)

            # Affichage des bordures vertes pour les cases autour de la case centrale
            elif abs(i - central_case_x) <= 2 and abs(j - central_case_y) <= 2 and not (i == central_case_x and j == central_case_y) and not (abs(i - central_case_x) == 2 and abs(j - central_case_y) == 2):
                green_border_size = BORDER_SIZE + 2  # Augmentation de la taille des carrés verts
                pygame.draw.rect(screen, (0, 255, 0), (case_x, case_y, CASE_SIZE[0], CASE_SIZE[1]), green_border_size)

            # Affichage des bordures noires pour les autres cases
            else:
                pygame.draw.rect(screen, (0, 0, 0), (case_x, case_y, CASE_SIZE[0], CASE_SIZE[1]), BORDER_SIZE)

            # Affichage des points pour la case actuelle
            for point in points[i][j]:
                point_x = case_x + point[0]
                point_y = case_y + point[1]
                pygame.draw.circle(screen, (0, 0, 255), (point_x, point_y), 3)

# Rafraîchissement de l'affichage
    pygame.display.flip()
