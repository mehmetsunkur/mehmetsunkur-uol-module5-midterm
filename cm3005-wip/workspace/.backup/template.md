For this project, we are utilizing a comprehensive music streaming dataset sourced from Kaggle that combines data from both Spotify and YouTube platforms. The dataset provides a rich collection of musical attributes and performance metrics that make it particularly suitable for linear regression analysis in predicting streaming performance.

The dataset encompasses a wide range of musical and performance metrics across 26 variables, combining both quantitative and qualitative data types. Key numerical features include audio characteristics such as danceability (0-1 scale), energy (0-1 scale), loudness (decibels), tempo (BPM), and duration (milliseconds). Performance metrics include Spotify stream counts and YouTube engagement metrics (views, likes, and comments), providing robust dependent variables for our analysis.

The data structure presents several preprocessing challenges that make it ideal for this assignment. First, the dataset contains information split across two platforms (Spotify and YouTube), requiring joining and normalization. Second, there are missing values in the YouTube metrics for songs without corresponding YouTube presence, providing an opportunity for data cleaning and imputation. The presence of both categorical variables (such as album_type and licensed status) and continuous variables (such as tempo and loudness) necessitates appropriate preprocessing steps to prepare the data for linear regression.

The dataset's fitness for linear regression analysis is particularly strong due to the continuous nature of many variables and the potential linear relationships between audio features and streaming performance. For example, we can investigate how characteristics like danceability and energy correlate with streaming numbers, or how YouTube engagement metrics might predict Spotify success.

The selection of this dataset aligns perfectly with our project objectives as it provides:
- Comprehensive musical attributes that could influence streaming success
- Multiple performance metrics for validation
- Sufficient complexity for meaningful preprocessing
- Rich feature set for engineering additional variables
- Adequate scale for statistical significance while remaining manageable for analysis

This dataset was obtained from the Kaggle platform, ensuring its accessibility and reproducibility for academic purposes.
