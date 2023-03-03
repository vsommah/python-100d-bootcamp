class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing it under water.")

    def swim(self):
        print("Keep swimming.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
