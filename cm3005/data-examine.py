import pandas as pd
import numpy as np
from datetime import datetime

def load_datasets():
    """
    Load both datasets and print their basic information
    """
    # Load datasets with encoding handling
    spotify_youtube = pd.read_csv('data/raw/Spotify_Youtube.csv', encoding='latin1')
    spotify_2024 = pd.read_csv('data/raw/Most Streamed Spotify Songs 2024.csv', encoding='latin1')
    
    print("Spotify YouTube Dataset Info:")
    print(spotify_youtube.info())
    print("\nMissing values in Spotify YouTube Dataset:")
    print(spotify_youtube.isnull().sum())
    print("\nSpotify 2024 Dataset Info:")
    print(spotify_2024.info())
    print("\nMissing values in Spotify 2024 Dataset:")
    print(spotify_2024.isnull().sum())
    
    return spotify_youtube, spotify_2024

def normalize_column_names(df):
    """
    Normalize column names to snake_case format
    """
    return df.rename(columns=lambda x: x.lower().replace(' ', '_'))

def clean_text_data(text):
    """
    Clean text data by removing special characters and standardizing format
    """
    if pd.isna(text):
        return text
    # Remove special characters and extra spaces
    cleaned = str(text).strip().lower()
    # Replace multiple spaces with single space
    cleaned = ' '.join(cleaned.split())
    return cleaned

def preprocess_spotify_youtube(df):
    """
    Preprocess Spotify YouTube dataset
    """
    # Normalize column names
    df = normalize_column_names(df)
    
    # Clean text columns
    text_columns = ['track', 'artist', 'album']
    for col in text_columns:
        df[col] = df[col].apply(clean_text_data)
    
    # Convert duration from ms to seconds
    df['duration_sec'] = df['duration_ms'] / 1000
    
    # Convert stream count to numeric, handling any non-numeric values
    df['stream'] = pd.to_numeric(df['stream'], errors='coerce')
    
    # Select relevant columns
    relevant_columns = [
        'track', 'artist', 'album', 'danceability', 'energy', 'key',
        'loudness', 'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo', 'duration_sec', 'stream',
        'views', 'likes', 'comments'
    ]
    
    return df[relevant_columns]

def preprocess_spotify_2024(df):
    """
    Preprocess Spotify 2024 dataset
    """
    # First normalize all column names to lowercase with underscores
    df = normalize_column_names(df)
    
    # Clean text columns
    text_columns = ['track', 'artist', 'album_name']
    for col in text_columns:
        df[col] = df[col].apply(clean_text_data)
    
    # Convert release_date to datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    
    # Convert numeric columns to appropriate types
    numeric_columns = ['spotify_streams', 'youtube_views', 'youtube_likes', 
                      'tiktok_posts', 'tiktok_likes', 'tiktok_views']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
    
    # Rename columns for consistency with the other dataset
    df = df.rename(columns={
        'album_name': 'album',
        'spotify_streams': 'stream',
        'youtube_views': 'views',
        'youtube_likes': 'likes'
    })
    
    # Select relevant columns
    relevant_columns = [
        'track', 'artist', 'album', 'release_date', 'stream',
        'views', 'likes', 'tiktok_posts', 'tiktok_likes', 'tiktok_views'
    ]
    
    return df[relevant_columns]

def identify_duplicates(df1, df2):
    """
    Identify duplicate songs between datasets based on track and artist
    """
    # Create a composite key for comparison
    df1['composite_key'] = df1['track'] + '|' + df1['artist']
    df2['composite_key'] = df2['track'] + '|' + df2['artist']
    
    # Find duplicates
    duplicates = set(df1['composite_key']).intersection(set(df2['composite_key']))
    
    print(f"\nNumber of duplicate songs found: {len(duplicates)}")
    if len(duplicates) > 0:
        print("\nSample of duplicate songs:")
        for key in list(duplicates)[:5]:
            print(f"- {key.replace('|', ' by ')}")
    
    return duplicates

def combine_datasets(spotify_youtube_df, spotify_2024_df):
    """
    Combine both datasets, handling duplicates and merging relevant information
    """
    # Process both datasets
    spotify_youtube_clean = preprocess_spotify_youtube(spotify_youtube_df)
    spotify_2024_clean = preprocess_spotify_2024(spotify_2024_df)
    
    # Identify duplicates
    duplicates = identify_duplicates(spotify_youtube_clean, spotify_2024_clean)
    
    # Remove composite key used for duplicate detection
    spotify_youtube_clean = spotify_youtube_clean.drop('composite_key', axis=1)
    spotify_2024_clean = spotify_2024_clean.drop('composite_key', axis=1)
    
    # For duplicate songs, prefer the newer 2024 dataset
    spotify_youtube_clean = spotify_youtube_clean[
        ~(spotify_youtube_clean['track'] + '|' + spotify_youtube_clean['artist']).isin(duplicates)
    ]
    
    # Combine datasets
    # First, identify common columns
    common_columns = list(set(spotify_youtube_clean.columns) & set(spotify_2024_clean.columns))
    unique_to_youtube = list(set(spotify_youtube_clean.columns) - set(spotify_2024_clean.columns))
    unique_to_2024 = list(set(spotify_2024_clean.columns) - set(spotify_youtube_clean.columns))
    
    # Create empty columns in each dataset for the unique columns from the other dataset
    for col in unique_to_youtube:
        spotify_2024_clean[col] = np.nan
    for col in unique_to_2024:
        spotify_youtube_clean[col] = np.nan
    
    # Combine the datasets
    combined_df = pd.concat([spotify_youtube_clean, spotify_2024_clean], ignore_index=True)
    
    # Save the combined dataset
    combined_df.to_csv('data/preprocessed/combined_dataset.csv', index=False)
    
    print("\nCombined Dataset Info:")
    print(combined_df.info())
    print("\nSample of combined dataset:")
    print(combined_df.head())
    
    return combined_df

def main():
    """
    Main function to execute the data preprocessing pipeline
    """
    print("Starting data preprocessing...")
    
    # Load datasets
    spotify_youtube_df, spotify_2024_df = load_datasets()
    
    # Combine and process datasets
    combined_df = combine_datasets(spotify_youtube_df, spotify_2024_df)
    
    print("\nData preprocessing completed successfully!")
    print(f"Combined dataset shape: {combined_df.shape}")

if __name__ == "__main__":
    main()
