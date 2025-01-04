# Data Preprocessing Summary

## Overview
This document describes the preprocessing steps undertaken to prepare the Spotify and YouTube music datasets for analysis. The preprocessing involved combining two datasets while ensuring data quality, handling duplicates, and standardizing formats.

## Source Datasets

### 1. Spotify-YouTube Dataset
- **Size**: 20,718 entries with 28 columns
- **Content**: Contains detailed audio features and performance metrics
- **Key Features**: Audio characteristics (danceability, energy, etc.) and platform metrics
- **Missing Data**: Minimal missing values in core features, some gaps in platform metrics

### 2. Most Streamed Spotify Songs 2024
- **Size**: 4,600 entries with 29 columns
- **Content**: Recent streaming data across multiple platforms
- **Key Features**: Cross-platform performance metrics
- **Missing Data**: Varies by platform, complete core data

## Preprocessing Steps

### 1. Data Loading and Initial Analysis
- Loaded both datasets with appropriate encoding (latin1)
- Performed initial analysis of data types and missing values
- Identified key columns for integration

### 2. Missing Value Analysis
#### Spotify-YouTube Dataset:
- Audio features: 2 missing entries
- YouTube metrics: 470-876 missing entries
- Stream count: 576 missing entries

#### Spotify 2024 Dataset:
- Core data (Track, Album): Complete
- Artist: 5 missing entries
- Platform metrics:
  * Spotify Streams: 113 missing
  * YouTube metrics: ~300 missing
  * TikTok metrics: ~1,000 missing
  * TIDAL Popularity: Completely empty (4,600 missing)

### 3. Data Cleaning and Standardization
- Normalized all column names to snake_case format
- Standardized text data:
  * Converted to lowercase
  * Removed extra spaces
  * Cleaned special characters
- Converted data types:
  * Duration: milliseconds to seconds
  * Dates: string to datetime
  * Numeric values: handled comma separators and type conversion

### 4. Duplicate Management
- Created composite keys using track and artist names
- Identified 1,303 duplicate songs between datasets
- Resolution strategy:
  * Preferred newer data from 2024 dataset
  * Preserved unique features from both datasets

### 5. Data Integration
- Combined datasets while maintaining data integrity
- Aligned column names and data types
- Final dataset structure:
  * 24,012 entries
  * 22 columns including:
    - Core song information (track, artist, album)
    - Audio features (danceability, energy, etc.)
    - Performance metrics (streams, views, likes)
    - Platform-specific metrics (TikTok data)
    - Temporal data (release dates)

### 6. First Normal Form (1NF) Compliance
- Ensured atomic values in all columns
- Eliminated repeating groups
- Established unique identifiers
- Standardized data types across columns

## Output Dataset
The preprocessed dataset is saved as 'combined_dataset.csv' in the data/preprocessed directory, featuring:
- Standardized column names
- Consistent data formats
- Handled missing values
- Removed duplicates
- Integrated cross-platform metrics

## Data Quality Improvements
1. **Completeness**: Merged complementary data from both sources
2. **Consistency**: Standardized formats and naming conventions
3. **Accuracy**: Preferred recent data for duplicate entries
4. **Usability**: Structured for straightforward analysis
5. **Integrity**: Maintained relationships between different metrics

The preprocessed dataset is now ready for statistical analysis and machine learning model development, with clean, standardized data that maintains the richness of both source datasets.
