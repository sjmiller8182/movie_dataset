import matplotlib.pyplot as plt
from scipy.stats import linregress as linreg
import numpy as np

def time_plot(x, y, label, title = None, x_lab = None, y_lab = None, fig_size = (15,7.5)):
    '''
    Plots a line plot of plot_col vs group_by.
    data - dataframe
    group_by - string
    plot_col - string or list of strings
    x_lab, y_lab, title - string
    '''
    plt.figure(figsize=(fig_size))
    
    if 'str' in str(type(label)):
        label = [label]
        y = [y]
    
    for i in range(len(label)):
        plt.plot(x, y[i], label = label[i]);
    plt.legend();
    if title is not None:
        plt.title(title);
    if y_lab is not None:
        plt.ylabel(y_lab);
    if x_lab is not None:
        plt.xlabel(x_lab);
    plt.show();
    
def bar(pos, height, labels = None, title = None, x_lab = None, y_lab = None, fig_size = (15,7.5)):
    '''
    Makes a bar chart from positions (pos) and heights. Use labels to replace pos elements.
    pos - positions of bars in chart
    height - heights of bars
    labels - labels for position vector
    x_lab, y_lab, title - string
    '''
    plt.figure(figsize=(fig_size));
    plt.bar(pos, height);
    if labels is not None:
        plt.xticks(pos,labels);
    if title is not None:
        plt.title(title);
    if y_lab is not None:
        plt.ylabel(y_lab);
    if x_lab is not None:
        plt.xlabel(x_lab);
    plt.show();
    
def _make_reglin_labels(r2, pV, stdE, parms):
    label = list()
    params = ['r2: ','p-V: ', 'stdE: ']
    r2 = np.round(r2, 2)
    pv = np.round(pV, 2)
    stdE = np.round(stdE, 2)
    for p in parms:
        if p == 'r2':
            label.append(params[0] + str(r2))
        elif p == 'pV':
            label.append(params[1] + str(pv))
        elif p == 'stdE':
            label.append(params[2] + str(stdE))
        else:
            pass
    return '\n'.join(label)

def scatter(x, y, label = None, title = None, x_lab = None, y_lab = None, add_trend_line = False, line_color = 'r', line_char = None, fig_size = (15,7.5)):
    '''
    Makes a bar chart from positions (pos) and heights. Use labels to replace pos elements.
    '''
    plt.figure(figsize=(fig_size));
    
    plt.scatter(x, y, label = label);
    if add_trend_line:
        m, b, r2, pv, std_error = linreg(x,y)
        lab = ''
        if line_char is not None:
            lab = _make_reglin_labels(r2, pv, std_error, line_char)
        else:
            lab = None
        plt.plot(x, m * x + b,'-', c = line_color, label = lab)
    plt.legend()
    if title is not None:
        plt.title(title);
    if y_lab is not None:
        plt.ylabel(y_lab);
    if x_lab is not None:
        plt.xlabel(x_lab);
    plt.show();