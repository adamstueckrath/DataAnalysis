
# coding: utf-8

# In[4]:

## Read in the data .csv 
## and store the results in variables
import unicodecsv

def parse_csv(file_name):
    with open(file_name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    

## Takes a date as a string, and returns a Python datetime object.
## If there is no date given, returns None.
from datetime import datetime as dt

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    

## Takes a string which is either an empty string or represents an integer,
## and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

    
## Takes a file and returns the length.   
def total_rows(file_name):
    return len(file_name)
        
    
## Loops through a file and appends each row's unique account/primary key to a set.
## Returns the set of unique keys.
def unique_count(data_file,key_name):
    unique_data = set()
    for data in data_file:
        unique.add(data[key_name])
    return unique_data


## Change the name of a key in a dictionary. The function adds a new key equaled
## to the old key and deletes the old key.
def change_dict_key_name(my_dict, new_key, old_key):
    for x in my_dict:
        x[new_key] = x[old_key]
        del[x[old_key]]
    return my_dict


## Find  unique account/primary keys missing from data_2
## Return a list of missing records from data_2
def find_missing_data(key,data_1,data_2):
    missing_data = []
    for data in data_1:
        compare_data = data[key]
        if compare_data not in data_2:
            missing_data.append(data)
    return missing_data

