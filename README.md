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
