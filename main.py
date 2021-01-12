import time
import random
import pygame


class Circle:
    r = 10
    color = 255, 255, 255

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = -1
        self.vy = -1

    def move(self):
        self.prov()
        self.x += self.vx
        self.y += self.vy

    def prov(self):
        if self.x - self.r <= 0 or self.x + self.r >= width:
            self.vx *= -1
        if self.y - self.r <= 0 or self.y + self.r >= height:
            self.vy *= -1


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = random.randint(200, 1500), random.randint(200, 800)
    screen = pygame.display.set_mode(size)
    screen.fill('black')
    clock = pygame.time.Clock()

    circles = []

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                circles.append(Circle(*event.pos))
        for circle in circles:
            circle.move()
            pygame.draw.circle(screen, circle.color, (circle.x, circle.y), circle.r)
        pygame.display.flip()
        clock.tick(100)

    pygame.quit()
