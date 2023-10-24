# This program intends to create a directory to allow users to construct their movie recommender.

# Imports classes
from MovieRecommender_Classes import *

MR = MovieRecommender('Hydra-Movie-Scrape.csv') # MR is an abbreviation for MovieRecommender

numMovies = len(MR)
idxRange = 10
currentIDX = 0

print('Current Page of Movies in alphabetical order:') # First page of 10 movies
for i in range(currentIDX, currentIDX + idxRange):
    if i < numMovies:
        print(MR.movieAsString(i))

while True:
    print("A - add movie above to favorites") # Menu of options
    print("R - get recommendations")
    print("N - show next page of movies")
    print("P - show previous page of movies")
    print("J - jump to movie with index")
    print("F - print my favorites")
    print("X - exit program")
    userInput = input("Enter Command (A/R/N/P/J/F/X): ").strip().lower()
    if userInput == "a": # Adds movie above to favorites
        movie_idx = int(input("Enter index of movie to add: ")) 
        MR.addToFavorites(movie_idx)
        print("Movie added to favorites.") 
    elif userInput == "r": # Get recommendations
        keyword = input("Enter a name or search term: ") 
        category = input("Search Title, Summary, or Cast (S/T/C): ").strip().lower()
        if category == 's':
            colulmn = 'Summary' 
        if category == "t":
            column = "Title" 
        elif category == "c":
            column = "Cast" 
        else:
            print("Invalid category.")
            continue
        recommendations = MR.recommendations(keyword, column) 
        print('The top rated movies with', keyword, 'in column', column, 'are:')
        print(recommendations)
    elif userInput == "n": # Show next page of movies
        if currentIDX + idxRange < numMovies:
            currentIDX += idxRange
            print('Current Page of Movies in alphabetical order:')
            for i in range(currentIDX, currentIDX + idxRange):
                if i < numMovies:
                    print(MR.movieAsString(i))
        else:
            print("End of movies reached.")
    elif userInput == "p": # Show previous page of movies
        if currentIDX > 0:
            currentIDX -= idxRange
            for i in range(currentIDX, currentIDX + idxRange):
                if i < numMovies:
                    print(MR.movieAsString(i))
        else:
            print("Beginning of movies reached.")
    elif userInput == "j": # Jump to movie with index
        movie_idx = int(input("Enter index: "))
        currentIDX = (movie_idx) 
        for i in range(currentIDX, currentIDX + idxRange):
            if i < numMovies:
                print(MR.movieAsString(i))
    elif userInput == "f": # Print My Favorites
        favorites = MR.favorites()
        print("My Current Favorite Movies:")
        print(favorites)
    elif userInput == "x": # Exit program
        print("Program has been exited.")
        break
    else:
        print("Invalid choice.")