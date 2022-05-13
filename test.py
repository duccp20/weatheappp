from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Lấy dữ liệu thời tiết hiện tại
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
        name.config(text="THỜI GIAN")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
              city + "&appid=f17f6b26cb023da304d45eb16c6c35a9"
        json_data = requests.get(api).json()
        data.clear()
        data.append(json_data)
    except:
        messagebox.showerror(title='Error',message='Không thể lấy dữ liệu thời tiết hiện tại')

#Hiển thị thông tin thời tiết hiện tại trên giao diện
def current_weather():
    getweather()
    if data == []:
        pass
    elif len(data[0]) == 2:
        messagebox.showerror(title='Error',message='Không tìm thấy địa điểm này')
    else:
        condition = data[0]['weather'][0]['main']
        description = data[0]['weather'][0]['description']
        temp = int(data[0]['main']['temp'] - 273.15)
        pressure = data[0]['main']['pressure']
        humidity = data[0]['main']['humidity']
        wind = data[0]['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
        if dv_toc_do_gio[0] == 'km/h':
            w.config(text=f'{wind} {dv_toc_do_gio[0]}')
        else:
            w.config(text=f'{round(wind / 3.6, 1)} {dv_toc_do_gio[0]}')
        h.config(text=humidity)
        d.config(text=description)
        if dv_ap_suat[0] == 'mBar':
            p.config(text=f'{pressure} {dv_ap_suat[0]}')
        else:
            p.config(text=f'{round(pressure * 0.750061, 2)} {dv_ap_suat[0]}')

def settings_window():
    def confirm():
        dv_toc_do_gio.clear()
        dv_toc_do_gio.append(wind_slection.get())
        dv_ap_suat.clear()
        dv_ap_suat.append(pressure_slection.get())
        st_window.destroy()
        current_weather()


    st_window = Toplevel()
    st_window.geometry('400x500')
    st_window.geometry('+%d+%d' % (800,150))
    st_window.title('Cài đặt')

    Label(st_window,text='Cài đặt',font=('arial',30)).place(x=10,y=10)

    setting_frame = Frame(st_window)
    setting_frame.place(x=10,y=60)
    # Thay đổi đơn vị tốc độ gió
    Label(setting_frame,text='Đơn vị tốc độ gió',font=(40)).grid(column=0,row=0)
    wind_slection = StringVar()
    wind_speed = ['km/h','m/s']
    wind_slection.set(dv_toc_do_gio[0])
    for i in range(len(wind_speed)):
        w_radiobutton = Radiobutton(setting_frame,text=wind_speed[i],font=30,value=wind_speed[i],variable=wind_slection)
        w_radiobutton.grid(column=i+1,row=0)

    # Thay đổi đơn vị áp suất
    Label(setting_frame, text='Đơn vị áp suất', font=(40)).grid(column=0, row=1,sticky=W)
    pressure_slection = StringVar()
    pressure = ['mBar', 'mmHg']
    pressure_slection.set(dv_ap_suat[0])
    for i in range(len(pressure)):
        p_radiobutton = Radiobutton(setting_frame,text=pressure[i],font=30,value=pressure[i],variable=pressure_slection)
        p_radiobutton.grid(column=i+1,row=1)

    chon = Button(st_window,text='OK',font=20,command=confirm)
    chon.place(x=350,y=450)

# Mặc định
data = []
dv_toc_do_gio = ['km/h']
dv_ap_suat =['mBar']


window = Tk()
window.title("Weather App")
window.geometry('900x500+300+200')
window.geometry('+%d+%d' % (300, 150))
window.resizable(FALSE, False)
# weather_icon = PhotoImage(file='weather.png')
# window.iconphoto(True,weather_icon)


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
                     cursor='hand2', bg='#404040', command=current_weather)
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
label1 = Label(window, text="Tốc độ gió", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=100, y=400)

label2 = Label(window, text="Độ ẩm", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=265, y=400)

label3 = Label(window, text="Trạng thái", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=420, y=400)

label4 = Label(window, text="Áp suất", font=(
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
w.place(x=100, y=430)
# humidity
h = Label(text="...", font=('arial', 20, 'bold'), bg='#1ab5ef')
h.place(x=280, y=430)
# description
d = Label(text="...", font=('arial', 20, 'bold'),
          bg='#1ab5ef')
d.place(x=390, y=430)
# pressure
p = Label(text="...", font=('arial', 20, 'bold'), bg='#1ab5ef')
p.place(x=630, y=430)

setting_button = Button(window,text='Cài đặt',command=settings_window)
setting_button.place(x=840,y=10)

window.mainloop()
