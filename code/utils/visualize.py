import matplotlib.pyplot as plt
import seaborn as sns

def custom_histogram(data, column, bin_size=0, fig_size=(15, 9), x_log=False, y_log=False, save_file=False):
    """Creates a histogram based on specified customizations

    :param DataFrame data: data of interest
    :param str column: name of column containing values of interest
    :param int bin_size: bin_size to group values by for histogram
    :param fig_size: figure dimensions
    :type fig_size: tuple of (int, int)
    :param bool x_log: specify log transformation of x-axis
    :param bool y_log: specify log transformation of y-axis
    :param bool save_file: save graph image as png file
    """

    if bin_size:
        # Minium value
        min_val = data[column].min()
        # Maximum value
        max_val = data[column].max()
        # Number of bins
        range_of_values = max_val - min_val
        num_bins = range_of_values / bin_size
        # print("With a bin size of {}, the data can be broken into {} bins.".format(bin_size, int(num_bins)))

    # Graph Theme
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})

    # Set graph size
    plt.figure(figsize=fig_size)

    # If bin_size specified, use that value, otherwise, use seaborn's default optimized binsize
    if bin_size:
        ax = sns.distplot(data[column], bins=int(num_bins))
    else:
        ax = sns.distplot(data[column])

    # Set labels
    ax.set_xlabel(column, fontsize=20)
    ax.set_ylabel('Frequency', fontsize=20)

    # log transform axis
    if x_log:
        ax.set_xscale('log')
    if y_log:
        ax.set_yscale('log')

    # Save graph
    if save_file:
        fig = ax.get_figure()
        fig.savefig('{}.png'.format(column))
