#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repozitorij, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#okiren plan

#I. Naredi ogrodje -> while zanka, canvas, eventi za exit itd


#II. Naredi kvadrat -> ta kvadrat bo v prihodnisti ratala kača, zaenkrat naj bo samo kvadrat
#	naredi logiko da ta kvadrat lahko zavija levo desno z kliki na gumne na tipkovnici
#	naredi logiko, da se nakej izpiše, ko se ta kvadrat dotakne stene
#	naredi logiko, da se ta kvadrat premika po nekem "gridu" -> hint nastavi clock.tick na nekaj malega,
#		vsak frame premakni kaco za nekaj pixlov, ta premik predstavlja sirino vsake celice


#III. Kvdrat spremeni v seznam kvadratov, ki predstavljajo kaco


#IV. Naredi logiko, da se nekaj izpiše, ce se kace zabije sama vase


#V. Naredi nek nov kvadrat ki predstavlja hrano
#	-> naredi da se vsakic ko ga kaca poje z glavo prestavi na nakljucno mesto in kaca zrasta


#od tu naprej je treba samo še štet score, kej izpiovat na ekrat, dt kk gumb za game over pa restart itd... neke olepšave




#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov

import pygame
import random
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 900
CELL_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 2.0")

font = pygame.font.Font(pygame.font.get_default_font(), 36)

clock = pygame.time.Clock()

print("press r to restart")
print("press q to quit")


def game_loop():
    snake = [(100, 100), (50, 100), (0, 100)]
    direction = (CELL_SIZE, 0)

    food = (
        random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE),
    )

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return

        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = random.randrange(0, WIDTH, CELL_SIZE),random.randrange(0, HEIGHT, CELL_SIZE)
        else:
            snake.pop()

        # collision detection
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake[1:]:
            return  # game over → restart

        screen.fill("black")

        for x, y in snake:
            pygame.draw.rect(screen, "green", (x, y, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, "red", (food[0], food[1], CELL_SIZE, CELL_SIZE))

        score_text = font.render(f"Score: " + str(score), True, "white")
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(13)


# restart loop
while True:
    game_loop()