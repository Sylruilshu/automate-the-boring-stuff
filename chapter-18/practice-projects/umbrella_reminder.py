import requests, bs4, text_me


WEATHER_URL = "https://www.weatherzone.com.au/STATE/CITY/CITY"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def check_weather() -> None:
    response = requests.get(WEATHER_URL, headers=HEADERS)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "lxml")
    forecast_element = soup.select(".sc-5f4db150-7")
    temperature_element = soup.select(".sc-5f4db150-5")
    weather_details = soup.select(".sc-5f4db150-12")

    forecast = forecast_element[0].text
    temperature_details = temperature_element[0].text
    chance_of_rain = weather_details[0].text
    amount_of_rain = weather_details[1].text
    fire_danger_rating = weather_details[2].text
    UV_index = weather_details[3].text

    temperature = temperature_details.split("C")

    chance_of_rain_without_percent = chance_of_rain[:-1]

    text_message = f"""Temperature: {temperature[0]}C-{temperature[1]}C
                    \nChance of rain: {chance_of_rain} 
                    \nUV Index: {UV_index} 
                    \nForecast: \n{forecast} 
                    \nAmount of rain: {amount_of_rain} 
                    \nFire danger rating: {fire_danger_rating}"""

    if int(chance_of_rain_without_percent) >= 60:
        text_message = text_message + "\n\nDont forget to pack an umbrella!"

    # text_me.text_myself(text_message)
    print(text_message)


check_weather()
