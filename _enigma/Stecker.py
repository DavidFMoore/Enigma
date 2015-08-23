class Stecker:
    def __init__(self, sub):
        self.sub = sub
    def map(self, in_):
        if in_ in self.sub:
            return self.sub[self.sub.index(in_)-1]
        else:
            return in_
