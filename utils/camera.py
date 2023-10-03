class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_pygame_pos(self, x, y):
        return (x - self.x, y - self.y)