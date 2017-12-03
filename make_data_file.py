#!/usr/bin/python3.5

### creating input file based on the crime.csv

import datetime
from csv import reader
import csv

# function to load csv file and create list
def load_csv(fname):
    # create an empty list called ds
    ds = list()
    ds.append(['AreaID', 'CrimeID', 'Age', 'Gender', 'Race'])
    with open(fname, 'r' ) as file:
        # create new file to hold just fields we care about
        count = 0
        csv_reader = reader(file)
        # process each row in the csv that has an Age value (a victim, ignore stolen cars etc)
        # note that each value read from the csv is type str
        for row in csv_reader:
            mystr = list()
            if not row:		# skip empty rows, if there are any
                continue
            if count != 0:
                # create list if there is a victim (field #11 (Age) is not blank)
                # list will contain AreaID/CrimeCode/Age/Gener/Race
                # if any of Age/Gender/Race are blank, skip
                if row[10] and row[11] and row[12]:
                    # Gender Code: M=0, F=1
                    # Race Code:
                    #   A - Other Asian                    ->  1.0
                    #   B - Black                          ->  2.0
                    #   C - Chinese                        ->  3.0
                    #   D - Cambodian                      ->  4.0
                    #   F - Filipino                       ->  5.0
                    #   G - Guamanian                      ->  6.0
                    #   H - Hispanic/Latin/Mexican         ->  7.0
                    #   I - American Indian/Alaskan Native ->  8.0
                    #   J - Japanese                       ->  9.0
                    #   K - Korean                         -> 10.0
                    #   L - Laotian                        -> 11.0
                    #   O - Other                          -> 12.0
                    #   P - Pacific Islander               -> 13.0
                    #   S - Samoan                         -> 14.0
                    #   U - Hawaiian                       -> 15.0
                    #   V - Vietnamese                     -> 16.0
                    #   W - White                          -> 17.0
                    #   X - Unknown                        -> 18.0
                    #   Z - Asian Indian                   -> 19.0
 
                    # AreaID / CrimeID / Age
                    mystr.append(float(row[4]))
                    mystr.append(float(row[7]))
                    mystr.append(float(row[10]))

                    # gender
                    if row[11] == 'M':
                        mystr.append(0.0)
                    else:
                        mystr.append(1.0)

                    # Race
                    if row[12] == 'A':
                        mystr.append(1.0)
                    elif row[12] == 'B':
                        mystr.append(2.0)
                    elif row[12] == 'C':
                        mystr.append(3.0)
                    elif row[12] == 'D':
                        mystr.append(4.0)
                    elif row[12] == 'F':
                        mystr.append(4.0)
                    elif row[12] == 'F':
                        mystr.append(5.0)
                    elif row[12] == 'G':
                        mystr.append(6.0)
                    elif row[12] == 'H':
                        mystr.append(7.0)
                    elif row[12] == 'I':
                        mystr.append(8.0)
                    elif row[12] == 'J':
                        mystr.append(9.0)
                    elif row[12] == 'K':
                        mystr.append(10.0)
                    elif row[12] == 'L':
                        mystr.append(11.0)
                    elif row[12] == 'O':
                        mystr.append(12.0)
                    elif row[12] == 'P':
                        mystr.append(13.0)
                    elif row[12] == 'S':
                        mystr.append(14.0)
                    elif row[12] == 'U':
                        mystr.append(15.0)
                    elif row[12] == 'V':
                        mystr.append(16.0)
                    elif row[12] == 'W':
                        mystr.append(17.0)
                    elif row[12] == 'X':
                        mystr.append(18.0)
                    elif row[12] == 'Z':
                        mystr.append(19.0)
                    ds.append(mystr)
                count = count + 1
            else:
                count = count + 1
        ###print(ds)

        with open('crime.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(ds)

#        for line in ds:
#            f.write(str(line))
#        f.close()
 
        return ds

# function to convert string column to float
def str_column_to_float(ds, column):
    for row in ds:
        row[column] = float(row[column].strip())
    
# function to normalize the data - make AreaID a number between 0 and 1
# Find the min and max values for each column
#def dataset_minmax(dataset):
#    minmax = list()
#    for i in range(len(dataset[0])):
#        col_values = [row[i] for row in dataset]
#        value_min = min(col_values)
#        value_max = max(col_values)
#        minmax.append([value_min, value_max])
#    return minmax

### Main ###

# Load crime data into list "ds"
###fname = 'Crime_Data_from_2010_to_Present_SUBSET.csv'
fname = 'Crime_Data_from_2010_to_Present.csv'
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

