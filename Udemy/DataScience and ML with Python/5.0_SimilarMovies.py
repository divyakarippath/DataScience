import pandas as pd

r_cols = ['user_id','movie_id','rating']
ratings = pd.read_csv("./Documents/Udemy_Datascience/DataScience/ml-100k/u.data",sep='\t',names=r_cols,usecols=range(3))
m_cols = ['movie_id','title']
movies = pd.read_csv("./Documents/Udemy_Datascience/DataScience/ml-100k/u.item",sep='|',names=m_cols,usecols=range(2))
ratings = pd.merge(movies,ratings)
print ratings.head()

movie_ratings = ratings.pivot_table(index = ['user_id'],columns = ['title'],values = 'rating')
print movie_ratings.head()

#Extract series of users who rated star wars
starWarsRatings = movie_ratings['Star Wars (1977)']
print starWarsRatings.head()

#Pairwise correlation
similarMovies = movie_ratings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
print df.head(10)
#sort
similarMovies.order(ascending = False)
