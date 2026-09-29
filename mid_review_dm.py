import tkinter as tk
import math
import wave
import struct
import winsound

# -----------------------------------
# 1. MUSICAL NOTES AND FREQUENCIES
# -----------------------------------

notes = {
    "Sa": 262,
    "Ri": 294,
    "Ga": 330,
    "Ma": 349,
    "Pa": 392,
    "Da": 440,
    "Ni": 494,
    "Sa'": 523
}

melody = []

# -----------------------------------
# 2. LOGIC GATES
# -----------------------------------

def AND_gate(a, b):
    return a and b


def OR_gate(a, b):
    return a or b


def NOT_gate(a):
    return not a


# -----------------------------------
# 3. PLAY MUSICAL NOTE
# -----------------------------------

def play_note(note):

    frequency = notes[note]

    # Logic gate operation
    play = 1
    note_selected = 1

    output = AND_gate(play, note_selected)

    # Create sound only if the logic gate output is true
    if output:
        create_sound(frequency)

    return output


# -----------------------------------
# 4. CREATE SOUND
# -----------------------------------

def create_sound(frequency):

    sample_rate = 44100
    duration = 0.4

    filename = "note.wav"

    with wave.open(filename, "w") as sound:

        sound.setnchannels(1)
        sound.setsampwidth(2)
        sound.setframerate(sample_rate)

        for i in range(int(sample_rate * duration)):

            value = math.sin(2 * math.pi * frequency * (i / sample_rate))

            data = struct.pack("<h",int(value * 15000))

            sound.writeframes(data)

    winsound.PlaySound(filename,winsound.SND_FILENAME)

# -----------------------------------
# 7. CLEAR MELODY
# -----------------------------------

def clear_melody():

    melody.clear()
