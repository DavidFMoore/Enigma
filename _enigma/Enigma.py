from Rotor import Rotor
from Reflector import Reflector
from Stecker import Stecker

class Enigma:
    def __init__(self, settings=[0], steckers=[], reflector='A', verbose=False):
        self.verbose = verbose
        self.reflector = Reflector(reflector)
        self.rotors = []
        self.steckers = []
        for i,setting in enumerate(settings):
            self.rotors.append(Rotor(i, setting))
        for stecker in steckers:
            self.steckers.append(Stecker(stecker))

    def print_settings(self):
        for i,ri in enumerate(self.rotors):
            print "%d:\t%d"%(i,ri.setting)

    def print_rotor_positions(self):
        for ri in self.rotors:
            print "%2d "%ri.position,
        print

    def map(self, letter):
        current = letter.upper()
        for si in self.steckers:
            if self.verbose:
                if current != si.map(current):
                    print "%s->%s,"%(current, si.map(current)),
            current = si.map(current)
        for ri in self.rotors:
            if self.verbose: print "%s->%s,"%(current, ri.map(current)),
            current = ri.map(current)
        if self.verbose: print "%s->%s,"%(current, self.reflector.map(current)),
        current = self.reflector.map(current)
        for ri in reversed(self.rotors):
            if self.verbose: print "%s->%s,"%(current, ri.rev_map(current)),
            current = ri.rev_map(current)
        for si in self.steckers:
            if self.verbose:
                if current != si.map(current):
                    print "%s->%s,"%(current, si.map(current)),
            current = si.map(current)
        if self.verbose: print
        return current

    def update_rotor_positions(self):
        self.rotors[0].position += 1
        for i in range(len(self.rotors)):
            if self.rotors[i].position == 26:
                self.rotors[i].position = 0
                if i < len(self.rotors)-1:
                    self.rotors[i+1].position += 1

    def reset_rotors(self):
        for ri in self.rotors:
            ri.position = ri.setting

    def encode(self, secret_message):
        output = ""
        for letter in secret_message:
            if not letter.isalpha():
                continue
            if self.verbose: self.print_rotor_positions()
            output += self.map(letter)
            self.update_rotor_positions()
        return output
