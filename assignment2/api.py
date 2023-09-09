import requests

# Api used:-
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# My Api Key:-
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def get_weather_data(city, api_key):
    url = f"{BASE_URL}q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to the data.")
        return None

def get_temperature(data, date_time):
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['main']['temp']
    return None

def get_wind_speed(data, date_time):
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['wind']['speed']
    return None

def get_pressure(data, date_time):
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['main']['pressure']
    return None

def main():
    city = input("Enter city (London as per api) ")
    weather_data = get_weather_data(city, API_KEY)

    if weather_data is not None:
        while True:
            print("\nOptions:")
            print("1. Get Temperature")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")

            option = input("Select an option: ")

            if option == '1':
                date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
                temperature = get_temperature(weather_data, date_time)
                if temperature is not None:
                    print(f"Temperature at {date_time}: {temperature} K")
                else:
                    print("Data not found!")

            elif option == '2':
                date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
                wind_speed = get_wind_speed(weather_data, date_time)
                if wind_speed is not None:
                    print(f"Wind Speed at {date_time}: {wind_speed} m/s")
                else:
                    print("Data not found!")

            elif option == '3':
                date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
                pressure = get_pressure(weather_data, date_time)
                if pressure is not None:
                    print(f"Pressure at {date_time}: {pressure} hPa")
                else:
                    print("Data not found!")

            elif option == '0':
                print("Exiting program!")
                break

            else:
                print("Invalid option!")

if __name__ == "__main__":
    main()
