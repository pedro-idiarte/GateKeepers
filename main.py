import pygame
from pygame import font
import random
import time

pygame.init()

#color library
green = (0, 255, 0)
black = (0, 0 ,0)
#font elements = Font.ttf

#player elements
rankings = ["Novice", "Apprentice", "Rookie", "Farmer", "Journeyman", "Scout", "Adventurer", "Seeker",
"Warrior", "Mercenary", "Hunter", "Guardian", "Ranger", "Knight", "Sentinel", "Champion",
"Berserker", "Conqueror", "Warlord", "Gladiator", "Commander", "Hero", "Sage", "Master",
"Grandmaster", "Champion of Legends", "Dragon Slayer", "Keeper of the Realm", "Ascendant",
"Immortal", "Celestial", "Eternal Guardian", "Legendary Warrior", "Mythical Hero",
"Transcendent", "Elder Sage", "Lord of Eternity", "Master of Realms", "Titan of Time",
"Archon", "Ethereal Warden", "Divine Guardian", "Immortal Legend", "Infinite Champion",
"Eternal Warlord", "Celestial Emperor", "Void Conqueror", "Elder God", "Mythic Deity",
"Keeper of the Grind"]

player_ranking = 0
actual_exp = 0
actual_ranking = rankings[player_ranking] if player_ranking < len(rankings) else rankings[-1]

# Atributos iniciais
strength = 1
dexterity = 1
wisdom = 1
intelligence = 1
charisma = 1
constitution = 1

# Valores de incremento a cada nível
increment_value = 1

#screen elements
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption(" GrindKeepers 'IdleGame' by PepeXP")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = black
framerate = 30
timer = pygame.time.Clock()

# Carrega todas as imagens para cada ranking e armazena em um array
images = []

for rank in rankings:
    try:
        # Carrega a imagem do ranking de acordo com o nome
        image = pygame.image.load(f"assets/rankings/{rank}.png")
        image = pygame.transform.scale(image, (300, 300))  # Ajusta o tamanho da imagem
        images.append(image)  # Adiciona ao array de imagens
    except FileNotFoundError:
        print(f"Imagem para {rank} não encontrada.")
        images.append(None)  # Coloca None se a imagem não for encontrada


def draw_text(text, font_path, size, color_text, x, y):
    font = pygame.font.Font(font_path, size)
    char_class = font.render(text, True, color_text)
    screen.blit(char_class, (x, y))


start_time = pygame.time.get_ticks()
xp_timer = pygame.time.get_ticks()

#game mode
run = True
while run:
    #background color
    screen.fill(background)

    # Exibe os atributos na tela
    draw_text(f"Strength: {strength}", 'Font.ttf', 30, green, 20, 150)
    draw_text(f"Dexterity: {dexterity}", 'Font.ttf', 30, green, 20, 180)
    draw_text(f"Wisdom: {wisdom}", 'Font.ttf', 30, green, 20, 210)
    draw_text(f"Intelligence: {intelligence}", 'Font.ttf', 30, green, 20, 240)
    draw_text(f"Charisma: {charisma}", 'Font.ttf', 30, green, 20, 270)
    draw_text(f"Constitution: {constitution}", 'Font.ttf', 30, green, 20, 300)

    #Actual player ranking
    draw_text(actual_ranking, 'Font.ttf', 50, green, 270 ,20)
    draw_text('EXP '+str(actual_exp), 'Font.ttf', 50, green, 20, 20)

    # Calcula o tempo desde o início
    elapsed_time_ms = pygame.time.get_ticks() - start_time
    elapsed_seconds = elapsed_time_ms // 1000
    days = elapsed_seconds // 86400
    hours = (elapsed_seconds % 86400) // 3600
    minutes = (elapsed_seconds % 3600) // 60
    seconds = elapsed_seconds % 60

    # Formata e exibe o contador de tempo
    time_display = f"Uptime: {days}d {hours:02}:{minutes:02}:{seconds:02}"
    draw_text(time_display, 'Font.ttf', 30, green, 20, 550)

    # Exibe a imagem do ranking atual se ela existir
    if 0 <= player_ranking < len(images) and images[player_ranking]:
        screen.blit(images[player_ranking], (240, 100))

    # Check if 10 minutes (600,000 ms) have passeds
    if pygame.time.get_ticks() - xp_timer >= 1:  # 10 minutes in milliseconds
        actual_exp += 1  # Gain 1 XP
        xp_timer = pygame.time.get_ticks()  # Reset timer

        # Check if it's time to level up
        if actual_exp >= (player_ranking + 1) * 100:  # Level up for every 1000 XP * current level
            player_ranking += 1  # Go to the next level

            # Escolha aleatoriamente um atributo para incrementar sem substituição
            attributes = ['strength', 'dexterity', 'wisdom', 'intelligence', 'charisma', 'constitution']
            attribute_to_increment = random.sample(attributes, 1)[0]

            # Incrementa o atributo escolhido
            globals()[attribute_to_increment] += increment_value

            # Update the ranking if within bounds
            if player_ranking < len(rankings):
                actual_ranking = rankings[player_ranking]
            else:
                actual_ranking = rankings[-1]  # If max level, stay at highest rank

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    timer.tick(framerate)

pygame.quit()