import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the datasets
spotify_data = pd.read_csv('data/raw/Spotify_Youtube.csv')
most_streamed_data = pd.read_csv('data/raw/Most Streamed Spotify Songs 2024.csv', encoding='latin1')

# Print the first few rows of each dataset
print(spotify_data.head())
print(most_streamed_data.head())

# Check for missing values
print(spotify_data.isnull().sum())
print(most_streamed_data.isnull().sum())

# Drop any rows with missing values
spotify_data.dropna(inplace=True)
most_streamed_data.dropna(inplace=True)

# Normalize the data
scaler = MinMaxScaler()
if not spotify_data.empty:
    spotify_data[['Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']] = scaler.fit_transform(spotify_data[['Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']])
if not most_streamed_data.empty:
    most_streamed_data[['Track Score', 'Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes', 'TikTok Views']] = scaler.fit_transform(most_streamed_data[['Track Score', 'Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes', 'TikTok Views']])

# Save the preprocessed data to new CSV files
if not spotify_data.empty:
    spotify_data.to_csv('data/preprocessed/Spotify_Youtube.csv', index=False)
if not most_streamed_data.empty:
    most_streamed_data.to_csv('data/preprocessed/Most Streamed Spotify Songs 2024.csv', index=False)
