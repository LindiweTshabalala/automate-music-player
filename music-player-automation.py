#!/usr/bin/env python3

import os

'''
playsong to run the script
'''

def choose_song():
    # song = input("What song would you like to play?")
    os.system('firefox music.youtube.com')


if __name__=='__main__':
    choose_song()