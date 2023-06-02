import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


data_table = np.array(pandas.read_csv("radius_with_names.csv"))
data_dict = {}

for planet in data_table[0:, 0]:
    where = np.where(data_table[0:, 0] == planet)
    cum = []
    for place in where:
        cum.append(data_table[place, 1])
    data_dict[str(planet)] = np.mean(cum)

