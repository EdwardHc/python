import sys
import pygame
from ball import Ball
from random import randint
from game_stats import GameStats
def check_events(ai_settings,screen,board):
	#监视屏幕和鼠标事件
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_Keydown_events(event,ai_settings,screen,board)
		elif event.type==pygame.KEYUP:
			check_Keyup_events(event,ai_settings,screen,board)

def check_Keydown_events(event,ai_settings,screen,board):
	'''响应按键'''
	if event.key==pygame.K_RIGHT:
		board.moving_right=True
	elif event.key==pygame.K_LEFT:
		board.moving_left=True
	elif event.key==pygame.K_UP:
		board.moving_up=True
	elif event.key==pygame.K_DOWN:
		board.moving_down=True
	elif event.key==pygame.K_q:
		sys.exit()

def check_Keyup_events(event,ai_settings,screen,board):
	'''响应松开'''
	if event.key==pygame.K_RIGHT:
		board.moving_right=False
	elif event.key==pygame.K_LEFT:
		board.moving_left=False
	elif event.key==pygame.K_UP:
		board.moving_up=False
	elif event.key==pygame.K_DOWN:
		board.moving_down=False

def update_screen(ai_settings,screen,board,balls):
	'''更新屏幕上的图像，屏切换到新屏幕'''
	screen.fill(ai_settings.bg_color)
	board.blitme()
	balls.draw(screen)
	#让最近绘制的屏幕可见
	pygame.display.flip()

def get_number_balls_x(ai_settings,ball_width):
	'''计算每行可容纳多少外星人'''
	#计算一行可容纳多少个外星人
	#外星人间距为外星人宽度
	available_space_x=ai_settings.screen_width-2*ball_width
	number_balls_x=int(available_space_x/(2*ball_width))
	return number_balls_x

def create_ball(ai_settings,screen,balls):
	'''创建一个外星人并将其放在当前行'''
	ball=Ball(ai_settings,screen)
	ball_width=ball.rect.width
	ball.x=ball_width+2*ball_width*randint(0,get_number_balls_x(ai_settings,ball_width))
	ball.rect.x=ball.x
	ball.rect.y=ball.rect.height
	balls.add(ball)
	
def create_balls(ai_settings,screen,board,balls):
	'''创建外星人群'''
	#创建第一行外星人
	ball=Ball(ai_settings,screen)
	number_balls_x=get_number_balls_x(ai_settings,ball.rect.width)
	for ball_number in range(ai_settings.ball_num):
			create_ball(ai_settings,screen,balls)
	
def check_board_ball_collisions(ai_settings,screen,board,balls):
	collisions=pygame.sprite.spritecollide(board,balls, True, pygame.sprite.collide_mask)
	if collisions:
		return True


def remove_balls(ai_settings,screen,balls):
	'''检查是否有外星人到达屏幕边缘，并更新外星人位置'''
	# 删除已消失的子弹
	for ball in balls.copy():
		#if ball.rect.bottom >= screen.get_rect().bottom:
		balls.remove(ball)

def check_balls_edges(ai_settings,screen,balls,stats):
	#balls.update()
	for ball in balls.copy():
		if ball.rect.bottom >= screen.get_rect().bottom:
			if stats.board_left>0:
				stats.board_left-=1
			else:
				stats.game_active=False
			return True

def update_balls(ai_settings,screen,board,balls,stats):
	'''更新子弹的位置，并删除已消失的子弹'''
	#更新子弹位置
	balls.update()
	if pygame.sprite.spritecollide(board, balls,True):
		#remove_balls(ai_settings, screen, balls)
		create_ball(ai_settings, screen, balls)
	if check_balls_edges(ai_settings,screen,balls,stats):
		remove_balls(ai_settings, screen, balls)
		create_ball(ai_settings, screen,balls)


