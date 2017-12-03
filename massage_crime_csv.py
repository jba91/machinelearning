#!/usr/bin/python3.5

### creating input file based on the crime.csv

import datetime
from csv import reader

# function to load csv file and create list
def load_csv(fname):
    # create an empty list called ds
    ds = list()
    with open(fname, 'r' ) as file:
        # create new file to hold just 3rd, 5th, and 8th fields
        count = 0
        csv_reader = reader(file)
        # for each row in the csv, append fields 3,5,8 to list ds
        # note that each value in the csv is type str
        for row in csv_reader:
            today = datetime.date.today()
            mystr = list()
            if not row:		# skip empty rows, if there are any
                continue
            if count != 0:
                # create list containing Victims (Field #11 not blank)
                if row[10]:
                    # create list containing Date/AreaID/CrimeCode

                    t = row[2].split("/")   # split string at "/"
                    month = int(t[0])
                    day = int(t[1])
                    year = int(t[2])
                    crimedate = datetime.date(year,month,day)
                    dt = (today-crimedate).days		# see date.py for details on this

                    mystr.append(dt)
                    mystr.append(row[4])
                    mystr.append(row[7])
                    mystr.append(row[10])
                    mystr.append(row[11])
                    mystr.append(row[12])
                    #print("mystr = ", mystr)
                    ds.append(mystr)
                count = count + 1
                print(ds)
            else:
                count = count + 1
#        print(ds)
        return ds

# function to convert string column to float
def str_column_to_float(ds, column):
    for row in ds:
        row[column] = float(row[column].strip())
    
# function to normalize the data - make AreaID a number between 0 and 1
# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

# Load crime data into list "ds"
fname = 'Crime_Data_from_2010_to_Present_SUBSET.csv'
ds = load_csv(fname)
#print("Loaded data file {0} with {1} rows and {2} columns " .format(fname, len(ds), len(ds[0])))
#print("--------------\n\n")

# convert strings in 2nd and 3rd columns to float
#for i in range(1,3):
#    #print("i =",i)
#    str_column_to_float(ds, i)
#print(ds)

#minmax = dataset_minmax(ds)
#print("minmax =", minmax)

