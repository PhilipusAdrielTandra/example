import os
import time
from playsound import playsound
from threading import Thread
mp3 = "OUTRO.mp3"
seconds = 16
def play_music():
    playsound("OUTRO.mp3")

t = Thread(target = play_music)
t.daemon = True
t.start()

start_time = time.time()
while (time.time() - start_time) < 19:
    seconds -= 1
    print("See you guys in", seconds)
    time.sleep(1)
    if seconds <= 0:
        print("SEE YOU GUYS")

# os.system("shutdown /s /t 1")
