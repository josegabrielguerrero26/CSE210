from game.casting.actor import Actor

# Import classes from other modules
from game.shared.point import Point
from game.shared.color import Color
import random

class Artifact(Actor):
    """class with inheritance attributes to make a item """
    
    def __init__(self):
        """constructor"""
        super().__init__()
        self._type = random.choice([True, False])
        self._text = "*" if self._type == True else "0"
        self._velocity = Point(0, 3)
    
    def get_type(self):
        """type of artifacts"""
        return self._type
    
    def set_coordinates(self):
        """coodinates of the removed artifacts"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        self.set_color(color)
        COLS = 30
        CELL_SIZE = 30
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        self.set_position(position)