#!/usr/bin/env python

import mido 
import random
from mido import Message, MidiFile, MidiTrack


firstchord = [ ]
lick = [ ]


licklength = input("please enter licklength: ")
licklength = int(licklength)
for q in range(licklength):
    noteinput = input("please enter next lick note: ")
    noteinput = int(noteinput)
    lick.append(noteinput)

hordlength = input("please enter chordlength: ")
hordlength = int(hordlength)
for w in range(hordlength):
    chordnoteinput = input("please enter next chord note: ")
    chordnoteinput = int(chordnoteinput)
    firstchord.append(chordnoteinput)
skiplick = input("please enter lick skip factor: ")
skiplick = int(skiplick)
numchords = input("how many chords do you want? ")
numchords = int(numchords)

print("lick is: ")
print(lick)
print("first chord is: ")
print(firstchord)
print(" here's your chords my friend:  ")
print ("    ")





def startlaterinlick(x,y):
# list of diminished waylolick repeated

# uses modular function to return value of the lick
# starting y values from beginning
    return (lick[(x+y) % (licklength)])

def getnextchord(chord):
    for i in range(hordlength):

        chord[i] = chord[i] + startlaterinlick(x, i+skiplick )

    return(chord)

with MidiFile() as outfile:
    track = MidiTrack()
    outfile.tracks.append(track)
newchord = firstchord


                    


for x in range(numchords):
    newchord = getnextchord(newchord)
    delta = 200
    for z in range(hordlength):
        
        track.append(Message('note_on', note=newchord[z], velocity=100, time=0))
    for z in range(hordlength):
        if z==0:
                    track.append(Message('note_off', note=newchord[z], velocity=100, time=delta))
        else:
                    track.append(Message('note_off', note=newchord[z], velocity=100, time=0))
    print (newchord)
    outfile.save('seanstest.mid')

