import matplotlib.pyplot as plt

def time_plot(x, y, label, title, x_lab, y_lab, fig_size = (15,7.5)):
    '''
    Plots a line plot of plot_col vs group_by.
    data - dataframe
    group_by - string
    plot_col - string or list of strings
    x_lab, y_lab, title - string
    ag_function - list of strings (mean, median, or count)
    
    '''
    plt.figure(figsize=(fig_size))
    
    if 'str' in str(type(label)):
        label = [label]
        y = [y]
    
    for i in range(len(label)):
        plt.plot(x, y[i], label = label[i]);
    plt.legend();
    plt.title(title);
    plt.ylabel(y_lab);
    plt.xlabel(x_lab);
    plt.show();