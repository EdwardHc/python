import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
	#初始化pygame、并设置和屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(ai_settings,screen)
	#创建一个用于射出子弹的编组
	bullets=Group()
	#创建一个外星人编组
	aliens=Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
		gf.update_aliens(ai_settings,aliens)
		#每次循环时都重绘屏幕
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()
