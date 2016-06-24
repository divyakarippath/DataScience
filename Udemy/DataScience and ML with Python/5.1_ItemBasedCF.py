import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./Documents/Udemy_Datascience/DataScience/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./Documents/Udemy_Datascience/DataScience/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2))
ratings = pd.merge(movies, ratings)
print ratings.head()

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print userRatings.head()

#calculate correlation score for every column pair , NaN if no users rated both the movies
corrMatrix = userRatings.corr()
print corrMatrix.head()

#Avoid correlation of movies which are rated by less than 100 users
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
print corrMatrix.head()

#Movie recommendation for userId 0, extract this user's rating from userRatings data frame
myRatings = userRatings.loc[0].dropna()
print myRatings

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print "Adding sims for " + myRatings.index[i] + "..."
    # Retrieve similar movies to this one that user rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well user rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    

print "sorting..."
simCandidates.sort_values(inplace = True, ascending = False)
print simCandidates.head(10)

#To combine movies similar to more than one movies using groupby

simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)
print simCandidates.head(10)

#Filter out movies which are already rated by the user
filteredSims = simCandidates.drop(myRatings.index)
print filteredSims.head(10)