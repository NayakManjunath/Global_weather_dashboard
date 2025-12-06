import requests 
import matplotlib.pyplot as plt

API_KEY = "your api key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    params = {

        "q" : city,
        "appid" : API_KEY,
        "units" :"metric"
    }
    response = requests.get(BASE_URL,params = params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data", response.status_code)
        return None
    
def display_weather_data(data):
    print(f"City : {data ['name']}")
    print(f"Temperature : { data ['main']['temp']}^C")
    print(f"Weather : { data ['weather'][0]['description'].title()}^C")
    print(f"Humidity : { data ['main']['humidity']}%")
    print(f"Temperature : { data ['wind']['speed']} m/sC")

def plot_weather_trend(days,temperature):
    plt.plot(days,temperature, marker ='0', color = 'blue')
    plt.title("Temperature Trend")
    plt.xlabel("Days")
    plt.ylabel("Temperature(^C)")
    plt.grid()
    plt.show()

def compare_weather(cities):
    temp =[]
    for City in cities:
        data = fetch_weather_data(city)
        if data:
            temp.append((city, data['main']['temp']))
            City_names = [t[0] for t in temps]
            City_temps = [t[1] for t in temps]
            plt.bar(City_names, City_temps, clolor = 'light orange')
            plt.title("Temperature Comparison")
            plt.xlabel("City")
            plt.ylabel("Temperature(^C)")
            plt.show()

def main():
    print("Welcome to the Global Weather Dashboard!")
    while True:
        print("1.View Weather for a City")
        print("2. Compare weather for multiple Cities")
        print("3.exit")
        choice = input(" choose an option:")

        if choice == "1":
            City = input ("Enter the City Name:")
            weather_data = fetch_weather_data(City)
            if weather_data:
                display_weather_data(weather_data)
            elif choice =="2":
                Cities = input("Enter City names separated by comas:").split(",")
                compare_weather([city.strip() for city in cities])
            elif choice == "3":
                print("Good bye!") 
                break
        else:
            print("Invalid choice. please try again!")   

if __name__ == "__main__":
    main()

