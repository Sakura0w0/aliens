class Settings():
    '''储存游戏所有设置内容'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20
        # 外星人设置
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动,为-1 表示向左移动
        self.fleet_direction = 1

        self.ship_limit = 3

        # 以什么速度加快游戏节奏
        self.speedup = 1.005
        self.pointup = 1.5
        self.dynamic()


    def dynamic(self):
        """随着游戏变化增加速度"""
        self.ship_speed = 2
        self.bullet_speed_factor = 3
        self.alien_speed = 0.5

        # fleet_direction为1 表示向右, -1表示向左
        self.fleet_direction = 1

        # 积分
        self.alien_point = 50


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup
        self.bullet_speed_factor *= self.speedup
        self.alien_speed *= self.speedup

        self.alien_point = int(self.alien_point * self.pointup)