import pygame
from pygame.sprite import Group
from settings import Settings
from board import Board
from ball import Ball
import ball_game_func as bf
def run_game():
	#初始化pygame、并设置和屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	board=Board(ai_settings,screen)
	#创建一个外星人编组
	balls=Group()
	#创建外星人群
	bf.create_ball(ai_settings,screen,balls)
	#开始游戏的主循环
	while True:
		bf.check_events(ai_settings,screen,board)
		board.update()
		bf.update_balls(ai_settings,screen,board,balls)
		#每次循环时都重绘屏幕
		bf.update_screen(ai_settings,screen,board,balls)
run_game()
