import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants  import LARGE_CACTUS

class LargeCactus(Obstacle):
    Y_POS_LAR_CAC = 300
    
    def __init__(self):
        self.type = random.randint(0, 2)
        image = LARGE_CACTUS[self.type]
        super().__init__(image)
        self.rect.y = self.Y_POS_LAR_CAC
    