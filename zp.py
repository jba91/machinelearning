#!/usr/bin/python3.5

import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

### test to make sure matplotlib works
print("\n---verify that matplotlib works---")
plt.plot([1,2,3,4])
plt.plot([2,4,7,14])
plt.ylabel('Just a TEST')
plt.show()
print(); input("Press Enter to continue...")

### read in our crime data
### data is from https://catalog.data.gov/dataset/crime-data-from-2010-to-present
z = pandas.read_csv("crime.csv")
print("\n---show the head (first few columns of data)---")
print(z.head())
print(); input("Press Enter to continue...")

# prints all columns
print("\n---show the columns in crime.csv---")
print(z.columns)
print(); input("Press Enter to continue...")

# show just the Age
print("\n---show the columns in crime.csv---")
print(z.Age)
print(); input("Press Enter to continue...")

# histogram of all Age
print("\n---show a historgram of all the Ages in the data---")
plt.hist(z["Age"])
plt.show()
print(); input("Press Enter to continue...")

### print crimes with Victims older than 90
print("\n---show all the crimes with victims older than 90 yrs old---")
# print first row that has an Age > 90
#print(z[z["Age"] > 11].iloc[0])
#print(z[z["Age"] == 90].iloc[0])
#print(z[z["Age"] > 90.0].iloc[3])
#print(z.iloc[29]

#print(z[z["Age"] == 90].iloc[0])
#print(z[z["average_rating"] == 0].iloc[0])

print(); input("Press Enter to continue...")
exit(0)

# k-means clustering
# create model with 2 params - num of clusters and random stat.
#kmeans_model = KMeans(n_clusters=5, random_state=1)

# get numeric columns from z
#good_cols = z._get_numeric_data()

# fit the model using the good columns
#kmeans_model.fit(good_cols)

# get cluster assignments
#labels = kmeans_model.labels_

### clusters : create PCA model
#pca_2 = PCA(2)

# fit the PCA model using the columns defined earlier
#plot_cols = pca_2.fit_transform(good_cols)

# create the scatter plot
#plt.scatter(x=plot_cols[:,0], y=plot_cols[:,1], c=labels)

# display the plot
#plt.show()


