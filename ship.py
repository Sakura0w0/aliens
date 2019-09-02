import pygame

class Ship():
    def __init__(self, speed_settings, screen):
        # 初始化飞机并设置起始位置
        self.screen = screen
        self.speed_settings = speed_settings

        # 加载飞机图像,并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.fire = False


        # 储存小数点
        self.center = float(self.rect.centerx)


    def blitme(self):
        # 在指定位置绘画飞船
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed_settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed_settings.ship_speed

        self.rect.centerx = self.center


    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx