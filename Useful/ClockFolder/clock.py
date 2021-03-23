import os
from time import sleep
from time import localtime
from datetime import datetime

class Clock:
    def __init__(self):
        pass


    def timer(sec=0, minute=0, hour=0):

        'this function is a simple timer'

        secs = sec
        minutes = minute
        hours = hour

        while True:
            secs += 1
            if secs == 60:
                secs = 0
                minutes += 1
            
            elif minutes == 60:
                minutes = 0
                hours += 1
            
            elif hours == 24:
                break
            
            if secs < 10:
                zeroS = '0'
            
            else:
                zeroS = ''
            
            if minutes < 10:
                zeroM = '0'
            
            else:
                zeroM = ''
            
            if hours < 10:
                zeroH = '0'
            
            else:
                zeroH = ''
            
            print(f'{zeroH}{hours}:{zeroM}{minutes}:{zeroS}{secs}')

            sleep(1.0)
            os.system('cls')


    def realTime(alls=False, clockDefalt=False, calendarDefalt=False):

        'returns the real time'

        if alls == True:
            return datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        
        elif alls == False:
            if clockDefalt == True:
                hour = datetime.now().strftime('%H:')
                minute = datetime.now().strftime('%M:')
                secs = datetime.now().strftime('%S')

                return f'{hour}{minute}{secs}'
            
            elif calendarDefalt == True:
                year = datetime.now().strftime('%Y')
                month = datetime.now().strftime('%m')
                day = datetime.now().strftime('%d')

                return f'{day}/{month}/{year}'

    