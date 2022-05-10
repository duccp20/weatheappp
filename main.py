#Ngọc test'=
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

window = Tk()
window.title("Weather App")
window.geometry('900x500+300+200')
window.geometry('+%d+%d' % (300, 150))
window.resizable(FALSE, False)

# getweather


def getweather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I : %M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            city+"&appid=f17f6b26cb023da304d45eb16c6c35a9"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")


# search box
search_image = PhotoImage(file='search.png')
search_box = Label(image=search_image)
search_box.place(x=20, y=20)

textfield = tk.Entry(window, justify='center', width=17, font=(
    'poppins', 25, 'bold'), bg="#404040", border=0, fg='white')
textfield.place(x=50, y=40)
textfield.focus()

search_icon_image = PhotoImage(file='search_icon.png')
search_icon = Button(image=search_icon_image, borderwidth=0,
                     cursor='hand2', bg='#404040', command=getweather)
search_icon.place(x=400, y=34)

# logo
logo_image = PhotoImage(file='logo.png')
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box
bottom_box_image = PhotoImage(file='box.png')
bottom_box = Label(image=bottom_box_image)
bottom_box.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(window, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(window, font=('Helvetica', 20))
clock.place(x=30, y=130)
# Label
label1 = Label(window, text="Wind", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(window, text="HUMIDITY", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)

label3 = Label(window, text="DESCRIPTION", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)

label4 = Label(window, text="PRESSURE", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

# temperation
t = Label(font=('arial', 70, 'bold'), bg='#ee666d')
t.place(x=400, y=150)
# condition
c = Label(font=('arial', 15, 'bold'))
c.place(x=400, y=250)
# wind
w = Label(text="...", font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=120, y=430)
# humidity
h = Label(text="...", font=('arial', 20, 'bold'), bg='#1ab5ef')
h.place(x=280, y=430)
# description
d = Label(text="...", font=('arial', 20, 'bold'),
          bg='#1ab5ef')
d.place(x=430, y=430)
# pressure
p = Label(text="...", font=('arial', 20, 'bold'), bg='#1ab5ef')
p.place(x=670, y=430)
window.mainloop()
