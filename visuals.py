import matplotlib.pyplot as plt


def line_plot(data, group_col, plot_col, ag_function = None, labels = None, x_lab = None, y_lab = None, title = None, fig_size = (15,7.5)):
	""" 
	Plots a histogram of data in a dataframe based on a column to group by (x-axis) and plot columns (y-axis). 
	Takes in a dataframe (pd.DataFrame) as data; first positional arg.
	Takes in a column name to group by - this will be used as the x-axis. Second positional arg.
	Takes in a column names to plot on the y-axis (list or dict) - this will be used as the x-axis. Third positional arg.
		in case of dict, keys are column names and items are labels.
		
	Optional kwargs:
	ag_function - DataFrame aggragation functions
	labels - list of labels for each plot_col
	x_lab - x-axis label
	y_lab - y-axis label
	title - title of plot
	fig_size - size of plot; tuple as (x size, y size)
	"""
	
	# set the plot size
	plt.figure(figsize=fig_size)
	
	# create list from plt_col input
	if type(plot_col) = dict():
		l = list()
		labels = list()
		leg = True
		for key in dict.keys
			l = l + list(key)
			labels = labels + list(plot_col[key])
	else:
		plot_col = list(plot_col)
		
	num_plot_cols = len(plot_col)
	
	
	if labels is not None:
		leg = True
	else:
		labels = [None for _ in range(num_plot_cols)]
		leg = False
	
	if ag_function is not None:
		num_ag_functions = len(ag_function)
	
	# set the result of the plot function to ax on the last iteration
	for i in range(num_plot_cols):
		
		# need a "case" statement for the aggragation functions?
		if ag_function is not None:
			for j in len(ag_function):
				if i == len(num_plot_cols) - 1 && j == len(num_ag_functions) - 1:
					ax = data.groupby(group_col).ag_function[j][plot_col[i]].plot(label = labels[i], legend = leg);
				else:
					data.groupby(group_col).ag_function[j][plot_col[i]].plot(label = labels[i], legend = leg);
		# non-aggragation selection
		else:
			if i == len(num_plot_cols) - 1:
				ax = data.groupby(group_col)[plot_col[i]].plot(label = labels[i], legend = leg);
			else:
				data.groupby(group_col)[plot_col[i]].plot(label = labels[i], legend = leg);
	
	# set plot descriptions
	ax.set_title(title);
	ax.set_ylabel(y_lab);
	ax.set_xlabel(x_lab);