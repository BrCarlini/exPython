import pygame
pygame.init()
print('======= Reproduzir MP3 =======')
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Digite algo para sair: ')