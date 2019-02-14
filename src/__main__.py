from sound import Output

sound_device = Output()

while True:
    data = input("").strip()
    if data == ".":
        break
    sound_device.play(data)