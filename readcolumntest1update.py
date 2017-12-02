import csv

input_file = csv.DictReader(open("crime.csv"))

total = 0 

print("The following content is from the column:'Time Occurred'")
for row in input_file:
    time = int(row["Time Occurred"])
    total = total  + time 
    print(time)
    print(" ")
    row_count = len(row)

print("The total is %d" % total)

print(row_count)
