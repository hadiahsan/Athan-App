# notification.py
import time
from datetime import datetime, timedelta
import pygame  # Used to play the sound

def schedule_athan(timings, athan_file):
    for prayer, time_str in timings.items():
        # Convert prayer time to datetime object
        time_obj = datetime.strptime(time_str, '%H:%M')
        
        # Calculate the delay in seconds
        now = datetime.now()
        delay = (time_obj - now).total_seconds()
        
        if delay > 0:
            print(f"Scheduling {prayer} at {time_obj}")
            # Schedule the Athan
            time.sleep(delay)
            play_athan(athan_file)

def play_athan(athan_file):
    pygame.mixer.init()
    pygame.mixer.music.load(athan_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
