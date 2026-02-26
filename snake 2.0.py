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


def random_food():
    return (
        random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE),
    )


def game_loop(snake_color=(0, 255, 0), snake1_color=(0, 0, 255)):
    snake = [(100, 100), (50, 100), (0, 100)]
    snake1 = [(850, 800), (900, 800), (950, 800)]

    direction = (CELL_SIZE, 0)
    direction1 = (-CELL_SIZE, 0)

    food = random_food()

    score = 0
    score1 = 0

    while True:
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

                if event.key == pygame.K_w and direction1 != (0, CELL_SIZE):
                    direction1 = (0, -CELL_SIZE)
                elif event.key == pygame.K_s and direction1 != (0, -CELL_SIZE):
                    direction1 = (0, CELL_SIZE)
                elif event.key == pygame.K_a and direction1 != (CELL_SIZE, 0):
                    direction1 = (-CELL_SIZE, 0)
                elif event.key == pygame.K_d and direction1 != (-CELL_SIZE, 0):
                    direction1 = (CELL_SIZE, 0)

                elif event.key == pygame.K_SPACE:
                    snake_color = (
                        random.randrange(0, 255),
                        random.randrange(0, 255),
                        random.randrange(0, 255),
                    )
                    snake1_color = (
                        random.randrange(0, 255),
                        random.randrange(0, 255),
                        random.randrange(0, 255),
                    )

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_r:
                    return

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        new_head1 = (snake1[0][0] + direction1[0], snake1[0][1] + direction1[1])

        snake.insert(0, new_head)
        snake1.insert(0, new_head1)

        if new_head == food:
            score += 1
            food = random_food()
        else:
            snake.pop()

        if new_head1 == food:
            score1 += 1
            food = random_food()
        else:
            snake1.pop()

        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
            or new_head in snake[1:]
            or new_head in snake1
        ):
            return

        if (
            new_head1[0] < 0
            or new_head1[0] >= WIDTH
            or new_head1[1] < 0
            or new_head1[1] >= HEIGHT
            or new_head1 in snake1[1:]
            or new_head1 in snake
        ):
            return

        screen.fill("black")

        for x, y in snake:
            pygame.draw.rect(screen, snake_color, (x, y, CELL_SIZE, CELL_SIZE))

        for x, y in snake1:
            pygame.draw.rect(screen, snake1_color, (x, y, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, "red", (food[0], food[1], CELL_SIZE, CELL_SIZE))

        score_text = font.render(f"P1 Score: " + str(score), True, "white")
        score1_text = font.render(f"P2 Score: " + str(score1), True, "white")

        screen.blit(score_text, (10, 10))
        screen.blit(score1_text, (WIDTH - 230, 10))

        pygame.display.update()
        clock.tick(6)


while True:
    game_loop()