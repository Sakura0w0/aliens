import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import functions as fun
from alien import Alien
from stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "play")

    # 创建外星人
    alien = Alien(ai_settings, screen)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建用于储存数据的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建外星人群
    fun.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        fun.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game:
            ship.update()
            fun.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            fun.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        fun.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()
