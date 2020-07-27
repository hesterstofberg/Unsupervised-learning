import streamlit as st
import joblib
import os
import pandas as pd
from plotly.offline import iplot
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo

average_rating = 3.53

def introduction_to_the_eda():
    st.header("Introduction")
    st.write("""In this section, we explore the influence of a variety of factors on movie ratings. These factors include  \n \
    1. User behaviour,  \n2. Time (year and day of week),  \n3. Genres and subgenres,  \n4. The movie budget, and  \n5. The director of the movie.  \n \
    \nThe data used in this analysis is displayed in the tab titled 'Raw data' while the analysis of the five factors listed above are displayed in the tabs following.
    """)
    st.header("Summary of findings")
    st.subheader("""Noteworthy findings and trends discovered in the data include:  \n""")
    st.write("""1. Evidence of a bot with over 12000 revews submitted in one month in 2019, all with a score of 5.0.  \n  \
                2. Half scores (e.g 0.5, 3.5) appear to be less popular than whole number scores. The most common score is 4.0.  \n  \
                3. There is no visible difference in ratings submitted during the week in comparison to those submitted over the weekend.  \n  \
                4. Of all the years in which movies were released, movies released in 1995 have more reviews than any other year.   \n  \
                5. Users with the most ratings have average ratings below the dataset average.  \n  \
                6. By volume, the most popularly reviewed genre is drama and the most popular multi-genre are comedy dramas.  \n  \
                8. Very old movies (95 years+) have erratic rating trends over time due to the low volume of reviews.
                """)
def overview():
    st.header("Datasets used")
    st.subheader("A brief summary of the data received")
    st.write("""The focus of this EDA was on movie rating trends and the influences thereof. Ratings are on a score from 0.5 to  \
                5 and the frequency of each is visible below, showing users favour integer scores (even after half scores were released in 2003).""")
    overview_reviews_per_year = pd.read_pickle("pickled_dataframes/overview/overview_reviews_per_year.pkl")
    overview_ratings_distributions = pd.read_pickle("pickled_dataframes/overview/overview_ratings_distributions.pkl")
    # Plot data
    trace = go.Bar(x = data.index,
                   y = data['movieId'],
                   )

    # Create layout
    layout = dict(title = 'Distribution Of Ratings In Dataset'.format(ratings_df.shape[0]),
                  xaxis = dict(title = 'Rating Value'),
                  yaxis = dict(title = 'Number of Reviews'))

    # Create plot
    fig = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig)
    st.write("""This dataset contains reviews from 1995 to 2019 for movies released between 2019 and over 100 years ago. The number of reviews submiited from 1995 - 2019 is displayed below.""")

    # Create figure
    fig = px.line(x=overview_reviews_per_year.index, y=overview_reviews_per_year['movieId'])
    fig.update_layout(
        title = "Number of Reviews Per Year",
        xaxis_title="Year",
        yaxis_title="Number of Reviews",
    )
    st.plotly_chart(fig)

def ratings_over_time():
    st.write("""The average rating over the lifetime of every movie in the dataset is displayed below.""")
    year_on_year_changes = pd.read_pickle("pickled_dataframes/ratings_over_movie_lifetime/movies_with_more_than_20_years_of_reviews.pkl")
    plt_d = year_on_year_changes[year_on_year_changes.index <=20 ]
    fig = px.line(x=plt_d.index, y=plt_d['rating']['mean'])
    fig.update_layout(
        title = "Average Rating By Year From First Review For The First 20 Years",
        xaxis_title="Year Since Movie's First Review",
        yaxis_title="Average rating",
    )
    st.plotly_chart(fig)
    st.write("""In the figure above, it is clear that, on average, the average rating for movies does show a downward trend.  \
                From this pattern we can conclude that most older movies are less likely to be well-reviewed as more recent movies.""")

def user_behaviour():
    st.write("""Here we share insights related to user behaviour and its influence on the movie ratings. These insights result  \
    from examining the relationship between volume of reviews and average rating for each user, as well as how user reviews  \
    change over time as the user becomes more seasoned critics.  \n  \
    Below we can see the relationship between the total number of user reviews and the user's average rating:""")

    # Read in dataframe
    aggregated_df = pd.read_pickle("pickled_dataframes/user_trends/aggregated_df.pkl")

    # Plot dataframe
    fig = px.scatter(x = aggregated_df['rating']['count'], y = aggregated_df['rating']['mean'])

    # Add a title and labels to the axes
    fig.update_layout(
        title = "Average Rating By User's Total Rating Submissions",
        xaxis_title="Count of individual user submissions",
        yaxis_title="Average rating"
    )
    # Add a line for the average
    fig.add_trace(go.Scatter(x=[0,15000], y=[average_rating, average_rating], mode="lines", name="Dataset Average"))
    st.plotly_chart(fig)

    # Explain the next chart
    st.write("""To work around the outlier with almost thirteen thousand reviews, zoom in closer to the y-axis.  \n  \
    In the chart above, it is worth noting that users who have submitted many reviews have average ratings that fall below the average rating for the  \
    entire dataset, i.e. on average, more seasoned reviewers tend to give movies a score.  \n  \
    The chart below displays how the average rating for high-volume users (i.e users with more than 1000 reviews) changes over time as the user  \
    submits more reviews. This helps us to understand if they have always given movies a lower-than average score, or if this change happens as  \
    they become more seasoned reviewers.  \n  \
    The results of this investigation are displayed below: """)

    # Read in dataframe
    year_on_year_summary = pd.read_pickle("pickled_dataframes/user_trends/year_on_year_summary.pkl")
    
    # Create figure
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(go.Bar(x=year_on_year_summary.index, y=year_on_year_summary['rating']['count'], name="Number of reviews"),
        secondary_y=False,
    )
    fig.add_trace(go.Line(x=year_on_year_summary.index, y=year_on_year_summary['rating']['mean'], name = "Average rating by year"),
        secondary_y=True,
    )

    # Add a line for the average
    fig.add_trace(go.Scatter(x=[0,24], y=[average_rating, average_rating], mode="lines", name="Average rating (entire dataset)"), secondary_y=True)

    # Set y-axes titles
    fig.update_yaxes(title_text="Average Rating", secondary_y=True)
    fig.update_yaxes(title_text="Number of Reviews", secondary_y=False)

    # Add a title and an x-axis label
    fig.update_layout(
        title = "Average Rating By Year From First Review",
        xaxis_title="Year Since First Review",
    )
    st.plotly_chart(fig)
    st.write("""In the chart above it is clear that users who have reviewed over 1000 movies have always had an average rating below the dataset  \
            average, even in their first year of submitting reviews. It is possible that these users are just more likely to find fault with movies  \
            because they are more experienced critics.""")

def genre_analysis():
    genre_overview_or_granular = st.radio("Would you like to see the overview or a granular breakout by genre?", ("Overview", "Granular breakout"))
    if genre_overview_or_granular == "Overview":
        st.write("""The average rating for the top 10 genres (by volume) for the first 20 years after a movie's release is shown below:""")
        top_10_genres_df = pd.read_pickle("top_10_genres_df.pkl")
        st.write("""Movies in the 'Documentary', 'Drama', and 'Drama | Romance' genres have consistently high ratings over time while  \
                    movies in the 'Horror' genre have low and erratic ratings over time.""")
        # Plot data
        fig = px.line(x=top_10_genres_df.index.get_level_values(1), y=top_10_genres_df['rating'], color=top_10_genres_df.index.get_level_values(0))
        fig.update_layout(
            title = "Average Rating Over Movie Lifetime, Coloured By Genre",
            xaxis_title="Movie Age",
            yaxis_title="Average rating",
            legend_title="Genre"
            )
        st.plotly_chart(fig)
    elif genre_overview_or_granular == "Granular breakout":
        st.write("""Select a genre to examine using the options list on the left hand side.""")
        genres = ('Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                  'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western')
        genre = st.sidebar.radio(
                    "Select a genre",genres)
        aggregated_reviews_df = pd.read_pickle(
            'pickled_dataframes/genres/' + genre +'_genre.pkl')
        fig = px.line(
            y=aggregated_reviews_df['rating']['mean'],
            x=aggregated_reviews_df.index.get_level_values(1),
            color=aggregated_reviews_df.index.get_level_values(0))
        fig.update_layout(
            title="Average Rating Over Time For " + genre + " Movies",
            xaxis_title="Year Since Movie's Release",
            yaxis_title="Average rating",
            legend_title=genre + "/ Not " + genre)
        st.plotly_chart(fig)
    

def movie_budget():
    pass

def director_analysis():
    pass


