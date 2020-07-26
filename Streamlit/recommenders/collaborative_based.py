"""

    Collaborative-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `collab_model` !!

    You must however change its contents (i.e. add your own collaborative
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import pandas as pd
import streamlit as st
from utils.data_loader import load_movies, load_ratings, load_predictions, load_pickled_SVD

# Importing data
movies_df = load_movies()


def get_movie_id_from_title(title):
    return movies_df.loc[movies_df["title"] == title, "movieId"].iloc[0]


def get_movie_title_from_id(movie_id):
    return movies_df.loc[movies_df["movieId"] == movie_id, "title"].iloc[0]


def get_top_rated_users_for_movie(movie_id):
    """Map a given favourite movie to users within the
       MovieLens dataset with the same preference.

    Parameters
    ----------
    movie_id : int
        A MovieLens Movie ID.

    Returns
    -------
    list
        User IDs of users with similar high ratings for the given movie.

    """
    ratings_df = load_ratings()

    user_id_df = ratings_df.loc[ratings_df["movieId"] == movie_id].sort_values(
        "rating", axis=0, ascending=False)

    # Return the 5 users who rated this movie the highest
    return list(user_id_df['userId'])[:5]


def get_top_predictions_for_users(user_list):
    
    algo = load_pickled_SVD()
    list_movieId = list(movies_df.movieId.unique())
    
    predicted_ratings_list = []
    
    for userID in user_list:
        for movieID in list_movieId:
            prediction_value = algo.predict(userID, movieID)
            predicted_ratings_list.append({'userId':userID, 'movieId': movieID, 'predicted_rating': prediction_value.est})
            
    prediction_data = pd.DataFrame(predicted_ratings_list)
    prediction_data = prediction_data.sort_values('predicted_rating', ascending=False).groupby('movieId').first().reset_index()

    return prediction_data[["movieId", "predicted_rating"]].iloc[:50]


# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.
def collab_model(movie_list, top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    # Finding movie ID's for input
    movieId_1 = get_movie_id_from_title(movie_list[0])
    movieId_2 = get_movie_id_from_title(movie_list[1])
    movieId_3 = get_movie_id_from_title(movie_list[2])
    
    user_ids = []
    user_ids = user_ids + get_top_rated_users_for_movie(movieId_1)
    user_ids = user_ids + get_top_rated_users_for_movie(movieId_2)
    user_ids = user_ids + get_top_rated_users_for_movie(movieId_3)

    if len(user_ids) < 1:
        raise ValueError("Unable to find matching users")

    filtered_predictions = get_top_predictions_for_users(user_ids)
    filtered_predictions = filtered_predictions[
        ~filtered_predictions.movieId.isin([movieId_1, movieId_2, movieId_3])
    ]

    prediction_output = pd.merge(
        filtered_predictions, movies_df, on="movieId", how="left"
    )

    return list(prediction_output["title"].iloc[:top_n])
