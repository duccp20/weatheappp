import imghdr
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

window = Tk()
window.geometry('900x500')
data = [1, 2, 3, 'a']

if data[3] == 'a':
    canvas = Canvas(window, width=900, height=500)
    canvas.pack(fill='both', expand=True)
    bg = ImageTk.PhotoImage(Image.open("box.png"))
    canvas.create_image(0, 0, image=bg, anchor="nw")

window.mainloop()
