from kubot.core.handlers import cmd
import requests
import os

@cmd("weather", help_text="Get weather for a given zip code")
def adduser(args, message, say):
    if len(args) < 1:
        say("""```Syntax: weather <zip code>```""")
        return
    zip_code = args[0]
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + os.environ["OPENWEATHERMAP_API_KEY"] + "&units=imperial&zip=" + zip_code
    r = requests.get(url)
    result = r.json()

    city = result['name']
    temperature = round(result['main']['temp'])
    temp_feels = round(result['main']['feels_like'])
    temp_low = round(result['main']['temp_min'])
    temp_high = round(result['main']['temp_max'])
    wind_speed = round(result['wind']['speed'])

    blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Weather for {city}"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*:thermometer: Temperature:*\n{temperature}F (Feels like {temp_feels}F)"
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*:arrow_upper_right: High:*\n{temp_high}F"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*:arrow_lower_right: Low:*\n{temp_low}F"
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*:wind_blowing_face: Wind Speed:*\n{wind_speed} mph"
                }
            ]
        }
    ]
    
    for condition in result['weather']:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Condition:* {condition['main']}"
            }
        })
    
    say(text=f"Weather for {city} - {temperature}F"
        ,blocks=blocks)