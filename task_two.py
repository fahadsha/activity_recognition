# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:08:29 2018

@author: fahads99
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def find_steps(lowerlimit, upperlimit, magnitude, threshold):
    """
    Summary:
    find_steps function is used to define conditions and serve as a
    purpose of monitoring the data in window frames and give the respective
    no. of steps, Light intensity and sound level
    """
    pass_data = DATA_SENSORS[magnitude].iloc[lowerlimit:upperlimit]
    peak, _ = find_peaks(pass_data, height=threshold)
    num_peak = len(peak)
    plt.figure(figsize=(10, 10))
    plt.plot(DATA_SENSORS[magnitude])
    plt.plot(peak, DATA_SENSORS[magnitude][peak], "x")
    plt.show()
    return num_peak


DATA_SENSORS = pd.read_csv('steps_found.csv')
ACC_X = DATA_SENSORS['ACCELEROMETER X (m/s²)']
ACC_Y = DATA_SENSORS['ACCELEROMETER Y (m/s²)']
ACC_Z = DATA_SENSORS['ACCELEROMETER Z (m/s²)']

TIME = DATA_SENSORS['Time since start in ms']
TOTAL_TIME = (TIME[155]-TIME[0])/1000 #time in seconds
print(DATA_SENSORS.head())

DATA_SENSORS['RMS'] = np.sqrt(sum(ACC_X)**2+(ACC_Y)**2+(ACC_Z)**2)
MEAN_VALUE = (sum(DATA_SENSORS['RMS'])/len(DATA_SENSORS['RMS']))
print("Number of steps : ", find_steps(0, 200, 'RMS', 0))
STEP_RATE = find_steps(0, 155, 'RMS', 10)/60
print("Steps rate per second :", STEP_RATE)
print("total time in seconds:", TOTAL_TIME)

"""
This section below will check the acquired light data and compare
at which level is the intensity of light. 
"""
LIGHT_SENSE = DATA_SENSORS['LIGHT (lux)']
MEAN_LIGHT = np.mean(LIGHT_SENSE)
print("mean light intensity", MEAN_LIGHT)
LIGHT_LEVEL = find_steps(0, 200, 'LIGHT (lux)', MEAN_LIGHT)
if LIGHT_LEVEL >= MEAN_LIGHT:
    print("Enjoy the sunshine")
elif LIGHT_LEVEL < MEAN_LIGHT:
    print("weather is more cloudy today")
else:
    print("it is nightime")
"""
This section below will check the acquired sound data and compare
at which level is the sound intensity.  
"""
SOUND_BAR = DATA_SENSORS['SOUND LEVEL (dB)']
MEAN_SOUND = np.mean(SOUND_BAR)
print("mean sound intensity", MEAN_SOUND)
SOUND_LEVEL = find_steps(0, 200, 'SOUND LEVEL (dB)', MEAN_SOUND)
if SOUND_LEVEL >= MEAN_SOUND:
    print("choatic area! put your headphones On!")
elif SOUND_LEVEL < MEAN_SOUND:
    print("Country side calmness")
else:
    print("it is nightime")
    