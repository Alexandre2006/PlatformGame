# Camera Class
# Entirely written by humans

class Camera:
    def __init__(self):
        self.y = 0
    
    def move_to(self, y):
        if self.y < y:
            self.y = y
    
    def calculate_pygame_pos(self, y):
        return (y - self.y)