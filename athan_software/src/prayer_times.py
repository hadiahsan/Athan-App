import requests

def get_prayer_times(latitude, longitude, method):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={Milton}&country={Ontario}&method={method}"
    response = requests.get(url)
    data = response.json()
    timings = data['data']['timings']
    return timings
