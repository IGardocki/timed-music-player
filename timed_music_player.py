import schedule
import time
import pygame
import os

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("item_0.wav")
    pygame.mixer.music.play()

def job():
    print("Playing song")
    play_song()

if __name__ == "__main__":
    # Change to the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Schedule the job to run
    schedule.every().day.at("23:36").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
