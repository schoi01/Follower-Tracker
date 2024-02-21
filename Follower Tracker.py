import time
import sys
import requests, re

from bs4 import BeautifulSoup
from tkinter import *
import instaloader


def create_widget():
    l1 = Label(start_window, text="Please log into your Instagram account:")
    l1.grid(row=0, column=1, columnspan=2)

    # label for username and password
    username_label = Label(start_window, text="Username: ")
    username_label.grid(row=1, column=0)
    pw_label = Label(start_window, text="Password: ")
    pw_label.grid(row=2, column=0)

    # entry space for username and password
    username_entry = Entry(start_window, width=20, textvariable=ig_username)
    username_entry.grid(row=1, column=1)
    pw_entry = Entry(start_window, width=20, textvariable=ig_pw)
    pw_entry.grid(row=2, column=1)

    # enter button for log in
    enter = Button(start_window, text="Enter", width=10, command=login)
    enter.grid(row=2, column=2)


def login():
    # destroy current window and open a new window after logging in
    start_window.destroy()
    login_window = Tk()
    login_window.title("Your profile")
    login_window.geometry(size)

    username = ig_username.get()
    pw = ig_pw.get()

    bot = instaloader.Instaloader()
    bot.login(user=username, passwd=pw)

    profile = instaloader.Profile.from_username(bot.context, username)

    followers = []
    count = 0
    for follower in profile.get_followers():
        followers.append(follower.username)
        count += 1

    print("# of followers: ", count)


# window size
size = "300x150"

# create window with assigned size
start_window = Tk()

# Set title and size for the window
start_window.title("Follower Tracker")
start_window.geometry(size)

ig_username = StringVar()
ig_pw = StringVar()

create_widget()

start_window.mainloop()
