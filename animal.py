class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        """
        base class function breathe
        """
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("doing underwater")

nemo = Fish()
nemo.breathe()
nemo.swim()