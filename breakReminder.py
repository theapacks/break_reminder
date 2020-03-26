import time
import datetime
import ctypes

NUMBER_OF_ACTIVE_MINUTES=1
TIME_NOW=datetime.datetime.now()
NEXT_BREAK_TIME= TIME_NOW + datetime.timedelta(minutes=NUMBER_OF_ACTIVE_MINUTES)
print(TIME_NOW)
print(NEXT_BREAK_TIME)


while datetime.datetime.now() < NEXT_BREAK_TIME:
    time.sleep(1)

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
ctypes.windll.user32.MessageBoxW(0, "its time to take a break", "Break Reminder", 1)
