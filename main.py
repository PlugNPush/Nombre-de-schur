class Color:
    def __init__(self):
        self.white = '\033[0m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[31m'

color = Color()

print(color.purple, "Bonjour !")
