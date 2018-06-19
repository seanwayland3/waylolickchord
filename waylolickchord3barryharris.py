#!/usr/bin/env python

import mido 
import random
from mido import Message, MidiFile, MidiTrack

lick = [(3, 3, -1, -1, 3, 3, -1, -1, 3, 3, -1, -1)]
a=45
b=45+8
c=45+15

firstchord = [(a), (b), (c)]


def startlaterinlick(x,y):
# list of diminished waylolick repeated
    lick = [1, 1, 1, 1, 3, -2, 1, 1, 1, 1, 1, 1, 1, -2]
# uses modular function to return value of the lick
# starting y values from beginning
    return (lick[(x+y) % 12])

def getnextchord(chord):
    chord[0] = chord[0] + startlaterinlick(x, 0)
    chord[1] = chord[1] + startlaterinlick(x, 0)
    chord[2] = chord[2] + startlaterinlick(x, 0)
    return(chord)

with MidiFile() as outfile:
    track = MidiTrack()
    outfile.tracks.append(track)
newchord = firstchord

for x in range(11):
    newchord = getnextchord(newchord)
    delta = 200
    for i in range(3):
        
        track.append(Message('note_on', note=firstchord[i], velocity=100, time=0))
    for i in range(3):
        if i==0:
                    track.append(Message('note_off', note=firstchord[i], velocity=100, time=delta))
        else:
                    track.append(Message('note_off', note=firstchord[i], velocity=100, time=0))
                    


for x in range(30):
    newchord = getnextchord(newchord)
    delta = 200
    for i in range(3):
        
        track.append(Message('note_on', note=newchord[i], velocity=100, time=0))
    for i in range(3):
        if i==0:
                    track.append(Message('note_off', note=newchord[i], velocity=100, time=delta))
        else:
                    track.append(Message('note_off', note=newchord[i], velocity=100, time=0))
    print (newchord)
    outfile.save('seanstest.mid')

