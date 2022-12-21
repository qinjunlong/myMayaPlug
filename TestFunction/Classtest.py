
class animal(object):
    def __init__(self):
        print("FF1")

    def play(self):
        print("play")
        
    def study(self):
        print("study")
class dog(animal):
    def __init__(self):
        super(animal, self).__init__()
        print("FF2")
b =dog()
b.study()