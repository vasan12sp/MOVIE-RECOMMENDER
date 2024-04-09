# MOVIE-RECOMMENDER
Movie Recommender System based on combining cosine similarity and sentiment analysis

DATASET: https://www.kaggle.com/datasets/rajugc/imdb-movies-dataset-based-on-genre

Inside the "DataPreProcessing" folder, all the csv files are available

About:
The project is a unique movie recommender system that employs both cosine similarity and sentiment analysis to deliver personalized recommendations. Unlike traditional systems, which rely solely on collaborative filtering or cosine similarity, this system combines these methods for enhanced accuracy. Initially, it calculates cosine similarity to identify the top 10 similar movies to the user's input. Then, it dynamically scrapes the top 5 most liked reviews from IMDb for each of these movies. After cleaning and analyzing the sentiment of these reviews, a combined score is computed. Finally, the system presents the top 10 recommended movies, sorted by this score, along with IMDb links for further exploration.

Steps:
 1. Run 'filter_dataset.py' inside the DataPreProcessing folder (genre wise datasets are merged into one and filtered based on some criteria to reduce the size of the data)
 2. Run 'final_data_processing.py' inside the DataPreProcessing folder (new column called 'tags' formed and other unwanted columns are removed and duplicates are removed)
 3. Run 'user_interface.py' with streamlit
