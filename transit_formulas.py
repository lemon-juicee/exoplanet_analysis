import numpy as np
import math
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import tools

def apparent_brightness():
    data = tools.data_from_csv('pl_name,pl_orbsmax,st_num.csv')
    brightness_dict = {}
    for name, orb, lum in data:
        lum = float(10) **  lum
        brightness = (149597870691 * orb) / (4. * float(math.pi) * float(lum) * 3.826 * 10**26)
        brightness_dict[name] = brightness
    return brightness_dict

def brightness_decrease(name):
    data = tools.data_from_csv(name)
    brightness_loss = {}
    for name, pl_rade, st_rad in data:
        loss = ((pl_rade * 6378137) ** 2) / ((st_rad * 695700000) ** 2)
        brightness_loss[name] = loss
    return brightness_loss

def decrease_transit_rv():
    transit_data = np.array(list(brightness_decrease('transit,pl_name,pl_rade,st_rad.csv').values()))
    rv_data = np.array(list(brightness_decrease('rv,pl_name,pl_rade,st_rad.csv').values()))
    plt.hist(transit_data, range = (0, 1), color = 'red', bins = 1000, alpha = 0.5, weights=np.ones_like(transit_data) / np.size(transit_data))
    plt.hist(rv_data, range = (0, 1), color = 'blue', bins = 1000, alpha = 0.5, weights=np.ones_like(rv_data) / np.size(rv_data))
    plt.show()

