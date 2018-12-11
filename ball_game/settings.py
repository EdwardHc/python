class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕设置
		self.screen_width=1200
		self.screen_height=600
		self.bg_color=(230,230,230)
		#接球板的设置
		self.board_speed_factor=30
		# 球的设置
		self.ball_drop_speed=5
		self.ball_num=3
		#子弹设置
		self.bullet_speed_factor=3
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullet_allowed=3
		#外星人设置
		self.alien_speed_factor=1
		self.fleet_drop_speed=10
		#fleet_direction为1表示右移，为-1表示左移
		self.fleet_direction=1

		