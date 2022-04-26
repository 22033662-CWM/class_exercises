class UselessCal:
    def __init__(self):
        self.total = 0.0

    def add(self, *args: float) -> float:
        for num in args:
            self.total = self.total + num
        return self.total
