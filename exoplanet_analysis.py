import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns


class Parameter:
    """Allow for importing of a certain parameter from the Exoplanet Archive."""

    def __init__(self, file, earth_value):
        """Initialize parameter from Exoplanet Archive data."""
        self.data = np.array(pandas.read_csv(file))
        self.dict = {planet:parameter for [planet, parameter] in self.data}
        self.ev = earth_value
    def plot_pdf(self, color = 'blue', show_earth = False, earth_color = 'black'):
        """Plot a kernel density estimate of the parameter's probability distribution function."""
        # Fill isn't perfect, but works rudimentarily
        # TODO : Establish better estimate of fill
        values = np.array(self.data[0:,1])
        median = np.median(values)
        sns.kdeplot(values, fill = True, color = color)
        ax = sns.kdeplot(values)
        kde_x = ax.get_lines()[-1].get_xdata()
        kde_y = ax.get_lines()[-1].get_ydata()
        if median > self.ev and show_earth:
            mask = kde_x < self.ev
            filled_x, filled_y = kde_x[mask], kde_y[mask]
            ax.fill_between(filled_x, y1=filled_y)
            plt.axvline(self.ev, 0, 1, color = earth_color)
        elif median < self.ev and show_earth:
            mask = kde_x > self.ev
            filled_x, filled_y = kde_x[mask], kde_y[mask]
            ax.fill_between(filled_x, y1=filled_y)
            plt.axvline(self.ev, 0, 1, color = earth_color)
        plt.show()
    def plot_cdf(self, show_earth = False, earth_color = 'black'):
        """Plot an empirical cumulative distribution function for the parameter."""
        # TODO : Affirm accuracy of shading
        # Fill is much more accurate than plot_pdf but may still need work
        values = np.array(self.data[0:,1])
        median = np.median(values)
        ax = sns.ecdfplot(values)
        ecdf_x = ax.get_lines()[-1].get_xdata()
        ecdf_y = ax.get_lines()[-1].get_ydata()
        if median > self.ev and show_earth:
            mask = ecdf_x < self.ev
            filled_x, filled_y = ecdf_x[mask], ecdf_y[mask]
            ax.fill_between(filled_x, y1=filled_y)
            plt.axvline(self.ev, 0, 1, color = earth_color)
        elif median < self.ev and show_earth:
            mask = ecdf_x > self.ev
            filled_x, filled_y = ecdf_x[mask], ecdf_y[mask]
            ax.fill_between(filled_x, y1=filled_y)
            plt.axvline(self.ev, 0, 1, color = earth_color)
        plt.show()


radius = Parameter('radius_with_names.csv', 1)
