#Program opens and plays the audio from an MP3 file.
import pygame
print('=' * 10, 'DEFIANCE 021', '=' * 10)
pygame.init()
pygame.mixer.music.load('defiance021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
