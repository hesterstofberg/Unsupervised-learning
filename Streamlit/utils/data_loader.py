"""

    Helper functions for data loading and manipulation.

    Author: Explore Data Science Academy.

"""
# Data handling dependencies
import pickle
import pandas as pd
from surprise import SVD
import streamlit as st


@st.cache
def load_movie_titles(path_to_movies):
    """Load movie titles from database records.

    Parameters
    ----------
    path_to_movies : str
        Relative or absolute path to movie database stored
        in .csv format.

    Returns
    -------
    list[str]
        Movie titles.

    """
    df = pd.read_csv(path_to_movies)
    df = df.dropna()
    movie_list = df['title'].to_list()
    return movie_list


# @st.cache
def load_movies():
    return pd.read_csv("resources/data/movies.csv", sep=",", delimiter=",")


# @st.cache
def load_ratings():
    ratings_df = pd.read_csv("resources/data/ratings.csv")
    ratings_df.drop(["timestamp"], axis=1, inplace=True)
    return ratings_df


# @st.cache
def load_predictions():
    return pickle.load(open("resources/data/predicted_rating_df.pkl", "rb"))


# @st.cache
def load_model():
    # We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
    return pickle.load(open("resources/models/SVD.pkl", "rb"))

# @st.cache
def load_pickled_SVD():
    # We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
    return pickle.load(open("resources/data/SVD_model.pkl", "rb"))