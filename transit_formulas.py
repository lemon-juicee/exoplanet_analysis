import numpy as np
import math
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

def apparent_brightness():
    data = np.array(pandas.read_csv('pl_name,pl_orbsmax,st_num.csv'))
    brightness_dict = {}
    for name, orb, lum in data:
        lum = float(10) **  lum
        brightness = (149597870691 * orb) / (4. * float(math.pi) * float(lum) * 3.826 * 10**26)
        brightness_dict[name] = brightness
    return brightness_dict

def brightness_decrease():
    data = np.array(pandas.read_csv('pl_name,pl_rade,st_rad.csv'))
    brightness_loss = {}
    for name, pl_rade, st_rad in data:
        loss = ((pl_rade * 6378137) ** 2) / ((st_rad * 695700000) ** 2)
        brightness_loss[name] = loss
    return brightness_loss
