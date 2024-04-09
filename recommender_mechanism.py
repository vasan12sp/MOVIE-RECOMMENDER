import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import requests
import re
import time
from textblob import TextBlob
import streamlit as st
import concurrent.futures

# Function to load and preprocess data
@st.cache_data
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to vectorize tags
@st.cache_data
def vectorize_tags(df, max_features=10204):
    cv = CountVectorizer(max_features=max_features, stop_words='english')
    vector = cv.fit_transform(df['tags'].astype(str)).toarray()
    return vector, cv

# Function to calculate cosine similarity
@st.cache_data
def calculate_cosine_similarity(vector):
    similarity = cosine_similarity(vector)
    return similarity

# Function to scrape top reviews from IMDb
@st.cache_data
def scrape_top_reviews(movie_code):
    # Simulating loading animation
    with st.spinner("Fetching reviews..."):
        time.sleep(1)  # Reduced sleep time
    
    url = f"https://m.imdb.com/title/{movie_code}/reviews?sort=totalVotes&dir=desc"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        review_elements = soup.find_all('div', attrs={'class':'text'})
        reviews = [review.get_text(strip=True) for review in review_elements][:5]
        return reviews
    else:
        return []

# Function to clean reviews and analyze sentiment
@st.cache_data
def clean_and_analyze_sentiment(reviews):
    cleaned_reviews = []
    for review in reviews:
        cleaned_review = re.sub(r'<.*?>', '', review)
        unwanted_words = ['the', 'and', 'is', 'in', 'of']
        cleaned_review = ' '.join(word for word in cleaned_review.split() if word.lower() not in unwanted_words)
        cleaned_reviews.append(cleaned_review)

    combined_text = ' '.join(cleaned_reviews)
    blob = TextBlob(combined_text)
    sentiment_score = blob.sentiment.polarity

    return sentiment_score

# Function to recommend similar movies
@st.cache_data
def recommend_similar_movies(df, similarity, movie_name, top_n=10):
    # Simulating loading animation
    with st.spinner("Fetching similar movies..."):
        time.sleep(1)  # Reduced sleep time
        
    if movie_name in df['movie_name'].values:
        index = df[df['movie_name'] == movie_name].index[0]
        distance = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])

        recommended_movies = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit scraping reviews tasks for all movies
            future_to_reviews = {executor.submit(scrape_top_reviews, df.iloc[i[0]]['movie_id']): i for i in distance[1:top_n+1]}
            for future in concurrent.futures.as_completed(future_to_reviews):
                index = future_to_reviews[future]
                try:
                    reviews = future.result()
                    sentiment_score = clean_and_analyze_sentiment(reviews)
                    rating = df.iloc[index[0]]['rating']  # Fetch movie rating
                    combined_score = (rating * 5) + (sentiment_score * 50)
                    recommended_movies.append((df.iloc[index[0]]['movie_id'], combined_score, df.iloc[index[0]]['movie_name']))
                except Exception as exc:
                    print(f"Error fetching reviews: {exc}")
        
        # Sort recommended movies based on combined score
        recommended_movies.sort(key=lambda x: x[1], reverse=True)
        
        return recommended_movies
    else:
        return None