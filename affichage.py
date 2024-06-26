import pygame
from pygame import mixer
import random
from button import Button

pygame.init()
mixer.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")

class get_font():
    def custom(taille): 
        """Fonction servant à selectionner la police de caractères custom"""
        return pygame.font.Font("assets/font.ttf", taille)
    
    def gabriola(taille):
        """Fonction servant à selectionner la police de caractères gabriola"""
        return pygame.font.SysFont("Gabriola", taille)

def init_main_menu():
    """Fonction servant à selectionner le mode de jeu"""

    SCREEN.fill((0, 0, 0))
    SCREEN.set_alpha(0)
    
    pygame.mixer.music.unload()    
        
    pygame.mixer.music.load("assets/Skyrim - Music & Ambience - Night.mp3")
    mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        SCREEN.blit(pygame.image.load("assets/Background.png"), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font.custom(70).render("Menu Principal", True, (245, 245, 220))
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PVP_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 380), text_input="PvP", font=get_font.custom(40), base_color="White", hovering_color="Green")

        BOT_TARAK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 460), text_input="Tarak", font=get_font.custom(40), base_color="White", hovering_color="Green")

        BOT_DIANTHEA_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 540), text_input="Dianthea", font=get_font.custom(40), base_color="White", hovering_color="Green")

        BOT_PETER_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 620), text_input="Peter", font=get_font.custom(40), base_color="White", hovering_color="Green")

        BOT_CYNTHIA_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 700), text_input="Cynthia", font=get_font.custom(40), base_color="White", hovering_color="Green")

        for button in [PVP_BUTTON, BOT_TARAK_BUTTON, BOT_DIANTHEA_BUTTON, BOT_PETER_BUTTON, BOT_CYNTHIA_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PVP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    pygame.mixer.music.fadeout(3000)
                    fade_out()
                    pygame.mixer.music.unload()
                    return "pvp"
                if BOT_TARAK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    pygame.mixer.music.fadeout(2000)
                    fade_out()
                    pygame.mixer.music.unload()
                    return "tarak"
                if BOT_DIANTHEA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    pygame.mixer.music.fadeout(2000)
                    fade_out()
                    pygame.mixer.music.unload()
                    return "dianthea"
                if BOT_PETER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    pygame.mixer.music.fadeout(2000)
                    fade_out()
                    pygame.mixer.music.unload()
                    return "peter"
                if BOT_CYNTHIA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    pygame.mixer.music.fadeout(2000)
                    fade_out()
                    pygame.mixer.music.unload()
                    return "cynthia"

        pygame.display.update()

def follow_prompt():
    """Fonction servant à afficher la page 'suivez le promp' """

    SCREEN.blit(pygame.image.load("assets/Background.png"), (0, 0))

    FOLLOW_PROMPT_TEXT = get_font.custom(70).render("Suivez le Prompt", True, "White")
    FOLLOW_PROMPT_RECT = FOLLOW_PROMPT_TEXT.get_rect(center=(600, 400))
    SCREEN.blit(FOLLOW_PROMPT_TEXT, FOLLOW_PROMPT_RECT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

def fade_out():
    """Fonction servant à faire une transition de fond"""
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade_surface.fill((0,0,0)) # Fill with black or any color you want to fade to
    for alpha in range(0, 51):
        fade_surface.set_alpha(alpha)
        SCREEN.blit(fade_surface, (0,0))
        pygame.display.update()
        pygame.time.wait(60)

def init_display(joueurs):
    """Fonction servant à initialiser l'affichage du jeu"""
    global rectangle_goblin, rectangle_guerrier

    joueur_1, joueur_2 = joueurs

    pygame.mixer.music.unload()

    pygame.mixer.music.load("assets/Skyrim - Music & Ambience - Taverns.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    SCREEN.fill((245, 245, 220))

    GRID = pygame.image.load("assets/grid.png")
    SCREEN.blit(GRID, (420, 60))
    SCREEN.blit(GRID, (420, 490))

    IMAGE_JOUEUR_1 = pygame.image.load("assets/goblin.png")
    SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_1, 0.4), (100, 550))

    IMAGE_JOUEUR_2 = pygame.image.load("assets/guerrier.png")
    SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_2, 0.4), (875.2, 30))

    FONT = pygame.font.SysFont("Gabriola", 40)

    nom_joueur_1 = FONT.render(joueur_1, True, "black")
    SCREEN.blit(nom_joueur_1, (35, 505))

    nom_joueur_2 = FONT.render(joueur_2, True, "black")
    nom_joueur_2_width = nom_joueur_2.get_width()
    nom_joueur_2_x = 1150 - nom_joueur_2_width
    SCREEN.blit(nom_joueur_2, (nom_joueur_2_x, 255))

    case_joueur_1 = pygame.draw.rect(SCREEN, (31, 142, 77), (35,300,340,190), 0)
    for i in range(4):
        pygame.draw.rect(SCREEN, (139, 69, 19), (35-i,300-i,345,195), 3)

    case_joueur_2 = pygame.draw.rect(SCREEN, (31, 142, 77), (810,300,340,190), 0)
    for i in range(4):
        pygame.draw.rect(SCREEN, (139, 69, 19), (810-i,300-i,345,195), 3)
    
    SCREEN.blit(pygame.transform.scale_by(pygame.image.load("assets/carte.png"), 0.1), (5, 5))
    SCREEN.blit(pygame.transform.scale_by(pygame.image.load("assets/carte.png"), 0.1), (1143.8, 743.2))

    pygame.display.update()

def init_end_game(gagant, nom_joueur_1, nom_joueur_2, score_joueur_1, score_joueur_2):
    """Fonction servant à afficher le menu de fin de partie"""

    SCREEN.fill((245, 245, 220))

    running = True
    while running:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        END_GAME_TEXT_BRAVO = get_font.custom(70).render(f"Bravo !", True, (171, 9, 9))      
        END_GAME_RECT_BRAVO = END_GAME_TEXT_BRAVO.get_rect(center=(600, 100))
        SCREEN.blit(END_GAME_TEXT_BRAVO, END_GAME_RECT_BRAVO)

        END_GAME_TEXT = get_font.custom(40).render(f"{gagant} a gagné(e) !", True, "Black")
        END_GAME_RECT = END_GAME_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(END_GAME_TEXT, END_GAME_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 700), text_input="Retour", font=get_font.custom(40), base_color="White", hovering_color=(255, 51, 51))
        BACK_BUTTON.changeColor(MENU_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)  

        IMAGE_JOUEUR_1 = pygame.image.load("assets/goblin.png")
        SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_1, 0.4), (200, 340))

        IMAGE_JOUEUR_2 = pygame.image.load("assets/guerrier.png")
        SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_2, 0.4), (800, 320))

        Nom_joueur_1 = get_font.gabriola(40).render(nom_joueur_1, True, (171, 9, 9))
        Nom_joueur_1_rect = Nom_joueur_1.get_rect(center=(300, 335))
        SCREEN.blit(Nom_joueur_1, Nom_joueur_1_rect)

        Nom_joueur_2 = get_font.gabriola(40).render(nom_joueur_2, True, (171, 9, 9))
        Nom_joueur_2_rect = Nom_joueur_2.get_rect(center=(900, 310))
        SCREEN.blit(Nom_joueur_2, Nom_joueur_2_rect)

        Score_joueur_1 = get_font.gabriola(40).render(f"{score_joueur_1}", True, "black")
        Score_joueur_1_rect = Score_joueur_1.get_rect(center=(300, 540))
        SCREEN.blit(Score_joueur_1, Score_joueur_1_rect)

        Score_joueur_2 = get_font.gabriola(40).render(f"{score_joueur_2}", True, "black")
        Score_joueur_2_rect = Score_joueur_2.get_rect(center=(900, 540))
        SCREEN.blit(Score_joueur_2, Score_joueur_2_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False
                    pygame.mixer.music.stop()
                    mixer.music.unload()

        pygame.display.update()

class de():

    def add_grille(face_dé, x, y, joueur):
        """Fonction servant à ajouter un dé sur l'affichage du jeu"""

        dé = "assets/dé_" + str(face_dé) + ".png"

        if joueur == "joueur_2":
            if x == 1 and y == 1:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (435, 65))
            elif x == 2 and y == 1:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 65))
            elif x == 3 and y == 1:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (685, 65))
            elif x == 1 and y == 2:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (435, 155))
            elif x == 2 and y == 2:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 155))
            elif x == 3 and y == 2:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (685, 155))
            elif x == 1 and y == 3:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (435, 250))
            elif x == 2 and y == 3:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 250))
            elif x == 3 and y == 3:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (685, 250))
        elif joueur == "joueur_1":
            if x == 1 and y == 1:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (435, 495))
            elif x == 2 and y == 1:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 495))
            elif x == 3 and y == 1:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (685, 495))
            elif x == 1 and y == 2:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (435, 587))
            elif x == 2 and y == 2:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 587))
            elif x == 3 and y == 2:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (685, 587))
            elif x == 1 and y == 3:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (435, 678))
            elif x == 2 and y == 3:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 678))
            elif x == 3 and y == 3:
                SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (685, 678))

        pygame.display.flip()

    def remove_grille(x, y, joueur):
        """Fonction servant à supprimer un dé sur l'affichage du jeu"""

        rect = {
            'taille' : (75, 75),
            'couleur' : (245, 245, 220)
        }

        if joueur == "joueur_2":
            if x == 1 and y == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((435, 65), rect["taille"]))
            elif x == 2 and y == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((560, 65), rect["taille"]))
            elif x == 3 and y == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((685, 65), rect["taille"]))
            elif x == 1 and y == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((435, 155), rect["taille"]))
            elif x == 2 and y == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((560, 155), rect["taille"]))
            elif x == 3 and y == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((685, 155), rect["taille"]))
            elif x == 1 and y == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((435, 250), rect["taille"]))
            elif x == 2 and y == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((560, 250), rect["taille"]))
            elif x == 3 and y == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((685, 250), rect["taille"]))

        elif joueur == "joueur_1":
            if x == 1 and y == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((435, 495), rect["taille"]))
            elif x == 2 and y == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((560, 495), rect["taille"]))
            elif x == 3 and y == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((685, 495), rect["taille"]))
            elif x == 1 and y == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((435, 587), rect["taille"]))
            elif x == 2 and y == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((560, 587), rect["taille"]))
            elif x == 3 and y == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((685, 587), rect["taille"]))
            elif x == 1 and y == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((435, 678), rect["taille"]))
            elif x == 2 and y == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((560, 678), rect["taille"]))
            elif x == 3 and y == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((685, 678), rect["taille"]))

        pygame.display.flip()

    def remove_plateau(joueur):
        """Fonction servant à supprimer un dé sur l'affichage du jeu"""

        if joueur == "joueur_1":
            pygame.draw.rect(SCREEN, (31, 142, 77), (35,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(SCREEN, (139, 69, 19), (35-i,300-i,345,195), 3)
        elif joueur == "joueur_2":
            pygame.draw.rect(SCREEN, (31, 142, 77), (810,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(SCREEN, (139, 69, 19), (810-i,300-i,345,195), 3)

        pygame.display.flip()

    def lancer(joueur):
        """Fonction servant à charger l'animation de lancé de dé et qui retourne un chiffre entre 1 eet 6"""

        clock = pygame.time.Clock()
        frames = [pygame.image.load(f"assets/dé_{i}.png") for i in [4, 2, 5, 1, 6, 3, 5, 1, 3, 5, 2, 6, 5, 2, 6, 2, 1, 3]]
        frame = 0

        for frame in range(len(frames)):
            clock.tick(12)
            if frame >= len(frames):
                frame = 0

            image = frames[frame]

            if joueur == "joueur_1":
                SCREEN.blit(pygame.transform.scale_by(image, 0.2), (153, 343))

            elif joueur == "joueur_2":
                SCREEN.blit(pygame.transform.scale_by(image, 0.2), (930, 340))

            pygame.display.update()

        face_random = random.randint(1, 6)
        image = pygame.image.load(f"assets/dé_{face_random}.png")

        if joueur == "joueur_1":
            SCREEN.blit(pygame.transform.scale_by(image, 0.2), (153, 343))

        elif joueur == "joueur_2":
            SCREEN.blit(pygame.transform.scale_by(image, 0.2), (930, 340))

        pygame.display.update()

        return face_random

class score():

    def add_colonne(score, joueur, x):
        """Fonction servant à afficher le score d'une colonne d'un joueur"""

        FONT = pygame.font.SysFont("Gabriola", 40)
        score = FONT.render(f"{score}", True, "Black")

        if joueur == "joueur_1":
            if x == 1:
                SCREEN.blit(score, (460, 440))
            elif x == 2:
                SCREEN.blit(score, (585, 440))
            elif x == 3:
                SCREEN.blit(score, (705, 440))

        elif joueur == "joueur_2":
            if x == 1:
                SCREEN.blit(score, (460, 335))
            elif x == 2:
                SCREEN.blit(score, (585, 335))
            elif x == 3:
                SCREEN.blit(score, (705, 335))

        pygame.display.flip()

    def remove_colonne(joueur, x):
        """Fonction servant à supprimer le score d'une colonne d'un joueur"""

        rect = {
            'taille' : (50, 50),
            'couleur' : (245, 245, 220)
        }

        if joueur == "joueur_1":
            if x == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((450, 440), rect["taille"]))
            elif x == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((575, 440), rect["taille"]))
            elif x == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((695, 440), rect["taille"]))

        elif joueur == "joueur_2":
            if x == 1:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((450, 335), rect["taille"]))
            elif x == 2:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((575, 335), rect["taille"]))
            elif x == 3:
                pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((695, 335), rect["taille"]))

        pygame.display.flip()

    def add_total(score, joueur):
        """fonction servant à afficher le score total d'un joueur"""

        FONT = pygame.font.SysFont("Gabriola", 40)
        score = FONT.render(f"{score}", True, "Black")

        if joueur == "joueur_1":
            score_width = score.get_width()
            score_x = 370 - score_width
            SCREEN.blit(score, (score_x, 505))

        elif joueur == "joueur_2":
            SCREEN.blit(score, (818, 255))

        pygame.display.flip()

    def remove_total(joueur):
        """Fonction servant à supprimer le score d'une colonne d'un joueur"""

        rect = {
            'taille' : (70, 50),
            'couleur' : (245, 245, 220)
        }

        if joueur == "joueur_1":
            pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((310, 505), rect["taille"]))
        elif joueur == "joueur_2":
            pygame.draw.rect(SCREEN, rect["couleur"], pygame.Rect((818, 255), rect["taille"]))

        pygame.display.flip()

def clear_grille(joueur):
    """Fonction servant à effacer tout les dés dans une grille donnée"""

    if joueur == "joueur_2":
        SCREEN.blit(pygame.image.load("assets/grid.png"), (420, 60))
    if joueur == "joueur_1":
        SCREEN.blit(pygame.image.load("assets/grid.png"), (420, 490))

    pygame.display.flip()

    