import pygame
import math

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
input_message = "Введіть рівень рекурсії. Чим нижче число тим дерево детальніше: "

n = 5
m = 5


def draw_tree(x, y, length, angle):
    if length > max_recursion_level:
        length *= 0.7
        length_cos = length * math.cos(angle)
        length_sin = length * math.sin(angle)

        end_pos = (x + length_cos, y - length_sin)
        pygame.draw.line(screen, BLACK, (x, y), end_pos)
        x = x + length_cos
        y = y - length_sin

        draw_tree(x, y, length, angle+math.pi/n)
        draw_tree(x, y, length, angle-math.pi/m)


if __name__ == '__main__':
    max_recursion_level = int(input(input_message))
    while max_recursion_level <= 0:
        print('Число повинно бути додатнім')
        max_recursion_level = int(input(input_message))

    screen = pygame.display.set_mode((600, 600))
    screen.fill(WHITE)
    draw_tree(320, 500, 200, math.pi/2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


