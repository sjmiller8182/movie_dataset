import numpy as np

def get_means(df, group_by, feature):
    ''' Returns the unique elements of 'group_by' in df and the means of each 
    unique element in df. Assumes df is of type pd.DataFrame. 
    '''
    # groupby sorts values ascending by 'groupby'
    df_g = df.copy()
    means = df_g.groupby(group_by).mean()[feature].tolist()
    groups = list(df[group_by].values.unique())
    # sort ascending to match means
    groups.sort()
    return groups, means
    
def get_counts(df, group_by, feature):
    ''' Returns the unique elements of 'group_by' in df and the counts of each
    unique element in df. Assumes df is of type pd.DataFrame. 
    '''
    # groupby sorts values ascending by 'groupby'
    df_g = df.copy()
    counts = df_g.groupby(group_by).count()[feature].tolist()
    groups = list(df[group_by].values.unique())
    # sort ascending to match counts
    groups.sort()
    return groups, counts
def get_medians(df, group_by, feature):
    ''' Returns the unique elements of 'group_by' in df and the medians of each
    unique element in df. Assumes df is of type pd.DataFrame. 
    '''
    # groupby sorts values ascending by 'groupby'
    df_g = df.copy()
    medians = df_g.groupby(group_by).median()[feature].tolist()
    groups = list(df[group_by].values.unique())
    # sort ascending to match medians
    groups.sort()
    return groups, medians