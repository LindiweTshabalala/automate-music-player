#!/usr/bin/env python3

import os
import urllib.request
import re
import webbrowser

'''
playsong to run the script
'''

def choose_song():
    song = input("What video would you like to play?")
    song = "".join(song.split(" "))
    url_ = urllib.request.urlopen("https://www.youtube.com/results?search_query="+song)
    video = re.findall(r"watch\?v=(\S{11})",url_.read().decode())

    webbrowser.open("https://www.youtube.com/watch?v="+video[0])


if __name__=='__main__':
    choose_song()