class Jar:
    def __init__(self, capacity=12):
        self.num = 0
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        else:
            self.cap = capacity

    def __str__(self):
        ret = ""
        for _ in range(self.num):
            ret += "🍪"
        return ret

    def deposit(self, n):
        if self.num + n > self.cap:
            raise ValueError()
        else:
            self.num += n

    def withdraw(self, n):
        if self.num - n < 0:
            raise ValueError()
        else:
            self.num -= n

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.num
