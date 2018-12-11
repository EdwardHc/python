import pygame
from pygame.sprite import Group
from settings import Settings
from star import Star
import star_functions as sf


def run_star():
    # 初始化pygame、并设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Star Shining")
    # 创建一个外星人编组
    stars = Group()
    # 创建外星人群
    sf.create_sky(ai_settings, screen, stars)
    # 开始游戏的主循环
    while True:
        sf.check_events(ai_settings, screen, stars)
    # 每次循环时都重绘屏幕
        sf.update_screen(ai_settings, screen, stars)


run_star()
