🎧 Spotify Music Recommendation System

A content-based music recommender system built using Spotify audio features and deployed as an interactive Streamlit web application. The app suggests similar songs based on audio similarity and allows users to explore tracks, genres, artists, and manage favorites.

🚀 Features

🔍 Song Search with Fuzzy Matching
Handles typos and partial song names using fuzzy string matching.

🎶 Personalized Song Recommendations
Recommends similar songs based on:

Energy

Danceability

Valence

🎼 Genre Explorer
Browse songs by genre.

🎤 Artist Explorer
View songs by selected artists.

❤️ Favorites Section
Save recommended songs to a favorites list during the session.

📊 Similarity Visualization
Displays similarity scores using progress bars.

🧠 Recommendation Logic

This is a content-based filtering system:

Spotify audio features are scaled using StandardScaler

Cosine similarity is computed between songs

Songs with the highest similarity scores are recommended

🛠️ Tech Stack

Python

Streamlit – Frontend & app deployment

Pandas / NumPy – Data handling

Scikit-learn – Feature scaling & similarity calculation

FuzzyWuzzy – Fuzzy string matching

📂 Dataset

File used: spotify_cleaned.csv

Contains:

Track name

Artist

Genre

Audio features (energy, danceability, valence)

⚠️ Dataset must be placed in the same directory as the app file.

▶️ How to Run the App
# Install dependencies
pip install streamlit pandas numpy scikit-learn fuzzywuzzy python-Levenshtein

# Run the app
streamlit run app.py


(Rename your file if needed, e.g., app.py)

📸 App Sections

About Recommender – Explains how recommendations work

Song Search – Enter a song and get recommendations

All Songs – Browse the full dataset

Genre Explorer – Filter songs by genre

Artists – Explore songs by artist

🎯 Use Cases

Music discovery platforms

Personalized recommendation systems

Demonstrating ML concepts like similarity metrics

Data Science portfolio projects

📌 Future Improvements

Spotify API integration for real-time data

Album artwork & song preview links

User-based collaborative filtering

Persistent user profiles & favorites

Deployment on Streamlit Cloud / Hugging Face Spaces

👤 Author

Gulshanpreet Kaur
Data Science & AI Enthusiast
