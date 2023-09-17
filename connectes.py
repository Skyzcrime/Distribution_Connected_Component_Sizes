#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv


def min_et_max(tab):
    min = tab[0]
    max = tab[0]
    for i in range(1,len(tab)):
        if tab[i] < min:
            min = tab[i]
        elif tab[i] > max:
            max = tab[i]
    return (min, max)


def create_grid(coord_x, coord_y, distance):
    # On determine les coordonnées de grid 
    nb_points = len(coord_x)
    min_x, max_x = min_et_max(coord_x)
    min_y, max_y = min_et_max(coord_y)
    taille_cellule = (distance)*0.7072  # trying to approach sqrt(2)
    # creation de grid après initialisation 
    grid =[[ [] for _ in range(int((max_y-min_y)/taille_cellule)+1)] for _ in range(int((max_x-min_x)/taille_cellule)+1)]
    # on remplit grid des points du fichier 
    for i in range (nb_points):
        id_x = int((coord_x[i]-min_x)/taille_cellule)
        id_y = int((coord_y[i]-min_y)/taille_cellule)
        grid[id_x][id_y].append((coord_x[i], coord_y[i]))
    return grid

def load_instance(filename):
    """
    loads .pts file.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        coord_x = []
        coord_y = []
        for l in lines:
            points = [float(f) for f in l.split(',')]
            coord_x.append(points[0])
            coord_y.append(points[1])
        grid  = create_grid(coord_x, coord_y, distance)
        points_visites = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
         #  returns distance**2 (ca revient à enlever la racine), grid et une liste reunissant les points visites.
        return distance**2, grid, points_visites

def count_compo(grid, i, j, points_visites, distance):
    # Initialisation de la pile avec les coordonnées du premier point
    pile = [(i, j)]
    taille = 0
    while pile:
        # on récupère les coordonnées du point en haut de la pile
        x, y = pile.pop()
        if not points_visites[x][y] and grid[x][y]:
            points_visites[x][y] = True
            #  on ajoute le nombre de points dans la case car dans la case ils font forcement partie de la meme compo connexe
            taille += len(grid[x][y])
            # on ajoute les coordonnées des points voisins non visités
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    if (dx != 0 or dy != 0) and (abs(dx)!=2 or abs(dx)!=2):
                        #aucun interet de comparer avec la case actuelle 
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not points_visites[nx][ny] and connexion_entre_cases(grid, x, y, nx, ny, distance):
                            #permet de verifier qu'on ne sorte pas ( cas aux bords et si la case à cote est bonn)
                            pile.append((nx, ny)) 
    return taille


def print_components_sizes(distance, grid, points_visites):
    #on met les valeurs de count_compo dans un liste qu'on trie de manière décroissante sort et en O(nlogn)
    components_sizes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not points_visites[i][j] and grid[i][j]:
                components_sizes.append(count_compo(grid, i, j, points_visites, distance))
    components_sizes.sort(reverse=True)
    print(components_sizes)


def connexion_entre_cases(grid, i, j, x, y, distance):
    points1 = grid[i][j]
    points2 = grid[x][y]
    for point1 in points1:
        for point2 in points2:
            dx = point1[0] - point2[0]
            dy = point1[1] - point2[1]
            if dx*dx + dy*dy < distance:
                return True
            #cela permet de savoir si on peut lier les cases pour faire une compo connexe 
    return False





def main():
    for instance in argv[1:]:
        distance, grid,  points_visites  = load_instance(instance)
        print_components_sizes(distance,grid,points_visites)


main()
