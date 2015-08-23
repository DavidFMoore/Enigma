abcs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Reflector:
  def __init__(self, reflector):
    self.charmap = {
        'A': "EJMZALYXVBWFCRQUONTSPIKHGD",
        'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        'C': "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        'easy': "ZYXWVUTSRQPONMLKJIHGFEDCBA"
        }[reflector]
  def map(self, in_):
    out = abcs.index(in_)
    return self.charmap[out]
