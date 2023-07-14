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
