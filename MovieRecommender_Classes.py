# This program establishes the class movie recommender with functions to sort movies. CSV file includes relevant information regarding movies.

# Imports
import pandas as pd

class MovieRecommender:
    def __init__(self, filename): # Constructor of class defining instance variables
        self.__allMovies = pd.read_csv(filename).sort_values('Title').reset_index(drop = True)
        self.__myFavorites = set()
    def movieAsString(self, idx):
        movie = self.__allMovies.loc[idx]
        return f"{idx}: [{movie['IMDB ID']}] ({movie['Rating']}/10) {movie['Year']} - {movie['Title']}" # String representation format
    def addToFavorites(self, idx):
        self.__myFavorites.add(idx) # Adds movie's idx to favorite
    def favorites(self):
        favoriteMovies = ' '
        for idx in self.__myFavorites:
            favoriteMovies += self.movieAsString(idx) + '\n' 
        return favoriteMovies
    def recommendations(self, keyword, column):
        recommendationList = ' '
        reccomendedMovies = self.__allMovies[self.__allMovies[column.title()].str.contains(keyword.title())] # Makes case insensitive
        reccomendedMovies = reccomendedMovies.sort_values(by = 'Rating', ascending = False) # Sorts based on rating
        reccomendedMovies = reccomendedMovies.head(5) # Displays top 5
        for idx in reccomendedMovies.index:
            recommendationList += self.movieAsString(idx) + '\n'
        return recommendationList
    def __len__(self):
        return len(self.__allMovies) # Returns number of movies in entire data set