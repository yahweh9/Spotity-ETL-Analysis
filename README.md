# 🎧 Spotify ETL & Data Analysis Project

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** and **exploratory data analysis (EDA)** on a Spotify tracks dataset. The goal is to uncover relationships between audio features and generate insights into music trends and popularity.

---

## 📌 Project Overview

In this project, I:
- Cleaned and transformed raw Spotify data
- Engineered new features for better analysis
- Performed exploratory data analysis (EDA)
- Visualized relationships between key audio features
- Generated insights into genre characteristics and song popularity

---

## ⚙️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

---

## 🔄 ETL Pipeline

### 🟢 Extract
- Loaded dataset from Kaggle
- Removed unnecessary columns (`Unnamed: 0`)

### 🟡 Transform
- Handled missing values (`artists`, `album_name`, `track_name`)
- Identified duplicate records (same artist + track name)
- Created new feature:
  - `duration_min` (converted from milliseconds)
- Performed sanity checks:
  - Tracks with 0 BPM
  - Tracks with 0 duration

### 🔵 Load
- Exported cleaned dataset to:
This is looking like a fantastic start, but right now, your README is completely missing the best part of your project!

The draft you provided only covers the standard data cleaning (Notebook 1). We need to finish that Load section and then immediately add a massive section highlighting the Machine Learning and NLP pipeline we just built in Notebooks 2 and 3. If a recruiter only reads your README, they need to know you built an AI-driven recommendation engine, not just a data-cleaning script.

Here is the complete, highly technical rest of the README. You can copy and paste this directly beneath your 🔵 Extract and 🟡 Transform sections.

🔵 Load
Exported the transformed dataset to a structured CSV file (data/cleaned_spotify_tracks.csv) to serve as the foundational database for the machine learning pipeline.

🧠 Machine Learning & NLP Recommendation Engine
To bypass the recent deprecation of Spotify's developer API for live audio features, this project engineers a multi-stage recommendation architecture bridging Unsupervised Learning and Natural Language Processing (NLP).

Audio Profiling (K-Means & PCA): Processed historical audio metrics (energy, valence, acousticness) through Principal Component Analysis for dimensionality reduction, utilizing K-Means to mathematically group the 113,000-track database into 15 distinct cluster profiles.

Semantic Tag Extraction (Last.fm API): Transitioned from audio-frequency analysis to semantic analysis by pinging the Last.fm API to retrieve live, crowd-sourced human text tags for user-inputted tracks.

The NLP Pipeline (TF-IDF & Cosine Similarity): Initialized a TF-IDF Vectorizer to translate human text tags into mathematical vectors. Calculated Cosine Similarity across the local database to find the mathematical nearest-neighbors to the target vibe.

Production Delivery (Spotify API): Utilized the spotipy library and OAuth2.0 authentication to automatically generate a public playlist containing the top 20 recommendations and push it directly to a live Spotify account.

🚀 How to Run Locally
1. Clone the repository
Bash
git clone https://github.com/YOUR_USERNAME/Spotity-ETL-Analysis.git
cd Spotity-ETL-Analysis
2. Install dependencies
Bash
pip install pandas numpy scikit-learn spotipy python-dotenv requests matplotlib seaborn
3. Environment Setup (Crucial!)
This project relies on secure external APIs. You must provide your own API keys to execute Notebook 3.
Create a file named exactly .env in the root folder of the project and add your credentials:

Plaintext
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
LASTFM_API_KEY=your_lastfm_api_key
(Note: A .gitignore file is already included to ensure your .env file is never accidentally uploaded to GitHub).

4. Execute the Pipeline
Launch Jupyter Notebook and run the files sequentially:

01_ETL_and_EDA.ipynb

02_KMeans_Clustering.ipynb

03_NLP_Recommendation_Pipeline.ipynb
