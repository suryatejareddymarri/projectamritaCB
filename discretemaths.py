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

    if output:

        melody.append(note)

        # Show information
        info.config(
            text=f"Note: {note}   Frequency: {frequency} Hz"
        )

        logic.config(
            text="AND = 1    OR = 1    NOT = 0"
        )

        # Create sound
        create_sound(frequency)


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

            value = math.sin(
                2 * math.pi * frequency * i / sample_rate
            )

            data = struct.pack(
                "<h",
                int(value * 15000)
            )

            sound.writeframes(data)

    winsound.PlaySound(
        filename,
        winsound.SND_FILENAME
    )


# -----------------------------------
# 5. SHOW MELODY
# -----------------------------------

def show_melody():

    if melody:

        melody_text.config(
            text="Melody: " + " → ".join(melody)
        )

    else:

        melody_text.config(
            text="Melody: Empty"
        )


# -----------------------------------
# 6. SIMPLE AI MELODY GENERATION
# -----------------------------------

def generate_ai():

    if len(melody) < 2:

        info.config(
            text="Select at least 2 notes first."
        )

        return

    # Simple pattern-based generation
    new_melody = melody.copy()

    new_melody.append(melody[-2])
    new_melody.append(melody[-1])

    melody_text.config(
        text="AI Melody: " + " → ".join(new_melody)
    )

    info.config(
        text="AI generated a new melody pattern."
    )


# -----------------------------------
# 7. CLEAR MELODY
# -----------------------------------

def clear_melody():

    melody.clear()

    melody_text.config(
        text="Melody: Empty"
    )

    info.config(
        text="Melody cleared."
    )


# -----------------------------------
# 8. GUI WINDOW
# -----------------------------------

window = tk.Tk()

window.title(
    "Music Composer Using Logic Gates"
)

window.geometry("800x500")


# Title

title = tk.Label(
    window,
    text="🎵 MUSIC COMPOSER USING LOGIC GATES",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)


# Information

info = tk.Label(
    window,
    text="Select a musical note",
    font=("Arial", 14)
)

info.pack(pady=10)


# Logic gate information

logic = tk.Label(
    window,
    text="AND = 0    OR = 0    NOT = 1",
    font=("Arial", 12)
)

logic.pack(pady=5)


# -----------------------------------
# NOTE BUTTONS
# -----------------------------------

button_frame = tk.Frame(window)

button_frame.pack(pady=30)


for note in notes:

    button = tk.Button(
        button_frame,
        text=note,
        width=7,
        height=3,
        font=("Arial", 12, "bold"),
        command=lambda n=note: play_note(n)
    )

    button.pack(
        side="left",
        padx=3
    )


# -----------------------------------
# MELODY DISPLAY
# -----------------------------------

melody_text = tk.Label(
    window,
    text="Melody: Empty",
    font=("Arial", 13)
)

melody_text.pack(pady=15)


# -----------------------------------
# CONTROL BUTTONS
# -----------------------------------

play_melody_button = tk.Button(
    window,
    text="SHOW MELODY",
    command=show_melody,
    width=15
)

play_melody_button.pack(pady=5)


ai_button = tk.Button(
    window,
    text="🤖 AI GENERATE",
    command=generate_ai,
    width=15
)

ai_button.pack(pady=5)


clear_button = tk.Button(
    window,
    text="CLEAR",
    command=clear_melody,
    width=15
)

clear_button.pack(pady=5)


# -----------------------------------
# START PROGRAM
# -----------------------------------

window.mainloop()