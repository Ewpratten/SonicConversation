from rawaudio import sine_tone
import time

sound_lookup = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":"..-",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----."
}

class Output(object):
    def __init__(self):
        self.buffer = []
        self.duration = 0.1
    
    def dit(self):
        sine_tone(440, self.duration)
    
    def dah(self):
        sine_tone(480, self.duration)

    def play(self, data:str):
        self.buffer = [i for i in data]

        for char in self.buffer:
            if char == " ":
                time.sleep(self.duration * 2)
            
            if char not in sound_lookup:
                continue
            
            sequence = sound_lookup[char]
            for sound in sequence:
                if sound == "-":
                    self.dah()
                if sound == ".":
                    self.dit()
            
            time.sleep(self.duration)