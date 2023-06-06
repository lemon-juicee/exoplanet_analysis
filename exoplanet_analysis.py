import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


data_table = np.array(pandas.read_csv("radius_with_names.csv"))
data_dict = {planet:radius for [planet, radius] in data_table}
earth_value = 1

sns.kdeplot([planet[1] for planet in data_table])
plt.axvline(earth_value, 0, 1, color = 'black')
plt.show()