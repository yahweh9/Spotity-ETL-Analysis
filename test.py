import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load your clean dataset
df_clean = pd.read_csv('data/cleaned_spotify_tracks.csv')

features_to_use = [
    'danceability', 'energy', 'loudness', 'speechiness', 
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'
]

print("--- STARTING OFFLINE PIPELINE ---")

# 1. Scale the Data
print("1. Scaling features...")
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_clean[features_to_use])

# 2. Apply PCA (Principal Component Analysis)
# We are compressing 9 features into 4 "Super Features" to remove noise
print("2. Running PCA...")
pca = PCA(n_components=4, random_state=42)
pca_features = pca.fit_transform(scaled_features)

# Calculate how much of the original "story" we kept (Variance)
variance_kept = sum(pca.explained_variance_ratio_) * 100
print(f"   -> PCA compressed 9 features into 4, keeping {variance_kept:.1f}% of the original variance!")

# 3. Apply KMeans Clustering
# Let's group the 113,000 songs into 15 distinct "Vibe Clusters"
print("3. Running KMeans Clustering (Grouping into 15 Vibes)...")
# n_init=10 ensures the algorithm runs a few times to find the absolute best center points
kmeans = KMeans(n_clusters=15, random_state=42, n_init=10)
kmeans.fit(pca_features)

# 4. Save the results back to our dataframe
df_clean['cluster_id'] = kmeans.labels_

print("--- OFFLINE PIPELINE COMPLETE ---\n")

# Let's peek at the distribution to see how many songs ended up in each cluster
print("Cluster Population Breakdown:")
print(df_clean['cluster_id'].value_counts().sort_index())

print("\n--- CRACKING OPEN THE CLUSTERS ---")

# We only want to look at the features that are easy for humans to understand
human_features = ['danceability', 'energy', 'acousticness', 'valence', 'tempo']

# Calculate the average (mean) of every feature for each cluster
cluster_averages = df_clean.groupby('cluster_id')[human_features].mean()

# Loop through all 15 clusters to print their "Profile"
for cluster_num in range(15):
    print(f"🔍 CLUSTER {cluster_num}")
    
    # 1. Get the average stats for this specific cluster
    stats = cluster_averages.loc[cluster_num]
    
    # 2. Find the top 3 most common genres in this cluster
    top_genres = df_clean[df_clean['cluster_id'] == cluster_num]['track_genre'].value_counts().head(3).index.tolist()
    
    # 3. Find 3 highly popular songs as examples
    top_songs = df_clean[df_clean['cluster_id'] == cluster_num].sort_values(by='popularity', ascending=False).drop_duplicates('track_name').head(3)
    combined_names = top_songs['track_name'] + " (by " + top_songs['artists'] + ")"
    song_names = combined_names.tolist()

    # Print the profile!
    print(f"   Vibe:   Energy: {stats['energy']:.2f} | Dance: {stats['danceability']:.2f} | Acoustic: {stats['acousticness']:.2f} | Happiness: {stats['valence']:.2f}")
    print(f"   Genres: {', '.join(top_genres).title()}")
    print(f"   Tracks: {', '.join(song_names)}")
    print("-" * 50)