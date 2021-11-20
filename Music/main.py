import threading
import time
import pygame, mutagen.mp3

FN = 1/1
HN = 1/2
QN = 1/4
EN = 1/8
SN = 1/16
TN = 1/32
sN = 1/64


def play(note, dur):
    print(note, dur)
    song_file = "notes/" + note + ".mp3"
    mp3 = mutagen.mp3.MP3(song_file)
    pygame.mixer.init(frequency=mp3.info.sample_rate)
    s = pygame.mixer.Sound(song_file)
    c = s.play(maxtime=int(1024 * dur))
    while c.get_busy():
       pygame.time.delay(100)

def play_chord(notes, dur):
    chord = []
    for n in notes:
        chord.append(threading.Thread(target=play, kwargs={'note': n, 'dur': dur}))
    for c in chord:
        c.start()
    for c in chord:
        c.join()
        

def e_flat_minor_7(dur):
    play_chord([
        'Eb3',
        'Gb3',
        'Bb3',
        'Db3'
    ], dur)

def e_minor_7(dur):
    play_chord([
        'E3',
        'G3',
        'B3',
        'D3'
    ], dur)

for i in range(5):
    e_flat_minor_7(HN)
    time.sleep(SN)
    e_flat_minor_7(HN)
    time.sleep(SN)
    e_flat_minor_7(HN)
    time.sleep(SN)
    e_minor_7(FN+HN)
    time.sleep(SN)
