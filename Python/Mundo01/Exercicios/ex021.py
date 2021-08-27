# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
from pygame import mixer

pygame.init()
mixer.music.load("ex021.mp3")
mixer.music.play()
pygame.event.wait()
