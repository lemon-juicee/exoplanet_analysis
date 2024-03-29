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

def final_luminosity(name):
    data = tools.data_from_csv(name)
    total_brightness_loss = {}
    for name, pl_rade, st_rad, st_lum in data:
        loss = ((pl_rade * 6378137) ** 2) / ((st_rad * 695700000) ** 2)
        lum = 10 ** st_lum
        total_loss = loss * lum
        total_brightness_loss[name] = total_loss
    return total_brightness_loss

def decrease_transit_other(other):
    transit_data = np.array(list(brightness_decrease('transit,pl_name,pl_rade,st_rad.csv').values()))
    other_data = np.array(list(brightness_decrease(other + ',pl_name,pl_rade,st_rad.csv').values()))
    plt.hist(transit_data, range = (0, 1), color = 'red', bins = 1000, alpha = 0.5, weights=np.ones_like(transit_data) / np.size(transit_data))
    plt.hist(other_data, range = (0, 1), color = 'blue', bins = 1000, alpha = 0.5, weights=np.ones_like(other_data) / np.size(other_data))
    plt.show()

def final_lums_transit_other(other):
    transit_data = np.array(list(final_luminosity('transit,pl_name,pl_rade,st_rad,st_lum.csv').values()))
    other_data = np.array(list(final_luminosity(other + ',pl_name,pl_rade,st_rad,st_lum.csv').values()))
    plt.hist(transit_data, range = (0, 1), color = 'red', bins = 1000, alpha = 0.5, weights=np.ones_like(transit_data) / np.size(transit_data))
    plt.hist(other_data, range = (0, 1), color = 'blue', bins = 1000, alpha = 0.5, weights=np.ones_like(other_data) / np.size(other_data))
    plt.show()
