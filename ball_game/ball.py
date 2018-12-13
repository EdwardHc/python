import pygame
from pygame.sprite import Sprite
from random import randint
class Ball(Sprite):
	'''表示单个外星人的类'''
	def __init__(self,ai_settings,screen):
		'''初始化外星人并设置其起始位置'''
		super().__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#加载外星人图像，并设置其rect属性
		self.image=pygame.image.load('images/ball.bmp')
		self.rect=self.image.get_rect()
		#每个外星人最初都在左上角附近
		#self.rect.x=0.0
		#self.rect.y=0.0
		#存储外星人的准确位置
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
	def blitme(self):
		'''在指定位置绘制外星人'''
		self.screen.blit(self.image,self.rect)
	def update(self):
		'''向左或向右移动外星人'''
		self.y+=self.ai_settings.ball_drop_speed
		self.rect.y=self.y
	def check_edges(self):
		'''如果外星人位于屏幕边缘，就返回true'''
		screen_rect=self.screen.get_rect()
		if self.rect.bottom>=screen_rect.bottom:
			return True


