

def initialize_colors():
    yellow = [[3, 6, 5, 0], [2, 1, 0, 5], [1, 0, 2, 4], [0, 3, 4, 6]]
    blue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    green = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
    orange = [0, 0, 0, "2x", 0, 0, "2x", 0, "2x", 0, "3x"]
    purple = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return{"yellow": yellow,
           "blue": blue,
           "green": green,
           "orange": orange,
           "purple": purple}


class dice_roll:
    def __init__(self, white, yellow, blue, green, orange, purple):
        self.white = white
        self.yellow = yellow
        self.blue = blue
        self.green = green
        self.orange = orange
        self.purple = purple

roll = dice_roll(1,2,3,4,5,6)
print(roll)

