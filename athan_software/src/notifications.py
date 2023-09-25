# notification.py
import time
from datetime import datetime, timedelta
import pygame  # Used to play the sound

def schedule_athan(timings, athan_file):
    while True:
        now = datetime.now()
        for prayer, time_str in timings.items():
            time_obj = datetime.strptime(time_str, '%H:%M')
            
            # Calculate the difference between the current time and the prayer time
            time_diff = now - time_obj
            
            # If the current time is within 5 minutes of the prayer time, play the Athan
            if 0 <= time_diff.total_seconds() < 300:  # 300 seconds = 5 minutes
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
