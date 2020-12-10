import pandas as pd 
import matplotlib.pyplot as plt

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

def load():
    # Evaluating the three first records of each dataframe
    print("Top three records of movies df: \n", movies.head(3))
    print("Top three records of ratings df: \n",ratings.head(3))
    print("---------\n")

    # Evaluating the lenght of the datasets
    print("Count of movies: ", len(movies))
    print("Count of ratings: ", len(ratings))
    print("---------\n")

    # Creating a subset based on movieId
    ratings_matrix = ratings.query("movieId==2571")
    print(ratings_matrix)
    print("---------\n")

    # Lowest, Highest, mean, and description of ratings for Matrix
    print("Lowest rating for Matrix: ", ratings_matrix['rating'].min())
    print("Highest rating for Matrix: ", ratings_matrix['rating'].max())
    print("Mean of ratings for Matrix: ", ratings_matrix['rating'].mean())
    print("Description of ratings for Matrix: \n", ratings_matrix['rating'].describe())
    print("---------\n")

    # Mean rating grouped by movie
    mean_rating_movies= ratings.groupby("movieId")["rating"].mean()  
    print(mean_rating_movies.head())
    print("---------\n")

    # Relating movies and ratings
    movies_and_ratings = movies.join(mean_rating_movies, on="movieId")
    print(movies_and_ratings.head(3))
    print("---------\n")

    # Movies sorted by mean ratings
    movies_and_ratings_sorted = movies_and_ratings.sort_values("rating", ascending=False)
    print(movies_and_ratings_sorted.head(3))
    print("---------\n")

    # Basic plot from selected information
    plt.plot(ratings_matrix["rating"])
    plt.show()

    # Plot a histogram from selected information
    plt.hist(ratings_matrix["rating"])
    plt.title('Histrogram of Matrix Ratings')
    plt.ylabel('Ratings')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    load()