import musicalbeeps

player = musicalbeeps.Player(volume = 1.0, mute_output = False)

FN = 1/1
HN = 1/2
QN = 1/4
EN = 1/8
SN = 1/16
TH = 1/32
sN = 1/64

savage = ['''
    E2b     QN
    pause   EN
    E2b     QN
    pause   EN
    E2b     QN
    pause   EN
    E2      FN*2
    pause   EN
''']

for track in savage:
    lines = [l.strip() for l in track.strip().split('\n')]
    for note in lines:
        chunks = note.split(' ')
        key = chunks[0]
        dur = eval(chunks[-1])
        player.play_note(key, dur)
