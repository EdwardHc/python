import sys
import pygame
from water import Water
def check_events(ai_settings,screen):
	#监视屏幕和鼠标事件
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_Keydown_events(event,ai_settings,screen)


def check_Keydown_events(event,ai_settings,screen):
	'''响应按键'''
	if event.key==pygame.K_q:
		sys.exit()


def update_screen(ai_settings,screen,waters):
	'''更新屏幕上的图像，屏切换到新屏幕'''
	screen.fill(ai_settings.bg_color)
	waters.draw(screen)
	#让最近绘制的屏幕可见
	pygame.display.flip()

def get_number_waters_x(ai_settings,water_width):
	'''计算每行可容纳多少外星人'''
	#计算一行可容纳多少个外星人
	#外星人间距为外星人宽度
	available_space_x=ai_settings.screen_width-2*water_width
	number_waters_x=int(available_space_x/(2*water_width))
	return number_waters_x

def get_number_waters_y(ai_settings,water_height):
	'''计算屏幕可容纳多少行外星人'''
	available_space_y=(ai_settings.screen_height-
					   3*water_height)
	number_waters_y=int(available_space_y/(2*water_height))
	return number_waters_y

def create_water(ai_settings,screen,waters,water_number,list_number):
	'''创建一个外星人并将其放在当前行'''
	water=Water(ai_settings,screen)
	water_height=water.rect.height
	water.y=water.rect.height+2*water.rect.height*water_number
	water.rect.y=water.y
	water.rect.x=water.rect.width+2*water.rect.width*list_number
	waters.add(water)
	
def create_waters(ai_settings,screen,waters):
	'''创建外星人群'''
	#创建第一行外星人
	water=Water(ai_settings,screen)
	number_waters_x=get_number_waters_x(ai_settings,water.rect.width)
	number_waters_y=get_number_waters_y(ai_settings,water.rect.height)
	for number_list in range(number_waters_x):
		for water_number in range(number_waters_y):
			create_water(ai_settings,screen,waters,water_number,number_list)

def check_waters_edges(ai_settings,screen,waters):
	'''有外星人到达边缘时采取措施'''
	for water in waters.sprites():
		if water.check_edges():
			clean_water(ai_settings,waters)
			create_waters(ai_settings,screen,waters)
			
			
def clean_water(ai_settings,waters):
	'''将整群外星人下移并更新外星人位置'''
	#waters.update()
	for water in waters.sprites().copy():
		waters.remove(water)
	

def update_waters(ai_settings,screen,waters):
	'''检查是否有外星人到达屏幕边缘，并更新外星人位置'''
	check_waters_edges(ai_settings,screen,waters)
	waters.update()
