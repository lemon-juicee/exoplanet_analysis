import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


class Parameter:
    def __init__(self, file, earth_value):
        self.data = np.array(pandas.read_csv(file))
        self.dict = {planet:parameter for [planet, parameter] in self.data}
        self.ev = earth_value
    def plot(self, color = 'blue', show_earth = False, earth_color = 'black'):
        values = np.array(self.data[0:,1])
        median = np.median(values)
        sns.kdeplot(values, fill = True)
        ax = sns.kdeplot(values)
        kde_x = ax.get_lines()[-1].get_xdata()
        kde_y = ax.get_lines()[-1].get_ydata()
        if median > self.ev and show_earth:
            mask = kde_x < self.ev
            filled_x, filled_y = kde_x[mask], kde_y[mask]
            ax.fill_between(filled_x, y1=filled_y)
            earth_line = plt.axvline(self.ev, 0, 1, color = earth_color)
        elif median < self.ev and show_earth:
            mask = kde_x > self.ev
            filled_x, filled_y = kde_x[mask], kde_y[mask]
            ax.fill_between(filled_x, y1=filled_y)
            earth_line = plt.axvline(self.ev, 0, 1, color = earth_color)
        plt.show()

radius = Parameter('radius_with_names.csv', 1)
