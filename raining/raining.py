import pygame
from pygame.sprite import Group
from settings import Settings
from water import Water
import water_functions as wf
def run_water():
	#初始化pygame、并设置和屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Raining")
	waters=Group()
	#创建外星人群
	wf.create_waters(ai_settings,screen,waters)
	#开始游戏的主循环
	while True:
		wf.check_events(ai_settings,screen)
		wf.update_waters(ai_settings,screen,waters)
		#每次循环时都重绘屏幕
		wf.update_screen(ai_settings,screen,waters)
run_water()
