#! /usr/bin/env python

from _enigma.Enigma import Enigma
from time import time
from numpy import mean

answer = 'WETTERBERICHTHEILHITLER'
print answer

times = []
#do things the stupid way
for si, secret_message in enumerate(open('NoStecker3Rotor/EncryptedWeatherReports.txt').readlines()):
    print si
    secret_message = secret_message[:-1]
    settings = 0
    tryme = 0
    start = time()
    for i in range(26):
        for j in range(26):
            for k in range(26):
                E = Enigma([i,j,k])
                decrypt = E.encode(secret_message)
                if decrypt == answer: break
            if decrypt==answer: break
        if decrypt==answer: break
    stop = time()
    times.append(stop-start)
print mean(times)
