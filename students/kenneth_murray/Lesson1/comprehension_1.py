#!/usr/bin/env python

"""
Comprehension to lesson1 music assignment.
"""
#import collections
#create a named tuple list to iterate through

def tuple_from_csv(csv_in):
    '''creates a list of tuples from a CSV'''
    import csv
    from collections import namedtuple
    music_list = []
    with open (csv_in) as file_in:
        file_csv = csv.reader(file_in)
        Row = namedtuple('Row', next(file_csv))
        for csv_row in file_csv:
            row_tuple= Row(*csv_row)
            music_list.append(row_tuple)
    return music_list

def 

if __name__ == '__main__':

    my_music = tuple(tuple_from_csv('c:\\test\\featuresdf.csv'))
    print (my_music)


