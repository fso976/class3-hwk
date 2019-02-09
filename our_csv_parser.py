#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')

        #declare a new list to contain the parsed content with appropriate datatypes (i.e. float and int)
        f_values = []

        f_values.extend([float(i) for i in values[0:3]])
        f_values.extend(int(i) for i in values[3])
        f_values.extend([float(i) for i in values[4:8]])
        f_values.extend(int(i) for i in values[8])
        f_values.extend([float(i) for i in values[9:14]])
        print(f_values)


    print('finished!')
