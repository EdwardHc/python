import sys
import pygame
from star import Star
from random import randint

def check_events(ai_settings, screen, stars):
    # 监视屏幕和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_Keydown_events(event, ai_settings, screen,stars)


def check_Keydown_events(event, ai_settings, screen, stars):
    '''响应按键'''
    if event.key == pygame.K_SPACE:
        shine_stars(ai_settings, screen, stars)
    elif event.key == pygame.K_q:
        sys.exit()


def update_screen(ai_settings, screen, stars):
    '''更新屏幕上的图像，屏切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    stars.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def get_number_stars_x(ai_settings, star_width):
    '''计算每行可容纳多少外星人'''
    # 计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x


def get_number_stars_y(ai_settings, star_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height -
                         3 * star_height)
    number_stars_y = int(available_space_y / (2 * star_height))
    return number_stars_y


def create_star(ai_settings, screen, stars):
    '''创建一个外星人并将其放在当前行'''
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = randint(0,1200)+star_width
    star.rect.x = star.x
    star.rect.y = randint(0,600)+star.rect.height
    stars.add(star)


def create_sky(ai_settings, screen, stars):
    '''创建外星人群'''
    # 创建第一行外星人
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_stars_y = get_number_stars_y(ai_settings, star.rect.height)
    for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars)


