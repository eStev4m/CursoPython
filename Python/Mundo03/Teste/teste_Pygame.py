import pygame
from pygame.constants import QUIT

pygame.init()
lar = 1200
alt = 700
x = lar / 2
y = 0

tela = pygame.display.set_mode((lar, alt))
pygame.display.set_caption('Teste Caixa Vermelha')
relogio = pygame.time.Clock()


while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,120,200), (x, y, 120, 120))
    if y >= alt:
        y = 0
    y += 3
    pygame.draw.circle(tela, (137,120,98), (x + 360, y), 85)
    if y >= alt:
        y = 0
    y += 6

    pygame.display.update()
