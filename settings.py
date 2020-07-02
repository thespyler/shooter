import pygame
pygame.init()
height, width = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
game_on = True
ship = pygame.image.load('ship.png')

meteor = pygame.image.load('meteor.png')
laser = pygame.image.load('laser.png')

pygame.mixer.init()
#pygame.mixer.music.load('ls.ogg')
font = pygame.font.SysFont('Comic Sans MS',100)
small_font = pygame.font.SysFont('Comic Sans MS',30) 

class Fonter:
	def __init__(self, msg, color,  display):
		text = font.render(str(msg), True, color)
		self.rect = text.get_rect()
		self.rect.center = (height//2, width//2)
		display.blit(text,[self.rect.x, self.rect.y])  
		
class ScoreFont:
	def __init__(self, msg, color, display):
		text = small_font.render(str(msg), True, color)
		self.rect = text.get_rect()
		self.rect.center = (100, 100)
		display.blit(text,[self.rect.x, self.rect.y]) 
