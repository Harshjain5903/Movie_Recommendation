'''
Author: Bappy Ahmed
Email: entbappy73@gmail.com
Date: 2021-Nov-15
'''

import pickle
import streamlit as st
import requests
import pandas as pd # Added import for type hinting if needed later

def fetch_poster(movie_id):
    """Fetches the poster URL for a given movie ID from TMDB."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        data = requests.get(url)
        data.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
        data = data.json()
        poster_path = data.get('poster_path') # Use .get() to avoid error if key missing
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            print(f"DEBUG: No poster_path found for movie_id {movie_id}")
            return None # Return None if no poster path exists
    except requests.exceptions.RequestException as e:
        print(f"ERROR fetching poster for movie_id {movie_id}: {e}")
        return None
    except KeyError as e:
        print(f"ERROR: Unexpected key missing in API response for movie_id {movie_id}: {e}")
        print(f"API Response Data: {data}") # Print response data if key is missing
        return None


def recommend(movie_title):
    """Recommends top 5 similar movies based on the selected movie title."""
    try:
        # Find the index of the selected movie
        movie_index = movies[movies['title'] == movie_title].index[0]

        # Get similarity scores for the selected movie
        distances = similarity[movie_index]

        # Sort distances and get top 5 (excluding itself)
        # list(enumerate(...)) creates pairs of (index, similarity_score)
        # sorted(...) sorts these pairs by similarity_score (x[1]) in descending order
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movie_names = []
        recommended_movie_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id # Get movie ID from the original dataframe index
            recommended_movie_names.append(movies.iloc[i[0]].title)
            poster_url = fetch_poster(movie_id)
            recommended_movie_posters.append(poster_url) # Can be None if poster not found

        return recommended_movie_names, recommended_movie_posters

    except IndexError:
        st.error(f"Movie '{movie_title}' not found in the dataset's index. This might indicate an issue with the data loading or the movie list.")
        return [], []
    except Exception as e:
        st.error(f"An unexpected error occurred during recommendation: {e}")
        return [], []


# --- Streamlit App Layout ---

st.header('Movie Recommender System Using Machine Learning')

# Load data (consider adding error handling here too)
try:
    movies_dict = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict) # Convert dict back to DataFrame if needed, otherwise adjust loading
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("ERROR: movie_list.pkl or similarity.pkl not found. Please ensure the Jupyter notebook has been run successfully to generate these files in the 'artifacts' folder.")
    st.stop() # Stop execution if files are missing
except Exception as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)

    # Check if recommendations were found
    if names and posters:
        cols = st.columns(5) # Use a dynamic way to create columns
        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                # --- ADDED PRINT STATEMENT FOR DEBUGGING ---
                print(f"DEBUG Poster URL {i+1}: {posters[i]}")
                # --- Display image only if URL is valid ---
                if posters[i]:
                    st.image(posters[i])
                else:
                    st.caption("Poster not available") # Show a placeholder message
    else:
        # Handle case where recommend function returned empty lists (e.g., due to error)
        st.warning("Could not retrieve recommendations.")