# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:08:29 2018

@author: fahads99
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def find_steps(magnitude, threshold):
    """
    Summary:
    find_steps function is used to define conditions and serve as a
    purpose of monitoring the data in window frames and give the respective
    no. of step
    """
    pass_data1 = (DATA_SENSORS[magnitude] - DATA_SENSORS[magnitude].mean())
    peak, _ = find_peaks(pass_data1, height=threshold)
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
print("Number of steps : ", find_steps('RMS', 0))
#STEP_RATE = find_steps(0, 200, 'RMS', 5)/60
#print("Steps rate per second :", STEP_RATE)
print("total time in seconds:", TOTAL_TIME)

"""This section below will check the acquired light data and compare
at which level is the intensity of light.
According to National optical astronomy Observatory (NOAO)Common light
level outdoor at day & night measured in (Lux):
(1).Sunlight:107,527. (2)very Dark day:107 (3)twilight:10.8 (4)Full moon:0.108
(5). Cloudy day:1075
"""
LIGHT_SENSE = DATA_SENSORS['LIGHT (lux)']
SUN_LIGHT = 107527
CLOUDY_DAY = 1075
TWILIGHT = 10.8
FULL_MOON = 0.108
DARK_DAY = 107

MEAN_LIGHT = np.mean(LIGHT_SENSE)
print("mean light intensity", MEAN_LIGHT)

if MEAN_LIGHT < SUN_LIGHT:
    print("The intensity is very less than the typical Sunny day")
elif MEAN_LIGHT < CLOUDY_DAY:
    print("weather is more cloudy today")
elif MEAN_LIGHT < TWILIGHT:
    print("The sun is below the horizon")
elif MEAN_LIGHT < FULL_MOON:
    print("It is a full moon night")
elif MEAN_LIGHT < DARK_DAY:
    print("It is a pitch black day")
else:
    print("Quarter Moon")
"""This section below will check the acquired sound data and compare
at which level is the sound intensity.
According to report publised by "European Agency for safety and health at
work" on topic Noise figures measured in dB(A)(decibel levels):
(1)Whisper, countryside with rustling leaves: 50
(2)Quiet Office:45 (3). Normal conversation: 50 to 70
(4).dishwasher/lawnmover/kitchen:75 to 90
(5).headphones/powetools:90 to 100
"""
SOUND_BAR = DATA_SENSORS['SOUND LEVEL (dB)']
COUNTRY_SIDE = 50
QUIET_OFFICE = 45
NORMAL_CHAT = 60
KITCHEN_BUZZ = 80
HEADPHONES = 90
MEAN_SOUND = np.mean(SOUND_BAR)
print("mean sound intensity", MEAN_SOUND)
if MEAN_SOUND < COUNTRY_SIDE:
    print("Current state:Countryside with rustling leaves")
elif MEAN_SOUND < QUIET_OFFICE:
    print("professional life!")
elif MEAN_SOUND < NORMAL_CHAT:
    print("Current state:time for some chit chat")
elif MEAN_SOUND < KITCHEN_BUZZ:
    print("chopping,grinding / buzz of electronics")
elif MEAN_SOUND < HEADPHONES:
    print("Choatic area: Minus it out with Music")
else:
    print("The softest sound a person can hear with normal hearing")
    