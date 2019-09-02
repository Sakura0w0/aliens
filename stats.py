class GameStats():
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game = False


    def reset_stats(self):
        """初始化游戏"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0