import random
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud:
   def __init__(self):
      self.x = SCREEN_WIDTH + random.randint(800, 1000)
      self.y = random.randint(50, 100)
      self.x2 = SCREEN_WIDTH + random.randint(800, 1000)
      self.y2 = random.randint(60, 590)
      self.width = CLOUD.get_width()

   def update(self, game_speed):
      self.x -= game_speed
      if self.x <=  -self.width:
         self.x = SCREEN_WIDTH + random.randint(800, 1000)
         self.y = random.randint(50, 100)
      self.x2 -= game_speed
      if self.x2 <=  -self.width:
         self.x2 = SCREEN_WIDTH + random.randint(800, 1000)
         self.y2 = random.randint(60, 90)

   def draw(self, screen):
      screen.blit(CLOUD, (self.x, self.y))
      screen.blit(CLOUD,(self.x2 , self.y2))
    
