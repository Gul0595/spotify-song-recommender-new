import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Spotify Music Recommender",
    page_icon="🎧",
    layout="wide"
)

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("spotify_cleaned.csv")
    return df

df = load_data()

# -------------------------------
# Preprocessing
# -------------------------------
FEATURES = ["energy", "danceability", "valence"]
scaler = StandardScaler()
feature_matrix = scaler.fit_transform(df[FEATURES])
similarity_matrix = cosine_similarity(feature_matrix)

# -------------------------------
# Helper Functions
# -------------------------------
def get_fuzzy_match(song_name):
    match, score = process.extractOne(song_name, df["track_name"])
    return match, score

def recommend_songs(song_name, top_n=10):
    idx = df[df["track_name"] == song_name].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1: top_n + 1]]
    results = df.iloc[top_indices].copy()
    results["similarity"] = [sim_scores[i + 1][1] for i in range(len(top_indices))]
    return results

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🎧 Spotify Navigator")

menu = st.sidebar.radio(
    "Explore",
    [
        "🏠 About Recommender",
        "🔍 Song Search",
        "🎶 All Songs",
        "🎼 Genre Explorer",
        "🎤 Artists",
    ],
)

# -------------------------------
# Session State
# -------------------------------
if "favorites" not in st.session_state:
    st.session_state.favorites = []

results = None

# -------------------------------
# Pages
# -------------------------------
if menu == "🏠 About Recommender":
    st.title("🎧 Spotify Recommendation System")
    st.markdown("""
    **This app recommends songs based on audio similarity**
    - Energy
    - Danceability
    - Valence
    """)

elif menu == "🔍 Song Search":
    st.title("🔍 Song Recommendation")

    song_input = st.text_input("Enter a song name")
    top_n = st.slider("Number of recommendations", 5, 20, 10)

    if st.button("🎶 Recommend Songs"):
        matched_song, score = get_fuzzy_match(song_input)

        if score < 70:
            st.error("Song not found confidently")
        else:
            st.success(f"Matched Song: {matched_song}")
            results = recommend_songs(matched_song, top_n)

    if results is not None:
        cols = st.columns(2)
        for i, row in results.iterrows():
            with cols[i % 2]:
                st.markdown(
                    f"""
                    **🎶 {row['track_name']}**  
                    Artist: {row['artists']}  
                    Genre: {row['track_genre']}
                    """
                )
                st.progress(float(row["similarity"]))

                if st.button("❤️ Add to Favorites", key=f"fav_{row['track_name']}"):
                    st.session_state.favorites.append(row["track_name"])

elif menu == "🎶 All Songs":
    st.title("🎶 All Songs")
    st.dataframe(df[["track_name", "artists", "track_genre"]])

elif menu == "🎼 Genre Explorer":
    st.title("🎼 Genre Explorer")
    genre = st.selectbox("Select Genre", sorted(df["track_genre"].unique()))
    st.dataframe(df[df["track_genre"] == genre].head(20))

elif menu == "🎤 Artists":
    st.title("🎤 Artists")
    artist = st.selectbox("Select Artist", sorted(df["artists"].unique()))
    st.dataframe(df[df["artists"] == artist].head(20))

# -------------------------------
# Sidebar Favorites
# -------------------------------
st.sidebar.markdown("## ❤️ Favorites")
if st.session_state.favorites:
    for fav in st.session_state.favorites:
        st.sidebar.write("🎵", fav)
else:
    st.sidebar.info("No favorites yet")
