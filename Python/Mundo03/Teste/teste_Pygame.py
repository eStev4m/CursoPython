import pygame
from pygame.constants import QUIT

pygame.init()
lar = 640
alt = 480
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
    pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    if y >= alt:
        y = 0
    y += 3

    pygame.display.update()
