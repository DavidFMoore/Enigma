#! /usr/bin/env python

from _enigma import *

E = Enigma.Enigma([0], reflector="easy", verbose=True)

secret_message = """
    We the people, in order to form a more perfect union, establish justice, ensure domestic
    tranquility, provide for the common defense, promote the general welfare, and secure the
    blessings of liberty to ourselves and our posterity, do ordain and establish this constitution
    for the united states of america.
"""

secret_message = "AAA"

encrypted_message = E.encode(secret_message)
E.reset_rotors()
decrypted_message = E.encode(encrypted_message)
print secret_message.upper().replace(' ','')
print encrypted_message
print decrypted_message
