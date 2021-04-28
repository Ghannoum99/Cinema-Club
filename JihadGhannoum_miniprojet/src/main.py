# -*- coding: utf-8 -*-
from user import Utilisateur
from event import Evenement
from interface import Interface
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from PIL import Image, ImageTk
import calendar

def main():
    root = Tk()
    app= Interface(root)
    root.mainloop()

if __name__ == '__main__':
    main()