# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:57:07 2023

@author: User
"""

import datetime
import time
import winsound  # For Windows system, you can use other libraries for different operating systems

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm()
            break
        time.sleep(1)

def play_alarm():
    frequency = 2500  # Set the frequency in Hz
    duration = 3000  # Set the duration in milliseconds
    winsound.Beep(frequency, duration)

def main():
    print("Welcome to the Alarm Clock!")
    alarm_hour = int(input("Enter the hour (24-hour format): "))
    alarm_minute = int(input("Enter the minute: "))

    # Validate input
    if not (0 <= alarm_hour < 24) or not (0 <= alarm_minute < 60):
        print("Invalid input. Please enter a valid time.")
        return

    alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}:00"
    print(f"Alarm set for: {alarm_time}")

    set_alarm(alarm_time)
if __name__ == "__main__":
    main()
