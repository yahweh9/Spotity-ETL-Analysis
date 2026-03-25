# Spotity-ETL-Analysis
🎧 Spotify Tracks ETL & Data Analysis

This project demonstrates an end-to-end ETL pipeline and exploratory data analysis using a Spotify dataset from Kaggle.

📌 Project Objectives
Clean and transform raw music data
Perform feature engineering
Analyze relationships between audio features
Generate insights about music trends and popularity
⚙️ Tech Stack
Python
Pandas
NumPy
Matplotlib
Seaborn
🔄 ETL Pipeline
Extract
Dataset loaded from Kaggle
Removed unnecessary columns (Unnamed: 0)
Transform
Handled missing values (artists, album_name, track_name)
Identified duplicate tracks
Created new feature:
duration_min from duration_ms
Performed sanity checks:
0 BPM songs
0 duration tracks
Load
Exported cleaned dataset to:
data/processed/cleaned_spotify_tracks.csv
📊 Key Analysis
🔥 Correlation Heatmap

Key Insights:

Strong positive correlation:
Loudness ↔ Energy (0.76)
Strong negative correlation:
Energy ↔ Acousticness (-0.76)
Moderate relationship:
Danceability ↔ Valence (0.48)

👉 Insight:
There is no strong correlation with popularity, suggesting external factors like:

Artist fame
Social media trends
Playlist placement
🎵 Genre Audio Signature (Radar Chart)

Key Observations:

Classical:
High acousticness & instrumentalness
Very low energy & danceability
Pop vs K-pop:
Nearly identical audio profiles
High energy, danceability, valence
Heavy Metal vs Hip-Hop:
Metal: high energy, low danceability
Hip-hop: high speechiness & groove
📈 Key Takeaways
Energy and loudness are strongly linked
Acoustic and energetic songs are inversely related
Popularity cannot be predicted from audio features alone
🚀 Future Improvements
Build a machine learning model to predict popularity
Deploy a dashboard using Streamlit
Add Spotify API integration
📂 Dataset

Available on Kaggle:
👉 Spotify Tracks Dataset
