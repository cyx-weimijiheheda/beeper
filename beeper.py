from time import sleep
import json
from winsound import Beep as beep

BEAT = 1000

with open("dict.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def play_note(note, beat=1):
    time = int(BEAT*beat)
    if note == "0":
        sleep(time/1000)
    else:
        frequence = data[note]
        beep(frequence, time)

def play_music(text):
    notes = text.split()
    for n in notes:
        note, bt = n.split(":")
        print(note)
        play_note(note, float(bt))

def main():
    with open("In.txt", "r", encoding="utf-8") as f:
        music = f.read()
    play_music(music)

if __name__ == "__main__":
    main()
