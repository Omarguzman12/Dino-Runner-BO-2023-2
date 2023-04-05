import random
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud:
   def __init__(self):
      self.x = SCREEN_WIDTH + random.randint(800, 1000)
      self.y = random.randint(50, 100)
      self.width = CLOUD.get_width()

   def update(self, game_speed):
      self.x -= game_speed
      if self.x <=  -self.width:
         self.x = SCREEN_WIDTH + random.randint(600, 900)
         self.y = random.randint(50, 100)

   def draw(self, screen):
      screen.blit(CLOUD, (self.x, self.y))
    
