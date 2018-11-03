import matplotlib.pyplot as plt

def time_plot(data, group_by, plot_col, labels, x_lab, y_lab, title, fig_size = (15,7.5), ag_function = ['median']):
    '''
    Plots a line plot of plot_col vs group_by.
    data - dataframe
    group_by - string
    plot_col - string or list of strings
    x_lab, y_lab, title - string
    ag_function - list of strings (mean, median, or count)
    
    '''
    plt.figure(figsize=(fig_size))
    
    if 'str' in str(type(plot_col)):
        ag_function = ag_function[0]
        if ag_function.lower() == 'median':
            ax = data.groupby(group_by).median()[plot_col].plot(label = labels, legend = True);
        elif ag_function.lower() == 'count':
            ax = data.groupby(group_by).count()[plot_col].plot(label = labels, legend = True);
        else:
            ax = data.groupby(group_by).mean()[plot_col].plot(label = labels, legend = True);
    
    else:
        for i in range(len(labels)):
            if ag_function[i].lower() == 'median':
                ax = data.groupby(group_by).median()[plot_col[i]].plot(label = labels[i], legend = True);
            elif ag_function[i].lower() == 'count':
                ax = data.groupby(group_by).count()[plot_col[i]].plot(label = labels[i], legend = True);
            else:
                ax = data.groupby(group_by).mean()[plot_col[i]].plot(label = labels[i], legend = True);
        
    ax.set_title(title);
    ax.set_ylabel(y_lab);
    ax.set_xlabel(x_lab);
    plt.show();
