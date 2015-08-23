#! /usr/bin/env python

from _enigma.Enigma import Enigma
from random import randint

settings_file = open("SecretSettingsDoNotOpen.txt", 'w')
encrypts_file = open("EncryptedWeatherReports.txt", 'w')
secret_message = "Wetterbericht Heil Hitler"

for i in range(300):
    settings = [randint(0,25) for j in range(3)]
    E = Enigma(settings)
    encrypts_file.write("%s\n"%E.encode(secret_message))
    settings_file.write("%d,%d,%d\n"%(settings[0], settings[1], settings[2]))

encrypts_file.close()
settings_file.close()
