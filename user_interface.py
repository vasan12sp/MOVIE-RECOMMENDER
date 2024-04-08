import streamlit as st
from recommender_mechanism import load_and_preprocess_data, vectorize_tags, calculate_cosine_similarity, recommend_similar_movies

# Function to get user input and recommend movies
def get_user_input_and_recommend(df, similarity):
    movie_names = df['movie_name'].tolist()  # Get a list of all movie names
    
    user_input = st.selectbox("Enter a movie name:", movie_names)

    if user_input:
        recommended_movies = recommend_similar_movies(df, similarity, user_input)
        if recommended_movies:
            st.write("\nTop 10 Similar Movies:")

            for movie_id, combined_score, movie_name in recommended_movies:
                imdb_url = f"https://www.imdb.com/title/{movie_id}/"
                st.markdown(f"[{movie_name}]({imdb_url})")
                st.write(f"Combined Score: {combined_score}")
        else:
            st.write("Movie not found in the dataset.")

# Main function
def main():
    st.title("Movie Recommender System")
    
    file_path = 'DataPreProcessing/final_merged_data.csv'
    df = load_and_preprocess_data(file_path)
    vector, cv = vectorize_tags(df)
    similarity = calculate_cosine_similarity(vector)

    get_user_input_and_recommend(df, similarity)

if __name__ == "__main__":
    main()
