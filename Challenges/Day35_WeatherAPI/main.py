from tabnanny import check
import requests

LAT = 52.370216
LON = 4.895168

def get_hourly_API_data():
    url = "https://api.openweathermap.org/data/2.5/onecall?"
    params = dict(lat=LAT,
                lon=LON,
                appid="9abb843f5cc23aee14b330d2ab10557e",
                exclude=['current','minutely','daily']
                )

    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()['hourly']

def check_for_rain(data: dict) -> bool:
    # if the minimal id is less than 700 in the upcoming twelve hours, rain is expected
    min_id = min([sub['id'] for item in data[:12] for sub in item['weather']])
    return True if min_id < 700 else False
    

def main():
    weather_data = get_hourly_API_data()
    if check_for_rain(weather_data):
        print("It will rain somewhere in the upcoming twelve hours.")



if __name__ == "__main__":
    main()