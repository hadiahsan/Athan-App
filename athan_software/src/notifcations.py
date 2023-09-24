# notification.py
import time
from datetime import datetime, timedelta
import pygame  # Used to play the sound

def schedule_athan(timings, athan_file):
    while True:  # Keep the script running
        now = datetime.now()
        for prayer, time_str in timings.items():
            # Convert prayer time to datetime object
            time_obj = datetime.strptime(time_str, '%H:%M')
            
            # If the current time is equal to or later than the prayer time, play the Athan
            if now >= time_obj:
                print(f"Playing Athan for {prayer} at {time_obj}")
                play_athan(athan_file)
                
                # Update the timing for the next day
                timings[prayer] = (time_obj + timedelta(days=1)).strftime('%H:%M')
                
        time.sleep(60)  # Check every minute

def play_athan(athan_file):
    pygame.mixer.init()
    pygame.mixer.music.load(athan_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
