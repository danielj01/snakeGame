import time
import pygame
import neat
import os
import random
from collections import namedtuple

pygame.init()
pygame.font.init()

WIN_WIDTH = 700
WIN_HEIGHT = 350
BLOCK_SIZE = 20
score = 0
SNAKE_IMG = (pygame.transform.scale_by(pygame.image.load(os.path.join('Downloads', 'snakeGameAI', 'imgs', 'snake.png')), 0.3))
BASE_IMG = (pygame.transform.scale_by(pygame.image.load(os.path.join('Downloads', 'snakeGameAI', 'imgs', 'background.png')), 3))
APPLE_IMG = (pygame.transform.scale_by(pygame.image.load(os.path.join('Downloads', 'snakeGameAI', 'imgs', 'apple.png')), 1.8))
x = 200
y = 200


class Snake:
    snake_block_list = [SNAKE_IMG, SNAKE_IMG]
    def __init__(self,x,y):
        self.body=[(x,y)]
        self.length = 0
        self.img = SNAKE_IMG
        self.direction = 'right'   
    def move(self):
        x, y = self.body[0]
        if self.direction == 'right':
            x += 20
        elif self.direction == 'left':
            x -= 20
        elif self.direction == 'up':
            y -= 20
        elif self.direction == 'down':
            y += 20
        for i in range(len(self.body)-1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0] = (x, y)
    def getcoords(self):
        return (self.x, self.y)
    def draw(self, win):
        for x, y in self.body:
            win.blit(SNAKE_IMG, (x,y))
    def set_direction(self, direction):
        self.direction = direction


def main():
    snake = Snake(200,200)
    apple_coords = [100, 100]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True
    j = 0
    while run:
        win.blit(BASE_IMG, (0,0))
        clock.tick(10)
        snake.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_d]:
                    snake.set_direction('right')
                elif pressed[pygame.K_a]:
                    snake.set_direction('left')
                elif pressed[pygame.K_w]:
                    snake.set_direction('up')
                elif pressed[pygame.K_s]:
                    snake.set_direction('down')  
        for i, x in enumerate(snake.body):
            if len(snake.body) > 1:
                for j, x in enumerate(snake.body):
                    if j < len(snake.body):
                        if snake.body[i] == snake.body[j] and i != j:
                            run = False
        win.blit(APPLE_IMG, (apple_coords[0], apple_coords[1]))
        snake.draw(win)
        pygame.display.update()
        if snake.body[0][0] < 0 or snake.body[0][0] > WIN_WIDTH or snake.body[0][1] > WIN_HEIGHT-20 or snake.body[0][1] < 0:
            run = False
        if snake.body[0][0] == apple_coords[0] and snake.body[0][1] == apple_coords[1]:
            snake.body.append((0, 0))
            x = (random.randrange(2, 30)*20)
            y = (random.randrange(2,15)*20)
            apple_coords = [x,y]
        if run == False:
            print("Score: " + str(len(snake.body)))
main()
