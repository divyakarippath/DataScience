# Predict the rating of a movie by looking at 10 movies closer to it in terms of genre and popularity

import pandas as pd
import numpy as np
from scipy import spatial
import operator
#calculate distance between 2 movies based on genre and popularity
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance
    


# Calculate neighbours
def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors
#load the dataset to pandas dataframe
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./Documents/udemy_datascience/datascience/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))
print ratings.head()

#group by movie id to find total numbe of ratings of movie id and average rating

movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print movieProperties.head()

#Normalize the number of ratings (popularity) 0 - no rating , 1-most popular
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print movieNormalizedNumRatings.head()

#Genre info , 19 fields each corresponding a particular genre.Value 0 means not in that genre , 1 means in that genre.A movie can be associated to more than one genre
# build a dictionary with movie id as key and movie name,list of genre values, normalized popularity, avg rating
movieDict = {}
with open(r'./Documents/udemy_datascience/datascience/ml-100k/u.item') as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, genres, movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))
print movieDict[1]

#compute distance between movies with ids 2 and 4 , exmple , Higher the distance more different the movies are
print ComputeDistance(movieDict[2], movieDict[4])

#Compute distance between given test movie and all other movies in data set
K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print movieDict[neighbor][0] + " " + str(movieDict[neighbor][3])
    
avgRating /= float(K)

#compare with actual avg rating
print avgRating
print movieDict[1]
