from prayer_times import get_prayer_times
from notifications import schedule_athan

latitude = "43.489690"
longitude = "-79.883970"
method = ""  # Refer to the API documentation for available methods
athan_file = "../assets/athan.mp3"

def main():
    timings = get_prayer_times(latitude, longitude, method)
    print(timings)
    schedule_athan(timings, athan_file)
    
if __name__ == "__main__":
    main()
