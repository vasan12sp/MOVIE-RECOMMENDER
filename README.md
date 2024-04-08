# MOVIE-RECOMMENDER
Movie Recommender System based on combining cosine similarity and sentiment analysis

DATASET: https://www.kaggle.com/datasets/rajugc/imdb-movies-dataset-based-on-genre

Inside the "DataPreProcessing" folder, all the csv files are available

Steps:
 1. Run 'filter_dataset.py' inside the DataPreProcessing folder (genre wise datasets are merged into one and filtered based on some criteria to reduce the size of the data)
 2. Run 'final_data_processing.py' inside the DataPreProcessing folder (new column called 'tags' formed and other unwanted columns are removed and duplicates are removed)
 3. Run 'user_interface.py' with streamlit
