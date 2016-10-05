
# coding: utf-8

# In[1]:

## Takes data as an argument and key to group by.
## Returns a dictionary mapping account keys to list of records.
from collections import defaultdict

def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data


## Take grouped data as input and the field name to sum up.
## Returns the sum data.
def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data


## Returns summary statistics about the data 
## Use matplotlib and numpy
get_ipython().magic(u'pylab inline')

import matplotlib.pyplot as plt
import numpy as np

def describe_data(data):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)
    plt.hist(data)
    
## Import the seaborn library to make the visualization
## look better, adding axis labels and a title, and changing one or more
## arguments to the hist() function.
## Add axis labels using: plt.xlabel("Label for x axis") and plt.ylabel("Label for y axis")
## Add a title using: plt.title("Title of plot")


# In[ ]:



