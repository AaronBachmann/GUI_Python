import tkinter as tk
from tkinter import font
import requests
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
root.title("Get Weather")

HEIGHT = 500
WIDTH = 600

#api weather 5 day: api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
#api key: d661022f234f12894022d21699605f47


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        sunrise = weather['sys']['sunrise']
        sunset = weather['sys']['sunset']

        weather_output = 'City: %s \nConditions: %s \nTemperature (°F): %s \n Low: %s \n High: %s \n Humidity: %s \n Wind Velocity: %s' % (name, desc, temp, temp_min, temp_max, humidity, wind)
    except:
        weather_output = "There was a problem retrieving that information."

    return weather_output

def get_weather(city):
    weather_key = 'd661022f234f12894022d21699605f47'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    #print(weather)

    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('C:/Users/Aaron/PycharmProjects/100DaysPython/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk. PhotoImage(file="bitday_wallpaper_clock_1_0.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#D9FCBC", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg="#FFFFD0", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

entry = tk.Entry(frame, font=("Calibri", 14))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

label = tk.Label(lower_frame, font=("Calibri", 14))
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()