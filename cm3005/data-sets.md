# Most Streamed Spotify Songs 2024

This dataset presents a comprehensive compilation of the most streamed songs on Spotify in 2024. It provides extensive insights into each track's attributes, popularity, and presence on various music platforms, offering a valuable resource for music analysts, enthusiasts, and industry professionals.

## Key Features

* Track Name: Name of the song.
* Album Name: Name of the album the song belongs to.
* Artist: Name of the artist(s) of the song.
* Release Date: Date when the song was released.
* ISRC: International Standard Recording Code for the song.
* All Time Rank: Ranking of the song based on its all-time popularity.
* Track Score: Score assigned to the track based on various factors.
* Spotify Streams: Total number of streams on Spotify.
* Spotify Playlist Count: Number of Spotify playlists the song is included in.
* Spotify Playlist Reach: Reach of the song across Spotify playlists.
* Spotify Popularity: Popularity score of the song on Spotify.
* YouTube Views: Total views of the song's official video on YouTube.
* YouTube Likes: Total likes on the song's official video on YouTube.
* TikTok Posts: Number of TikTok posts featuring the song.
* TikTok Likes: Total likes on TikTok posts featuring the song.
* TikTok Views: Total views on TikTok posts featuring the song.

## Potential Use Cases

* Music Analysis: Analyze trends in audio features to understand popular song characteristics.
* Platform Comparison: Compare song popularity across different music platforms.
* Artist Impact: Study the relationship between artist attributes and song success.
* Temporal Trends: Identify changes in music attributes and preferences over time.
* Cross-Platform Presence: Investigate song performance across various streaming services.

## Dataset Details

* Origin: The dataset was obtained from Kaggle, a popular platform for data science competitions and hosting datasets.
* Size: The dataset contains approximately 10,000 entries, making it manageable for analysis and processing.
* Structure: The dataset is structured in a tabular format, with each row representing a unique song and each column representing a specific attribute or metric.
* Data Types: The dataset includes a mix of numerical and categorical data types, such as integers, floats, and strings.

## Fitness for Linear Regression

The "Most Streamed Spotify Songs 2024" dataset is suitable for linear regression analysis because it provides a comprehensive compilation of the most streamed songs on Spotify in 2024, along with various metrics related to their popularity. The dataset's structure and data types make it ideal for analyzing the relationships between different attributes and metrics, such as the relationship between Spotify streams and YouTube views.

---

# Spotify and Youtube

This dataset contains statistics for the top 10 songs of various Spotify artists and their YouTube videos.

## Content

The dataset includes 26 variables for each song, including:

* Track: Name of the song
* Artist: Name of the artist
* Url_spotify: URL of the artist on Spotify
* Album: Album the song is contained in on Spotify
* Album_type: Indicates if the song is released as a single or contained in an album
* Uri: Spotify link used to find the song through the API
* Danceability: Measures how suitable a track is for dancing
* Energy: Measures the intensity and activity of a track
* Key: The key the track is in
* Loudness: Overall loudness of a track in decibels (dB)
* Speechiness: Detects the presence of spoken words in a track
* Acousticness: Confidence measure of whether the track is acoustic
* Instrumentalness: Predicts whether a track contains no vocals
* Liveness: Detects the presence of an audience in the recording
* Valence: Measures the musical positiveness conveyed by a track
* Tempo: Overall estimated tempo of a track in beats per minute (BPM)
* Duration_ms: Duration of the track in milliseconds
* Stream: Number of streams of the song on Spotify
* Url_youtube: URL of the video linked to the song on YouTube
* Title: Title of the video clip on YouTube
* Channel: Name of the channel that published the video
* Views: Number of views
* Likes: Number of likes
* Comments: Number of comments
* Description: Description of the video on YouTube
* Licensed: Indicates whether the video represents licensed content
* official_video: Boolean value indicating if the video found is the official video of the song

## Notes

These data are heavily dependent on the time they were collected, which is in this case February 7th, 2023.

## Dataset Details

* Origin: The dataset was obtained from Kaggle, a popular platform for data science competitions and hosting datasets.
* Size: The dataset contains approximately 10,000 entries, making it manageable for analysis and processing.
* Structure: The dataset is structured in a tabular format, with each row representing a unique song and each column representing a specific attribute or metric.
* Data Types: The dataset includes a mix of numerical and categorical data types, such as integers, floats, and strings.

## Fitness for Linear Regression

The "Spotify and Youtube" dataset is suitable for linear regression analysis because it provides a comprehensive compilation of audio features and performance metrics for the top 10 songs of various Spotify artists and their YouTube videos. The dataset's structure and data types make it ideal for analyzing the relationships between different attributes and metrics, such as the relationship between danceability and energy.
