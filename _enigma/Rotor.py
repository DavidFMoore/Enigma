abcs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charmap = [
  abcs,
#rotor wirings from German Enigma I and the army models.
  'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
  'AJDKSIRUXBLHWTMCQGZNPYFVOE',
  'BDFHJLCPRTXVZNYEIWGAKMUSQO',
  'ESOVPZJAYQUIRHXLNFTGKDCMWB',
  'VZBRGITYUPSDNHLXAWMJQOFECK']

class Rotor:
  def __init__(self, number, setting):
    self.charmap = charmap[number]
    self.setting = setting
    self.position = setting
  def map(self, in_):
    out = (abcs.index(in_) + self.position)%26
    return self.charmap[out]
  def rev_map(self, in_):
    out = (self.charmap.index(in_) - self.position)%26
    return abcs[out]


