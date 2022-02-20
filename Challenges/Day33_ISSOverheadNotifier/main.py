from inspect import Parameter
# 20/02/2022

from datetime import datetime
import requests
import schedule

LAT = 52.370216
LON = 4.895168

def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_lat = float(response.json()['iss_position']['latitude'])
    iss_lon = float(response.json()['iss_position']['longitude'])
    
    # return True if iss is nearby, else false
    return True if abs(LAT - iss_lat) <= 5 and abs(LON - iss_lon) <= 5 else False

def is_night():
        parameters = {
            "lat": LAT,
            "lng": LON,
            "formatted": 0
        }
        # check whether it is night
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
        sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
        cur_hour = datetime.datetime.now().hour
        
        return True if sunrise < cur_hour < sunset else False
    

def main():
    if iss_nearby() and is_night():
        print("ISS is nearby")
        
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



if __name__ == "__main__":
    # schedule.every().minutes.do(main)
    # while True:
    #     schedule.run_pending
    main()