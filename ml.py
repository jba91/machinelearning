#!/usr/bin/python3.5

# Example of integer encoding string class values
from csv import reader

# load our csv file
def load_csv(fname):
    # create an empty list called ds
#    ds = list()
    ds = []
    with open(fname, 'r' ) as file:
        # create new file to hold just 3rd, 5th, and 8th fields
        count = 0
        csv_reader = reader(file)
        # for each row in the csv, append fields 3,5,8 to list ds
        # note that each value in the csv is type str
        for row in csv_reader:
            mystr = []
            if not row:		# skip empty rows, if there are any
                continue
            if count != 0:
                # create list containing Date/AreaID/CrimeCode
                #mystr = row[2] + ',' + row[4] + ',' + row[7]
                #mystr.append(row[2] + ',' + row[4] + ',' + row[7])
                mystr.append(row[2])
                mystr.append(row[4])
                mystr.append(row[7])
                print("mystr = ", mystr)
                ds.append(mystr)
                count = count + 1
            else:
                count = count + 1
    ### print(ds)
    return ds

# Load crime data into list "ds"
fname = 'crime.csv'
ds = load_csv(fname)
print( 'Loaded data file {0} with {1} rows and {2} columns ' .format(fname, len(ds), len(ds[0])))
print(ds)
