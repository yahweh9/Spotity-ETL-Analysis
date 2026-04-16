# 🎧 Spotify ETL & Data Analysis Project

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** and **exploratory data analysis (EDA)** on a Spotify tracks dataset. The goal is to uncover relationships between audio features and generate insights into music trends and popularity.

---

## 📌 Project Overview

In this project, I:
- Cleaned and transformed raw Spotify data from Kaggle https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
- Engineered new features for better analysis
- Performed exploratory data analysis (EDA)
- Visualized relationships between key audio features
- Generated insights into genre characteristics and song popularity

---

## ⚙️ Tech Stack

- **Python**
- **Pandas** & **NumPy**
- **Matplotlib** & **Seaborn**
- **Scikit-Learn** (PCA, K-Means, TF-IDF)
- **APIs** (Spotipy, Requests)

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
- Exported the transformed dataset to a structured CSV file (`data/cleaned_spotify_tracks.csv`) to serve as the foundational database for the machine learning pipeline.

---

## 🧠 Machine Learning & NLP Recommendation Engine

To bypass the recent deprecation of Spotify's developer API for live audio features, this project engineers a multi-stage recommendation architecture bridging **Unsupervised Learning** and **Natural Language Processing (NLP)**.

* **Audio Profiling (K-Means & PCA):** Processed historical audio metrics (energy, valence, acousticness) through Principal Component Analysis for dimensionality reduction, utilizing K-Means to mathematically group the 113,000-track database into 15 distinct cluster profiles.
* **Semantic Tag Extraction (Last.fm API):** Transitioned from audio-frequency analysis to semantic analysis by pinging the Last.fm API to retrieve live, crowd-sourced human text tags for user-inputted tracks.
* **The NLP Pipeline (TF-IDF & Cosine Similarity):** Initialized a TF-IDF Vectorizer to translate human text tags into mathematical vectors. Calculated Cosine Similarity across the local database to find the mathematical nearest-neighbors to the target vibe.

---


## 🔮 Future Enhancements (Roadmap)
While the core recommendation engine is fully functional locally, active development is underway to expand the pipeline's production capabilities:
* **Automated Spotify Delivery:** Integrating the `spotipy` library and OAuth2.0 to allow the pipeline to automatically construct a public playlist and push the top 20 candidate tracks directly to a live Spotify user account.
* **Live Audio Feature Fallback:** Implementing an acoustic-analysis fallback script (e.g., Librosa) to mathematically approximate Spotify's deprecated audio features for newly released, untagged tracks.
