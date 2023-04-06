import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
   

    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        self.rect.y = random.choice([280, 295, 350])
        self.step_index = 0
        self.ave = True
      

    def update(self, game_speed, player):
        if self.ave:
            self.bloat()
        
        if self.step_index >= 10:
          self.step_index = 0
        return super().update(game_speed, player)
    def bloat(self):
        self.image = BIRD[0] if self.step_index < 5  else BIRD[1]
        self.step_index += 1


    

    
