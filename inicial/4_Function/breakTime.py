'''
breakTime uses import: webbrowser and time
	Establishes a number of breaktimes and the interval between them.
	At these intervals you will open a default web page for breaktime
'''

import webbrowser
import time 

def breakTime(url, wait,turn):
    
    i = 1
    
    while True:
        
        webbrowser.open(url, new=2)
        time.sleep(wait*60)
        i = i + 1
        
        if(i > turn):
            break

url = input('Enter the URL you want to access: ')
wait = float(input('Enter the frequency in minutes of breakTime: '))
turn = int(input('Enter the amount of breakTime of the day: '))

breakTime(url, wait, turn)
