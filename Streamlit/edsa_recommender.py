"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Resources function
import eda_page
import plotly.express as px
from utils.genre_flipcard_HTMLCopy1 import *
from utils.helper_functions import *
from utils.person_flipcard_HTML import *
from utils.xolisa_flipcard import *
from recommenders.content_based import content_model
from recommenders.collaborative_based import collab_model
from utils.data_loader import load_movie_titles
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import streamlit as st
import logging

logger = logging.getLogger()


def resources():
    st.markdown("##### Resources:")
    st.markdown(
        "##### 1. _Data Science and Recommender Systems_  by John Paul Mueller & Luca Massaron [link here](https://www.dummies.com/programming/big-data/data-science/data-science-and-recommender-systems/)")
    st.markdown(
        "##### 2. _How recommender systems make their suggestions_ by Bibblio [link here](https://medium.com/the-graph/how-recommender-systems-make-their-suggestions-da6658029b76)")
    st.markdown(
        "##### 3. _Towards a Perspective of Hybrid Approaches and Methodologies in Recommender Systems_ by Nana Yaw Asabere [PDF here](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.685.9037&rep=rep1&type=pdf)")
    return


# Streamlit dependencies

# Data handling dependencies

# Custom Libraries


# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration


def main():
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

    pages = [
        'Enter the realm',
        'Recommender System',
        'Playground',
        'Look into the crystal ball',
        'How the magic works',
        'Meet the Realm Keepers']

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose a Page", pages)
    if page_selection == "Recommender System":

        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png', use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option', title_list[14930:15200])
        movie_2 = st.selectbox('Second Option', title_list[25055:25255])
        movie_3 = st.selectbox('Third Option', title_list[21100:21200])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(
                            movie_list=fav_movies, top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i + 1) + '. ' + j)
                except BaseException:
                    st.error("Oops! Looks like this algorithm doesn't work.\
                          We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(
                            movie_list=fav_movies, top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i + 1) + '. ' + j)
                except BaseException as e:
                    logger.exception(e)
                    st.error("Oops! Looks like this algorithm doesn't work.\
                          We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    if page_selection == 'Enter the realm':
        st.write(
            "<style type='text/css'>body {background-color:#1793b8}</style>",
            unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align: center; color: purple; font-size: 3.0rem; '><i>Cinematic Psychic</i> </h1>",
            unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align: left; color: purple; font-size: 2.5rem; '><i>Welcome</i> </h1>",
            unsafe_allow_html=True)
        st.image('resources/imgs/Face.jpg', use_column_width=True)
        st.markdown(
            "<h1 style='text-align: left; color: purple; font-size: 2.1rem; '><i>Let your future movie choices be revealed...</i> </h1>",
            unsafe_allow_html=True)

    if page_selection == 'Look into the crystal ball':
        st.write('# Exploratory Data Analysis :crystal_ball:')
        switcher = {'Overview': eda_page.introduction_to_the_eda, 'Analysis of Ratings Over Time': eda_page.ratings_over_time, 'Analysis of User Behaviour': eda_page.user_behaviour, 'Analysis of Performance by Genre': eda_page.genre_analysis} #, 'Influence of Directors on Ratings': eda_page.director_analysis}
                    #'Influence of Movie Budget on Ratings': eda_page.movie_budget, }
        eda_categories = list(switcher.keys())
        eda_selection = st.selectbox('Select a category of analysis to learn more about',eda_categories)
        eda_function = switcher.get(eda_selection)
        eda_function()

    if page_selection == "Playground":
        st.markdown("# For when you have a genre in mind...")
        st.write(genre_flipcard(), unsafe_allow_html=True)

    if page_selection == "How the magic works":

        option = st.sidebar.radio(
            "What would you like to know?",
            ("What is a recommender system?",
             "Why is it useful?",
             "How does it work?",
             "Real life examples"))

        if option == "What is a recommender system?":
            st.markdown("# What is a recommender system?")
            st.write("A recommender system can suggest items or actions of interest to a user, after having learned the user’s preferences over time. The technology, which is based on data and machine learning techniques (both supervised and unsupervised), has appeared on the Internet for about two decades.")
            st.write("In a way, recommenders try to narrow down choices for people by presenting them with suggestions that they are most likely to buy or use.")
            st.image(
                "resources/imgs/recommend.jpeg",
                caption='Source: https://towardsdatascience.com',
                use_column_width=True)

        if option == "Why is it useful?":
            st.markdown("# Why is it useful?")
            st.write("Today you can find recommender systems almost everywhere, and they’re likely to play an even larger role in the future under the likeness of personal assistants, such as Siri (developed by Apple), Amazon Alexa, Google Home, or some other artificial-intelligence–based digital assistant. The drivers for users and companies to adopt recommender systems are different but complementary:")
            st.write("*** Users:** users have a strong motivation to reduce the complexity of the modern world (regardless of whether the issue is finding the right product or a place to eat) and avoid information overload.")
            st.write("*** Companies:** companies need recommender to systems provide a practical way to communicate in a personalized way with their customers and successfully push sales.")
            st.image("resources/imgs/recommendation.jpg", caption='Recommendation systems can assist users in making decisions and increase revenue for companies.', use_column_width=True)
        

        if option == "How does it work?":

            st.markdown("# How does it work?")
            st.write("Recommender systems apply machine learning and data mining techniques to filter undetected information and can predict whether a user of a system would like a given resource based on his/her interests and preferences.")
            st.write("To date, a  number of recommendation algorithms have been proposed, where Collaborative Filtering (CF) and Content-Based Filtering (CBF) are the two most famous and adopted recommendation techniques.")

            based = st.radio(
                "Show more information on",
                ("Collaborative based filtering",
                 "Content based filtering",
                 "Hybrid recommender system"))

            if based == "Collaborative based filtering":
                st.markdown("## Collaborative based filtering")
                st.write("Collaborative filtering is based on the idea that people who agree in their evaluation of certain items in the past are likely to agree again in the future.")
                st.write("Presently, most collaborative filtering algorithms draw upon a neighborhood approach. In this technique, a number of peers are selected based on their similarity to you. The recommendation is then made by calculating a weighted average of the ratings of these ‘nearest neighbors’.")
                st.write("One of the challenges underlining this, is the new item problem. Collaborative filters recommend based on past annotations, so they cannot come up with a sensible prediction for items with limited historical data. This can create a rich-get-richer effect for those popular items. This bias can prevent matches between you and an item of great value and interest.")
                st.image(
                    "resources/imgs/collab_based.png",
                    caption='Collaborative based filtering. Source: https://www.kdnuggets.com',
                    width=300)

                resources()

            if based == "Content based filtering":
                st.markdown("## Content based filtering")
                st.write("Content-based filtering recommends based on a comparison between the items’ set of terms and your user profile. Your profile is represented with the same terms and built up by analyzing the content of items which have been seen by you.")
                st.write("The new item problem does not limit content-based filtering, which is the other major approach to recommendations. This is because content-based filtering is based on the items’ set of descriptors or terms rather than its annotations.")
                st.write("This method can also capture the specific interests of a user, and can recommend niche items that very few other users are interested in. An underlying challenge is that the model can only make recommendations based on existing interests of the user. In other words, the model has limited ability to expand on the users' existing interests.")
                st.image(
                    "resources/imgs/content_based.png",
                    caption='Content based filtering. Source: https://www.kdnuggets.com',
                    width=300)
                resources()

            if based == "Hybrid recommender system":
                st.markdown("## Hybrid recommender system")
                st.write("Hybrid systems put together two or more other strategies with the goal of reinforcing their advantages and reducing their disadvantages or limitations.")
                st.write("A weighted hybrid recommender system is one in which the score of a recommended item is computed from the results of all of the available recommendation techniques present in the system. In other words, the scores of several recommendation techniques are combined together to produce a single recommendation.")
                st.write("The benefit of a weighted hybrid is that all of the system’s capabilities are brought to bear on the recommendation process in a straightforward way and it is easy to perform post-hoc evaluation and adjust the hybrid accordingly.")
                st.image(
                    "resources/imgs/hybrid_based.png",
                    caption='Hybrid filtering. Source: https://towardsdatascience.com',
                    width=550)
                resources()

        if option == "Real life examples":
            st.markdown("# Examples of recommendations in our everyday lives")
            st.write("Recommendation systems are almost everywhere from Takealot to Netflix; from Facebook to Linkedin. Companies like Youtube and Netflix depend on their recommendation engines to help users discover new content.")

            example = st.radio(
                "Select an example",
                ("Takealot",
                 "Linkedin",
                 "Netflix",
                 "Facebook"))

            if example == "Takealot":
                st.markdown("### Takealot")
                st.write("Takealot uses data from its approximately 1.9 million users to identify which items are usually bought together and makes recommendations based on that. The recommendations in takealot.com are provided on the basis of explicitly provided ratings, buying behaviour, and browsing history.")
                st.image(
                    "resources/imgs/takealot.png",
                    caption='Takealot will suggest other items based on the item you are interested in.',
                    use_column_width=True)

            if example == "Linkedin":
                st.markdown("### Linkedin")
                st.write(
                    "Linkedin utilises data from your past experience, current job titles and endorsements to suggest probable jobs to you.")
                st.image(
                    "resources/imgs/linkedin.png",
                    caption='Linkedin uses multiple variables to suggest relevant jobs to their users.',
                    use_column_width=True)

            if example == "Netflix":
                st.markdown("### Netflix")
                st.write("A great example of using a Hybrid approach is that of Netflix. At Netflix, recommendations are not only based on what people’s watching and searching habits (collaborative based) but also movies sharing similar characteristics (content-based) are also recommended.")
                st.image(
                    "resources/imgs/netflix.png",
                    caption='Netflix aims to help users discover new content.',
                    use_column_width=True)

            if example == "Facebook":
                st.markdown("### Facebook")
                st.write(
                    "Recommender systems, such as Facebook, do not directly recommend products but they recommend connections.")
                st.image(
                    "resources/imgs/facebook.png",
                    caption='Facebook says its suggestions are based on "mutual friends, work and education information, networks you`re part of, contacts you`ve imported and many other factors."',
                    width=350)

            st.markdown("##### Resources:")
            st.markdown(
                "##### 1. _The Remarkable world of Recommender Systems_ by Parul Pandey [link here](https://towardsdatascience.com/the-remarkable-world-of-recommender-systems-bff4b9cbe6a7)")

    if page_selection == 'Meet the Realm Keepers':
        
        member = st.sidebar.radio("Who would you like to meet?", ("Meet the Psychics", "Meet the Overlord"))
        
        if member == 'Meet the Psychics':
            st.write(person_flipcard(), unsafe_allow_html=True)
            
        if member == 'Meet the Overlord':
            st.write(xolisa(), unsafe_allow_html=True)


if __name__ == '__main__':
    local_css('styles.css')
    main()
